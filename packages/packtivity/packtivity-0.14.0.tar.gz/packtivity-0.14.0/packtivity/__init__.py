import time
import logging
from datetime import datetime

from packtivity.utils import load_packtivity
from packtivity.syncbackends import defaultsyncbackend
from packtivity.typedleafs import TypedLeafs

log = logging.getLogger(__name__)

class pack_object(object):
    def __init__(self,spec):
        self.spec = spec

    @classmethod
    def fromspec(cls,*args,**kwargs):
        return cls(load_packtivity(*args,**kwargs))

    def __call__(self, parameters, state,
                 syncbackend = defaultsyncbackend(),
                 asyncbackend = None, asyncwait = False,
                 waitperiod = 0.01, timeout = 43200 ):   #default timeout is 12h

        parameters = TypedLeafs(parameters, state.datamodel)
        if syncbackend and not asyncbackend:
            return syncbackend.run(self.spec,parameters,state)
        elif asyncbackend:
            submit_time = datetime.fromtimestamp(time.time())
            proxy = asyncbackend.submit(self.spec, parameters, state)
            if not asyncwait:
                return proxy
            while True:
                if asyncbackend.ready(proxy):
                    return asyncbackend.result(proxy)
                timestamp = datetime.fromtimestamp(time.time())
                if (timestamp - submit_time).seconds > timeout:
                    raise RuntimeError('Timeout!')
                time.sleep(waitperiod)
