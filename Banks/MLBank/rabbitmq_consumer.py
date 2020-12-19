import pika
import json
import ast
import dbmethods as db

def main():
    url = "amqps://epryvnth:U21Lp1tn8pQfKtxzBS3CYmh61CJ1_jje@hawk.rmq.cloudamqp.com/epryvnth"
    params = pika.URLParameters(url)
    connection = pika.BlockingConnection(params)
    channel = connection.channel() # start a channel


    def callback(ch, method, properties, body):
        data = ast.literal_eval(body.decode("UTF-8"))
        if method.routing_key == '6969-transfer':
            print('This is a transfer')
            acc_numb = db.validate_card(data['originCardNumber'], data['originCVC'])
            if acc_numb:
                print('Updating Balance')
                db.update_balance(acc_numb, data['amount'], data['targetAccountNumber'], data['targetRegNumber'])

                update = {
                    "accountNumber": data['targetAccountNumber'],
                    "amount": data['amount'],
                    "sourceAccountNumber": acc_numb,
                    "sourceRegNumber": 6969
                }

            tar_reg_numb = data['targetRegNumber']
            channel.basic_publish(exchange='', routing_key=f'{tar_reg_numb}-update', body=json.dumps(update))
        
        if method.routing_key == '6969-update':
            print('This is an update')
            if db.validate_account(data['accountNumber']):
                db.update_balance(data['accountNumber'], data['amount'], data['sourceAccountNumber'], data['sourceRegNumber'])
            else:
                # Add to a failed queue or something
                pass


    channel.basic_consume(queue='6969-transfer', on_message_callback=callback, auto_ack=True)
    channel.basic_consume(queue='6969-update', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
    
main()