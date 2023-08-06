'''
Created on 2018/4/19

Preventing many time-consuming operations to be done in the same loop

:author: hubo
'''
from vlcp.event.event import withIndices, Event



@withIndices("limiter", "index")
class RateLimitingEvent(Event):
    pass


class RateLimiter(object):
    def __init__(self, limit, container):
        self._container = container
        self._limit = limit
        if self._limit <= 0:
            raise ValueError("Limit must be greater than 0")
        self._counter = 0
        self._task = None
        self._bottom_line = limit
    
    def _limiter_task(self):
        current_index = 0
        while True:
            for m in self._container.doEvents():
                yield m
            current_index += 1
            if current_index * self._limit >= self._counter:
                # Last event covers all (NOTICE: self._counter - 1 is the last limited)
                break
            else:
                # This will release from current_index * limit to (current_index + 1) * limit - 1
                self._container.scheduler.emergesend(RateLimitingEvent(self, current_index))
                self._bottom_line += self._limit
        # Reset counter
        self._counter = 0
        self._task = None
        self._bottom_line = self._limit
    
    def limit(self, use = 1):
        c = self._counter
        self._counter = c + use
        if self._task is None:
            self._task = self._container.subroutine(self._limiter_task(), False)
        if c >= self._bottom_line:
            # Limited
            yield (RateLimitingEvent.createMatcher(self, c // self._limit),)
        