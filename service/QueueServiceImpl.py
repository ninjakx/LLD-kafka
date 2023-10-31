import zope.interface
from entity.interface.iProducer import iProducer
from entity.interface.iConsumer import iConsumer
from entity.implementation.ProducerImpl import ProducerImpl
from entity.implementation.ConsumerImpl import ConsumerImpl
from .iQueueService import iQueueService
from mediator.QueueMediatorImpl import QueueMediatorImpl

class QueueServiceMeta(type):
    _instance = {}
    def __call__(self, *args, **kwargs):
        if self not in self._instance:
            instance = super().__call__(*args, **kwargs)
            self._instance[self] = instance
        return self._instance[self]

@zope.interface.implementer(iQueueService)
class QueueServiceImpl:
    def __init__(self):
        self._qmd = QueueMediatorImpl()

    def _createTopic(self, topicName:str):
        self._qmd.createTopic(topicName)

    def _createProducer(self, producerName:str)->iProducer:
        return ProducerImpl(producerName)

    def _createConsumer(self, consumerName:str)->iConsumer:
        return ConsumerImpl(consumerName)
    

