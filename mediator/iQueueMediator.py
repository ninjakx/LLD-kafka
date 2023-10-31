import zope.interface
from entity.Message import Message

class iQueueMediator(zope.interface.Interface):
    # will have all the topics by topicName
    def _publishToTopic(self, topicName:str, msg:Message):
        pass

    def _addTopic(self, topicName:str):
        pass

    def _readMsgIfPresent(self, topicName:str, offset:int):
        pass
