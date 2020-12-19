import pika
import json
import dbmethods as db

url = "amqps://epryvnth:U21Lp1tn8pQfKtxzBS3CYmh61CJ1_jje@hawk.rmq.cloudamqp.com/epryvnth"
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)

channel = connection.channel() # start a channel

data = {"name": "Michael"}


channel.basic_publish(exchange='', routing_key='6969-transfer', body=json.dumps(data))
connection.close()