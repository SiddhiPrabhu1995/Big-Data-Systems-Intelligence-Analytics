
# GeoStreaming using Apache Kafka producer and consumer with FastAPI and aiokafka 

## What is Apache Kafka?

Apache Kafka is a messaging system with a producer producing a message on the one side and a consumer consuming the message on the other side with a broker (zookeeper) in the middle.

When a producer sends a message, the message is pushed into Kafka topics. 

When a consumer consumes a message it is pulling the message from a Kafka topic. Kafka topics reside within a so-called broker (eg. Zookeeper). Zookeeper provides synchronization within distributed systems and in the case of Apache Kafka keeps track of the status of Kafka cluster nodes and Kafka topics.

## Kafka core principles

![CorePrinc](https://user-images.githubusercontent.com/57429405/124399613-7ba80900-dcea-11eb-8369-569af100a5c4.png)

•	When a producer sends a message, the message is pushed into Kafka topics. When a consumer consumes a message it is pulling the message from a Kafka topic. 
•	Kafka topics reside within a so-called broker (eg. Zookeeper). Zookeeper provides synchronization within distributed systems and in the case of Apache Kafka keeps track of the status of Kafka cluster nodes and Kafka topics.
•	Multiple producers pushing messages into one topic, or you can have them push to different topics
•	 Messages within topics can be retained indefinitly or be discarded after a certain time, depending on the needs. 
•	When a consumer starts consuming a message, it starts from the first message that has been pushed to the topic and continues from thereon. 
•	Kafka stores the so-called offset, basically a pointer telling the consumer which messages have been consumed and what is still left to indulge.
•	 Messages will stay within the topic, yet when the same consumer pulls messages from the topic it will only receive messages from the offset onwards.


## Geo Stream Kafka architecture

![architecture](https://user-images.githubusercontent.com/57429405/124399617-86fb3480-dcea-11eb-813e-03ec5c6c62f5.png)

## STEP 1: Setup an Apache Kafka cluster

## STEP 2: Run docker and use cmd to run the following command

This command would help spin up multiple docker containers for your kafka client, zookeeper, a producer and a consumer.

![image](https://user-images.githubusercontent.com/57429405/125013614-1df12500-e03a-11eb-816e-e2454a981476.png)

## STEP 3: Change the configurations of producer and consumer

The KAFKA_URI and KAFKA_PORT need to be configured the KAFKA_URI for Mac would be the same as KAFKA_ADVERTISED_HOST_NAME.
The KAFKA_PORT would be 9092 if you haven't made changes to the docker file.

## STEP 4: FastAPI Apache Kafka producer

Wrap the producer into a FastAPI endpoint. This allows for more than one entity at a time to produce messages to a topic,
but also enables to flexibly change topics that I want to produce messages to with FastAPI endpoint path parameters. 

Used aiokafka to make use of FastAPIs async capabilities.

## STEP 5: FastAPI Apache Kafka consumer

Since FastAPI is built on-top of starlette we can use class-basedd endpoints and especially the WebsocketEndpoint to handle incoming Websocket Sessions.

When an application starts a websocket connection with out websocket endpoint we grab the event loop, use that to build and start the aiokafka consumer, start it and start a consumer task in the loop. 

Once this is set, everytime the consumer pulls a new message it is forwarded to the application through the websocket. 

## STEP 6: Leaflet application when opened starts consumer at the backend which consumes latitude and longitude data from the producer

![image](https://user-images.githubusercontent.com/57429405/125013409-c652b980-e039-11eb-838d-87df6271aa56.png)


