from pymongo import MongoClient

client = MongoClient('mongodb+srv://Admin:Passw0rd@gonnerscluster.g61w7.mongodb.net/bank?retryWrites=true&w=majority')
db = client.bank.creditcards

def update_balance(account_number, amount):
    db.update_one(
        { 'AccountNumber': account_number },
        { '$set': { 'Balance': amount }}
    )

def validate_card(card_number, cvc):
    result = db.find_one(
        {'CardNumber': card_number, 'cvc': cvc}
    )
    
    if result != None:
        print(f'Card: {card_number} exists in the database')
    else:
        print(f'Card: {card_number} dose not exists in the database')

def validate_account(account_number):
    result = db.find_one(
        {'AccountNumber': account_number}
    )
    
    if result != None:
        print(f'Card: {account_number} exists in the database')
    else:
        print(f'Card: {account_number} dose not exists in the database')


#update_balance('2566923343', 1000)
#validate_card('5413696975959404', '338')
validate_account('6829168614')
