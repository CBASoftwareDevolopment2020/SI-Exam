import pika
import json

def main():
    url = "amqps://epryvnth:U21Lp1tn8pQfKtxzBS3CYmh61CJ1_jje@hawk.rmq.cloudamqp.com/epryvnth"
    params = pika.URLParameters(url)
    connection = pika.BlockingConnection(params)
    channel = connection.channel() # start a channel

    transfer_json = {
        "amount": 420,
        "orginCardNumber": "1234567890",
        "originCVC": "123",
        "targetAccountNumber": "111122223333",
        "targetRegNumber": "4651"
    }

    update_json = {
        "accountNumber": "111122223333",
        "amount": 420,
        "sourceAccountNumber": "1234567890",
        "sourceRegNumber": "0000",
    }

    channel.basic_publish(exchange='', routing_key='6969-transfer', body=json.dumps(transfer_json))
    channel.basic_publish(exchange='', routing_key='6969-update', body=json.dumps(update_json))
    connection.close()