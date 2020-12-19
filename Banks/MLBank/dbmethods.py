from pymongo import MongoClient

client = MongoClient('mongodb+srv://Admin:Passw0rd@gonnerscluster.g61w7.mongodb.net/bank?retryWrites=true&w=majority')
db = client.bank.creditcards

def update_balance(acc_numb, amount, src_acc_numb, src_reg_numb):
    curr_amount = db.find_one(
        {'AccountNumber': acc_numb}
    )

    result = db.update_one(
        { 'AccountNumber': acc_numb },
        { '$set': { 'Balance': curr_amount['Balance'] + amount }}
    )

    if result.modified_count > 0:
        return True
    else:
        return False

def validate_card(card_numb, cvc):
    result = db.find_one(
        {'CardNumber': card_numb, 'cvc': cvc}
    )
    
    if result != None:
        print(f'Card: {card_numb} exists in the database')
        return result['AccountNumber']
    else:
        print(f'Card: {card_numb} dose not exists in the database')
        return None

def validate_account(acc_numb):
    result = db.find_one(
        {'AccountNumber': acc_numb}
    )
    
    if result != None:
        print(f'Card: {acc_numb} exists in the database')
        return True
    else:
        print(f'Card: {acc_numb} dose not exists in the database')
        return False

def test(name):
    return {
        "name": name,
        "somethingElse": "some more"
    }








#update_balance('2566923343', 8000)
#validate_card('5413696975959404', '338')
#validate_account('6829168614')
