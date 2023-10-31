import zope.interface
from ..interface.iProducer import iProducer
from ..Message import Message
from mediator.QueueMediatorImpl import QueueMediatorImpl

@zope.interface.implementer(iProducer)
class ProducerImpl:
    # producer will have its name and mediator to carry out everything
    def __init__(self, name):
        self.__producerName = name
        self.__queueMediator = QueueMediatorImpl()
    
    def __getQueueMediator(self):
        return self.__queueMediator

    # override  
    def _publishToTopic(self, topicName:str, msg:str):
        qmd = self.__getQueueMediator()
        msgObj = Message()
        msgObj._setMessage(msg)
        print(f"Msg: {msg} has been published to topic: {topicName}\n")
        qmd._publishToTopic(topicName, msgObj)



    