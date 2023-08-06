'''
Created on 2016/4/11

:author: hubo
'''
from vlcp.event.runnable import RoutineContainer
from vlcp.server.module import callAPI
from uuid import uuid1
from vlcp.event.event import Event, withIndices
from vlcp.utils.dataobject import multiwaitif
from vlcp.protocol.openflow.openflow import OpenflowErrorResultException
from namedstruct.namedstruct import dump
import json
import logging
from contextlib import closing

@withIndices('updater', 'type')
class FlowUpdaterNotification(Event):
    STARTWALK = 'startwalk'
    DATAUPDATED = 'dataupdated'
    FLOWUPDATE = 'flowupdate'

class FlowUpdater(RoutineContainer):
    def __init__(self, connection, initialkeys, requestid = None, logger = None):
        RoutineContainer.__init__(self, connection.scheduler)
        self._initialkeys = initialkeys
        self._connection = connection
        self._walkerdict = {}
        self._savedkeys = ()
        self._savedresult = []
        self._updatedset = set()
        self._updatedset2 = set()
        if not logger:
            self._logger = logging.getLogger(__name__ + '.FlowUpdater')
        else:
            self._logger = logger
        if requestid is None:
            self._requstid = str(uuid1())
        else:
            self._requstid = requestid
        self._requestindex = 0
        self._dataupdateroutine = None
        self._flowupdateroutine = None
    def reset_initialkeys(self, keys, values):
        pass
    def walkcomplete(self, keys, values):
        if False:
            yield
    def updateflow(self, connection, addvalues, removevalues, updatedvalues):
        if False:
            yield
    def shouldupdate(self, newvalues, updatedvalues):
        return True
    def restart_walk(self):
        self._restartwalk = True
        for m in self.waitForSend(FlowUpdaterNotification(self, FlowUpdaterNotification.STARTWALK)):
            yield m
    def _dataobject_update_detect(self):
        _initialkeys = set(self._initialkeys)
        def expr(newvalues, updatedvalues):
            if any(v.getkey() in _initialkeys for v in updatedvalues if v is not None):
                return True
            else:
                return self.shouldupdate(newvalues, updatedvalues)
        while True:
            for m in multiwaitif(self._savedresult, self, expr, True):
                yield m
            updatedvalues, _ = self.retvalue
            if not self._updatedset:
                self.scheduler.emergesend(FlowUpdaterNotification(self, FlowUpdaterNotification.DATAUPDATED))
            self._updatedset.update(updatedvalues)
    def updateobjects(self, updatedvalues):
        if not self._updatedset:
            self.scheduler.emergesend(FlowUpdaterNotification(self, FlowUpdaterNotification.DATAUPDATED))
        self._updatedset.update(set(updatedvalues).intersection(self._savedresult))
    def _flowupdater(self):
        lastresult = set(v for v in self._savedresult if v is not None and not v.isdeleted())
        flowupdate = FlowUpdaterNotification.createMatcher(self, FlowUpdaterNotification.FLOWUPDATE)
        while True:
            currentresult = [v for v in self._savedresult if v is not None and not v.isdeleted()]
            additems = []
            updateditems = []
            updatedset2 = self._updatedset2
            for v in currentresult:
                if v not in lastresult:
                    additems.append(v)
                else:
                    lastresult.remove(v)
                    if v in updatedset2:
                        # Updated
                        updateditems.append(v)
            removeitems = lastresult
            self._updatedset2.clear()
            lastresult = set(currentresult)
            if not additems and not removeitems and not updateditems:
                yield (flowupdate,)
                continue
            for m in self.updateflow(self._connection, set(additems), removeitems, set(updateditems)):
                yield m
                
    def main(self):
        try:
            lastkeys = set()
            dataupdate = FlowUpdaterNotification.createMatcher(self, FlowUpdaterNotification.DATAUPDATED)
            startwalk = FlowUpdaterNotification.createMatcher(self, FlowUpdaterNotification.STARTWALK)
            self.subroutine(self._flowupdater(), False, '_flowupdateroutine')
            presave_update = set()
            while True:
                self._restartwalk = False
                presave_update.update(self._updatedset)
                self._updatedset.clear()
                _initialkeys = set(self._initialkeys)
                try:
                    for m in callAPI(self, 'objectdb', 'walk', {'keys': self._initialkeys, 'walkerdict': self._walkerdict,
                                                                'requestid': (self._requstid, self._requestindex)}):
                        yield m
                except Exception:
                    self._logger.warning("Flow updater %r walk step failed, conn = %r", self, self._connection,
                                         exc_info=True)
                    # Cleanup
                    with closing(callAPI(self, 'objectdb', 'unwatchall',
                                         {'requestid': (self._requstid, self._requestindex)})) as g:
                        for m in g:
                            yield m
                    with closing(self.waitWithTimeout(2)) as g:
                        for m in g:
                            yield m
                    self._requestindex += 1
                if self._restartwalk:
                    continue
                if self._updatedset:
                    if any(v.getkey() in _initialkeys for v in self._updatedset):
                        continue
                lastkeys = set(self._savedkeys)
                self._savedkeys, self._savedresult = self.retvalue
                removekeys = tuple(lastkeys.difference(self._savedkeys))
                self.reset_initialkeys(self._savedkeys, self._savedresult)
                _initialkeys = set(self._initialkeys)
                if self._dataupdateroutine:
                    self.terminate(self._dataupdateroutine)
                self.subroutine(self._dataobject_update_detect(), False, "_dataupdateroutine")
                self._updatedset.update(v for v in presave_update)
                presave_update.clear()
                for m in self.walkcomplete(self._savedkeys, self._savedresult):
                    yield m
                if removekeys:
                    for m in callAPI(self, 'objectdb', 'munwatch', {'keys': removekeys,
                                                                    'requestid': self._requstid}):
                        yield m
                self._updatedset2.update(self._updatedset)
                self._updatedset.clear()
                for m in self.waitForSend(FlowUpdaterNotification(self, FlowUpdaterNotification.FLOWUPDATE)):
                    yield m
                while not self._restartwalk:
                    if self._updatedset:
                        if any(v.getkey() in _initialkeys for v in self._updatedset):
                            break
                        else:
                            self._updatedset2.update(self._updatedset)
                            self._updatedset.clear()
                            self.scheduler.emergesend(FlowUpdaterNotification(self, FlowUpdaterNotification.FLOWUPDATE))
                    yield (dataupdate, startwalk)
        except GeneratorExit:
            raise
        except Exception:
            self._logger.exception("Flow updater %r stops update by an exception, conn = %r", self, self._connection)
            raise
        finally:
            self.subroutine(callAPI(self, 'objectdb', 'unwatchall', {'requestid': (self._requstid, self._requestindex)}))
            if self._flowupdateroutine:
                self.terminate(self._flowupdateroutine)
                self._flowupdateroutine = None
            if self._dataupdateroutine:
                self.terminate(self._dataupdateroutine)
                self._dataupdateroutine = None
    def execute_commands(self, conn, cmds):
        if cmds:
            try:
                for m in conn.protocol.batch(cmds, conn, self):
                    yield m
            except OpenflowErrorResultException:
                self._logger.warning("Some Openflow commands return error result on connection %r, will ignore and continue.\n"
                                             "Details:\n%s", conn,
                                             "\n".join("REQUEST = \n%s\nERRORS = \n%s\n" % (json.dumps(dump(k, tostr=True), indent=2),
                                                                                            json.dumps(dump(v, tostr=True), indent=2))
                                                       for k,v in self.openflow_replydict.items()))
