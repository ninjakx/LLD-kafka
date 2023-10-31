from service.QueueServiceImpl import QueueServiceImpl

if __name__ == "__main__":
    queueService = QueueServiceImpl()
    producer1 = queueService._createProducer("producer1")
    producer2 = queueService._createProducer("producer2")
    producer3 = queueService._createProducer("producer3")
    producer4 = queueService._createProducer("producer4")

    consumer1 = queueService._createConsumer("consumer1")
    consumer2 = queueService._createConsumer("consumer2")
    consumer3 = queueService._createConsumer("consumer3")
    
    producer1._publishToTopic("topic1", "message1")
    producer1._publishToTopic("topic1", "message2")
    producer2._publishToTopic("topic2", "message3")
    producer1._publishToTopic("topic1", "message4")

    consumer1._subToTopic("topic1")
    consumer1._subToTopic("topic2")

    consumer1._consumerRunner()