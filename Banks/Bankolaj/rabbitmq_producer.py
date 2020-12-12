import pika
import json

if __name__ == '__main__':
    url = "amqps://epryvnth:U21Lp1tn8pQfKtxzBS3CYmh61CJ1_jje@hawk.rmq.cloudamqp.com/epryvnth"
    params = pika.URLParameters(url)
    connection = pika.BlockingConnection(params)

    channel = connection.channel()  # start a channel

    # TRANSFER
    trn = {
        "amount": 420,
        "orginCardNumber": "1234567890",
        "originCVC": "123",
        "targetAccountNumber": "111122223333"
    }

    # UPDATE
    upd = {
        "accountNumber": "111122223333",
        "amount": 420,
        "sourceAccountNumber": "1234567890",
        "sourceRegNumber": "0000",
    }

    channel.basic_publish(exchange='', routing_key='1234-transfer', body=json.dumps(trn))
    channel.basic_publish(exchange='', routing_key='1234-update', body=json.dumps(upd))
    connection.close()
