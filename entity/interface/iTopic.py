import zope.interface

class iTopic(zope.interface.Interface):
        
    # add msg to the topic
    def _addMessage(self, msg:str):
        pass
    
    # check if any msg exist to read from it
    def _checkIfAnyMsgExist(self, offset:int):
        pass


