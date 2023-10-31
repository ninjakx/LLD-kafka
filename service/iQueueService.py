import zope.interface

class iQueueService(zope.interface.Interface):
     # singleton it will be
    def _createTopic(self, topicName:str):
        pass

    def _createProducer(self, producerName:str):
        pass

    def _createConsumer(self, consumerName:str):
        pass