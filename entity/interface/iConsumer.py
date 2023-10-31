import zope.interface

class iConsumer(zope.interface.Interface):
    def _subToTopic(self, topicName:str):
        pass