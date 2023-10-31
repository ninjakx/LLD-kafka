import zope.interface
from ..interface.iTopic import iTopic
from ..Message import Message
from threading import RLock
# import time

@zope.interface.implementer(iTopic)
class TopicImpl:
    def __init__(self):
        self.__msges = [] #queue
        self.__msgWriterReentrantLock = RLock()
        # re entrant lock - TODO

    def _getReentrantWriterLock(self):
        return self.__msgWriterReentrantLock

    def __getMsges(self):
        return self.__msges


    def _addMessage(self, message:Message):
        # critical section as same topic will be part of multiple consumer. 
        self._getReentrantWriterLock().acquire()
        self.__msges.append(message)
        self._getReentrantWriterLock().release()

    def _readMsgIfPresent(self, offset:int)->Message: # return msg if present else return None
        queue = self.__getMsges()
        # time.sleep(3)
        if len(queue)<=offset: # what if it's empty and offset is zero 
            return None
        # critical setion
        self._getReentrantWriterLock().acquire()
        msg = queue[offset]
        self._getReentrantWriterLock().release()
        return msg


