import zope.interface
from ..interface.iConsumer import iConsumer
from collections import OrderedDict
from mediator.QueueMediatorImpl import QueueMediatorImpl

import threading 
from threading import Thread
import time
 
@zope.interface.implementer(iConsumer)
class ConsumerImpl:
    # will keep all the topic it has subscribed to and their offset

    def __init__(self, consumerName:str):
        self.__consumerName = consumerName
        self.__topicList = []
        self.__topicVsOffset = OrderedDict()
        self.__queueMediator = QueueMediatorImpl()
        self.threadInit()


    def threadInit(self):
        thread = Thread(target = self._consumerRunner)
        thread.start()
        # thread.join()
        # print("thread finished...exiting")        

    def __getConsumerName(self):
        return self.__consumerName

    def __getQueueMediator(self):
        return self.__queueMediator

    def __getSubscribedTopics(self)->list:
        return self.__topicList

    def __setTopicOffset(self, topicName:str, offset:int)->int:
        self.__topicVsOffset[topicName] = offset

    def __getTopicOffset(self, topicName:str)->int:
        return self.__topicVsOffset[topicName]

    def __addToTopicList(self, topicName:str)->None:
        self.__topicList.append(topicName)

    def _subToTopic(self, topicName:str):
        self.__addToTopicList(topicName)
        self.__topicVsOffset[topicName] = 0

    def __consumeMsg(self, msg:str, offset:int):
        print(f"Msg: {msg} has been consumed by consumer: {self.__getConsumerName()} at offset: {offset} with current thread: {threading.current_thread().name}\n")


    # pull based mechanism
    # running on single thread
    def _consumerRunner(self):
        while(True):
            for topicName in self.__getSubscribedTopics():
                curOffset = self.__getTopicOffset(topicName)
                qmd = self.__getQueueMediator()
                msg = qmd._readMsgIfPresent(topicName, curOffset)
                if msg is not None:
                    self.__consumeMsg(msg._getMessage(), curOffset)
                    curOffset += 1
                # update offset
                self.__setTopicOffset(topicName, curOffset)

            try:
                #sleep for 100 milliseconds
                #thread sleep
                # "sleep() makes the calling thread sleep until seconds seconds have elapsed or a signal arrives which is not ignored."
                time.sleep(0.1)
            except Exception as e:
                print(f"Error: {e}")


                





    




    