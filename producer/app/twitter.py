from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from kafka import SimpleProducer, KafkaClient
import time

access_token = "1171481005238046720-oAZIynrQkf5wmbbGkJziH5bU5P9mME"
access_token_secret =  "kUtpMapZwIK5FSWhJJmgEUGXfrYq8YMXNP44a2DCCq8zb"
consumer_key =  "BO36N0DiFpnpjnk4t4alFyJES"
consumer_secret =  "i1aYkttchtpoh3cI5vKY10s2RS7nigoIblaqf4rc0krvjgg1rm"


class StdOutListener(StreamListener):
    def on_data(self, data):
        producer.send_messages("amazon", data.encode('utf-8'))
        return True
    def on_error(self, status):
        print (status)


success = False
kafka = None
while success == False:
    time.sleep(1)
    
    try:
        kafka = KafkaClient("kafka:9092")
        producer = SimpleProducer(kafka)
        l = StdOutListener()
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        stream = Stream(auth, l)
        stream.filter(track="amazon")
        success = True
        
    except:
        print("producer error")

