import os
import time
from kafka import KafkaConsumer
import pymongo
import json

kafka_topic = "amazon"

if __name__ == '__main__':

    myclient = pymongo.MongoClient("mongodb://root:example@mongo:27017/")
    mydb = myclient["test_database"]
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
        x = mycol.insert_one(record)







