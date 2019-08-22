from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from kafka import SimpleProducer, KafkaClient
import time

access_token = "68979886-IzdibLmYAx39y8PLNWA7kLPKl2rTDlLPCnf557I45"
access_token_secret =  "tjVsF4mx4vS9JO0hPcS7b8qoP7oIZK1A8nX0aMwhkNEDG"
consumer_key =  "jjSz1RE4ftTNmqB1XuUTM22Fc"
consumer_secret =  "5SNWrhQStzMp3UDwVY7YGuEofQ4QOBBP4rOo4hGnhKpdFQoVi9"


class StdOutListener(StreamListener):
    def on_data(self, data):
        producer.send_messages("pizza", data.encode('utf-8'))
        # print('tweet received')
#         print(data)
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
        stream.filter(track="pizza")
        success = True
    except:
        print("producer error")

