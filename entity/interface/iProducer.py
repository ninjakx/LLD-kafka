import zope.interface

class iProducer(zope.interface.Interface):

    def _publishToTopic(self, topicName:str, msg:str):
        pass