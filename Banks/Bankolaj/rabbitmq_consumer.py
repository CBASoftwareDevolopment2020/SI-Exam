import pika
import json
import ast
from bank import Bankolaj
from secrets import cloudamqp_host, cloudamqp_user, cloudamqp_password


def main():
    url = f'amqps://{cloudamqp_user}:{cloudamqp_password}@{cloudamqp_host}/{cloudamqp_user}'
    params = pika.URLParameters(url)
    connection = pika.BlockingConnection(params)
    channel = connection.channel()
    bank = Bankolaj()

    def callback(ch, method, properties, body):
        d = ast.literal_eval(body.decode("UTF-8"))
        if method.routing_key == '1234-transfer':
            print('Transfer queue')
            amt, card_num, cvc, trg_acc_num, trg_reg_num = d['amount'], d['originCardNumber'], d['originCVC'], d[
                'targetAccountNumber'], d['targetAccountNumber']
            acc_num = bank.validate_card(card_num, cvc)
            if acc_num:
                bank.update_balance(acc_num, amt, trg_acc_num, trg_reg_num)

                upd = {
                    "accountNumber": trg_acc_num,
                    "amount": amt,
                    "sourceAccountNumber": acc_num,
                    "sourceRegNumber": bank.bank_num
                }
                channel.basic_publish(exchange='', routing_key=f'{trg_reg_num}-update', body=json.dumps(upd))

        if method.routing_key == '1234-update':
            print('Update queue')
            acc_num, amt, src_acc_num, src_reg_num = d['accountNumber'], d['amount'], d['sourceAccountNumber'], d[
                'sourceRegNumber']
            if bank.validate_account(bank.bank_num, acc_num):
                bank.update_balance(acc_num, amt, src_acc_num, src_reg_num)
            else:
                # DO SOMETHING IF ACCOUNT DOESN'T EXIST
                pass

    # channel.basic_consume(queue='testq', on_message_callback=callback, auto_ack=True)
    channel.basic_consume(queue='1234-transfer', on_message_callback=callback, auto_ack=True)
    channel.basic_consume(queue='1234-update', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    main()
