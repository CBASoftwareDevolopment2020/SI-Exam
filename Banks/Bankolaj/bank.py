from data_manager import DataManager
from random import choice, randint
import secrets


class Bankolaj:
    def __init__(self):
        self.bank_num = '1234'
        self.dm = DataManager('db/bankolaj.db')
        self.next_card_num = randint(0, 99999999)
        self.next_acc_num = randint(0, 9999999999)
        # self.next_card_num = 1
        # self.next_acc_num = 1

    def create_account(self, owner: str):
        card_type = {'5019': 'Dankort', '4571': 'Visa/Dankort', '5413': 'Mastercard'}
        # card_type = {'5019': 'Dankort'}
        cvc = f'000{str(randint(0, 999))}'[-3:]
        # cvc = '420'
        acc_num, self.next_acc_num = f'0000000000{self.next_acc_num}'[-10:], self.next_acc_num + randint(1, 100)
        card_num, self.next_card_num = choice(list(card_type.keys())) + \
                                       self.bank_num + \
                                       f'0000000{self.next_card_num}'[-8:], self.next_card_num + randint(1, 100)
        self.dm.new_account(owner, acc_num, card_num, cvc)

    def update_balance(self, acc_num: str, amt: int, other_acc_num: str, other_reg_num: str) -> bool:
        return self.dm.update_balance(acc_num, amt, other_acc_num, other_reg_num)

    def validate_card(self, card_num: str, cvc: str) -> str:
        return self.dm.validate_card(card_num, cvc)

    def validate_account(self, reg_num: str, acc_num: str) -> bool:
        if reg_num == self.bank_num:
            return self.dm.validate_account(acc_num)
        return False


if __name__ == '__main__':
    fnames = set()
    lnames = set()
    for name in secrets.names:
        fname, *mnames, lname = name.split(' ')
        fnames.add(fname)
        lnames.add(lname)
    fnames = sorted(list(fnames))
    lnames = sorted(list(lnames))

    customers = list(set([f'{choice(fnames)} {choice(lnames)}' for _ in range(100)]))
    bank = Bankolaj()
    bank.dm.setup_tables()
    for customer in customers:
        for _ in range(randint(1, 3)):
            bank.create_account(customer)
    bank.dm.print_data()
