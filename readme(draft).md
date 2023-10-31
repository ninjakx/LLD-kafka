topic (multiple)
consumer (multiple)
producer (multiple)
queue (multiple)
message

queue will be particulary for a given topic and will serve the consumers that are relying on it.
will use offset to increment the index. 

### Topic
- create message
- check if any message present in this topic

Queue -> List<TOPIC>topics
Message -> string
Consumer -> int id

queueService:
- create producer -> which topic it is sending msg to
- create consumer , what topic it is consuming to
- create topics

consumer:
subscribe to topic

producer:
publish to topic

QueueMediator: will talk to the queue

public to topic
read msg if exist
add topic

-> singleton
-> hashmap: which topic it is having -> return that topic (get topic)






