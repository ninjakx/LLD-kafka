import zope.interface
from .iQueueMediator import iQueueMediator
from collections import OrderedDict
from entity.Message import Message
from entity.implementation.TopicImpl import TopicImpl

class QueueMediatorMeta(type):
    _instance = {}
    def __call__(self, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if self not in self._instance:
            instance = super().__call__(*args, **kwargs)
            self._instance[self] = instance
        return self._instance[self]

@zope.interface.implementer(iQueueMediator)
class QueueMediatorImpl(metaclass=QueueMediatorMeta):
    # will have all the topics by topicName
    def __init__(self):
       self.__topicMap = OrderedDict()

    def _publishToTopic(self, topicName:str, msg:Message):
        self._addTopic(topicName)
        self.__topicMap[topicName]._addMessage(msg)

    def _addTopic(self, topicName:str):
        if not self.__topicMap.get(topicName, False):
            self.__topicMap[topicName] = TopicImpl()

    def _readMsgIfPresent(self, topicName:str, offset:int)->Message:
        return self.__topicMap[topicName]._readMsgIfPresent(offset)

