import os
import time
from kafka import KafkaConsumer
import pymongo
import json

kafka_topic = "pizza"


if __name__ == '__main__':
    print('$$$$$$$$$$$ CONSUMER $$$$$$$$$$$$$$$$')

    myclient = pymongo.MongoClient("mongodb://root:example@mongo:27017/")
    mydb = myclient["tweetbase"]
    mycol = mydb["test"]


    success = False
    consumer = None
    while success == False:
        time.sleep(1)
        try:
            consumer = KafkaConsumer(bootstrap_servers=['kafka:9092'])
            consumer.subscribe([kafka_topic])
            success = True
        except:
            print("consumer error")


    for msg in consumer:
        record = json.loads(msg.value)
        # print(record)

        x = mycol.insert_one(record)


    #
    # # time.sleep(3)   # wait until Kafka is running
    # kafka_service = os.environ['KAFKA_SERVICE']
    # print("Consumer is using kafka service {0}".format(kafka_service))





