import pika
import json
from secrets import cloudamqp_host, cloudamqp_user, cloudamqp_password

if __name__ == '__main__':
    url = f'amqps://{cloudamqp_user}:{cloudamqp_password}@{cloudamqp_host}/{cloudamqp_user}'
    params = pika.URLParameters(url)
    connection = pika.BlockingConnection(params)

    channel = connection.channel()  # start a channel

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

    channel.basic_publish(exchange='', routing_key='1234-transfer', body=json.dumps(transfer_json))
    channel.basic_publish(exchange='', routing_key='1234-update', body=json.dumps(update_json))
    connection.close()
