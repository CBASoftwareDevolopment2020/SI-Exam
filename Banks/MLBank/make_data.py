from pymongo import MongoClient
from random import randint, choice


client = MongoClient('mongodb+srv://Admin:Passw0rd@gonnerscluster.g61w7.mongodb.net/bank?retryWrites=true&w=majority')
db = client.bank

bank_num = '6969'
card_type = {'5019': 'Dankort', '4571': 'Visa/Dankort', '5413': 'Mastercard'}
f_names = ['Michael', 'Jacob', 'Nikolaj', 'Daniel', 'Morten', 'Emil', 'Sandra', 'Louise', 'Donna']
l_names = ['Jackson', 'Lundsgaard', 'Lindholm', 'Borg', 'Nielsen', 'Martinez', 'Jensen', 'Pedersen']
cards = 5

for x in range (1,cards+1):
    try:
        creditcards = {
            'Name': f'{choice(f_names)} {choice(l_names)}',
            'CardNumber': choice(list(card_type.keys())) + bank_num + str(randint(0, 99999999)),
            'AccountNumber': str(randint((10**(10-1)),((10**10)-1))),
            'cvc': str(randint((10**(3-1)),((10**3)-1))),
            'Balance': 0
        }
        
        db.creditcards.create_index(('CardNumber'), unique=True)
        db.creditcards.create_index(('AccountNumber'), unique=True)

        result = db.creditcards.insert_one(creditcards)
        print(f'Created {x} of {cards} as {result.inserted_id}')

    except:
        print(f'Something went wrong!')

print(f'finished creating {cards} credit cards')
