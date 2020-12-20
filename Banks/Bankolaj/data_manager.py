import sqlite3
from sqlite3 import Error, Connection
from pprint import pprint as pp


def create_connection(db_file: str) -> Connection:
    """ create a database connection to the SQLite database specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn


class DataManager:
    def update_balance(self, acc_num: str, amt: int, other_acc_num: str, other_reg_num: str) -> bool:
        cur = self._conn.cursor()
        try:
            cur.execute("SELECT * FROM accounts WHERE accNum = ?", (acc_num,))
            acc_id, _, balance, owner = cur.fetchone()
            cur.execute("UPDATE accounts SET balance = ? WHERE id = ?", (balance + amt, acc_id))
            if cur.rowcount < 1:
                return False
            else:
                return True
        except Error as e:
            print(e)

    def validate_card(self, card_num: str, cvc: str) -> str:
        cur = self._conn.cursor()
        try:
            cur.execute("SELECT accounts.accNum FROM cards WHERE cardNum = ? AND cvc = ?", (card_num, cvc))
            res = cur.fetchone()
            if res:
                return True
            return False
        except Error as e:
            print(e)

    def validate_account(self, acc_num: str) -> bool:
        cur = self._conn.cursor()
        try:
            cur.execute("SELECT * FROM accounts WHERE accNum = ?", (acc_num,))
            res = cur.fetchone()
            if res:
                return True
            return False
        except Error as e:
            print(e)

    def __init__(self, db_file: str):
        self._conn: Connection = None
        self.get_connection(db_file)
        self.setup_tables()

    def get_connection(self, db_file: str) -> Connection:
        if self._conn is None:
            print('No connection set\nCreating connection')
            self._conn = create_connection(db_file)
        return self._conn

    def new_account(self, owner, acc_num, card_num, cvc):
        cur = self._conn.cursor()
        cur.execute('BEGIN')
        try:
            cur.execute(f"INSERT INTO accounts (accNum,owner) VALUES ('{acc_num}','{owner}');")
            cur.execute(f"INSERT INTO cards (cardNum,cvc,accId) VALUES ('{card_num}','{cvc}','{cur.lastrowid}');")
        except Error as e:
            print(e)
            cur.execute('ROLLBACK')
        finally:
            cur.execute('END')

    def setup_tables(self):
        drop_tables = '''   DROP TABLE IF EXISTS cards;
                            DROP TABLE IF EXISTS accounts;
                            DROP TABLE IF EXISTS transfers'''
        account_table = ''' CREATE TABLE accounts(
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                accNum NCHAR(10) UNIQUE NOT NULL ,
                                balance INTEGER NOT NULL DEFAULT 0,
                                owner NVARCHAR(64) NOT NULL
                            )'''
        card_table = '''CREATE TABLE cards(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            cardNum NCHAR(16) UNIQUE NOT NULL,
                            cvc NCHAR(3) NOT NULL,
                            accId INTEGER NOT NULL,
                            FOREIGN KEY (accId) REFERENCES accounts (id)
                        )'''
        transfer_table = '''CREATE TABLE transfers(
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                srcRegNum NCHAR(4) NOT NULL,
                                srcAccNum NCHAR(10) NOT NULL,
                                trgRegNum NCHAR(4) NOT NULL,
                                trgAccNum NCHAR(10) NOT NULL,
                                amount INTEGER NOT NULL
                            )'''
        try:
            print('Creating tables')
            self._conn.executescript(';\n'.join([drop_tables, account_table, card_table, transfer_table]))
            print('Tables created')
        except Error as e:
            print(e)
        print('Populating tables')
        self.populate_tables()
        print('Tables populated')

    def populate_tables(self):
        data = [('Nikolai Rusbjerg', '6331238411', '5019123400915835', '982', 0),
                ('Nikolai Rusbjerg', '6331238494', '5413123400915857', '769', 0),
                ('Jesper Saidane', '6331238566', '4571123400916022', '115', 0),
                ('Emil Lundsgaard-Larsen', '6331240853', '5019123400918138', '390', 0),
                ('Emil Lundsgaard-Larsen', '6331240870', '5019123400918176', '384', 0),
                ('Emil Lundsgaard-Larsen', '6331240947', '4571123400918272', '123', 0),
                ('Jacob Rusbjerg', '6331242246', '4571123400919564', '036', 0),
                ('Jesper Borg', '6331242378', '5019123400919704', '334', 0),
                ('Jesper Borg', '6331242393', '5413123400919797', '120', 0),
                ('Jesper Borg', '6331242460', '5413123400919861', '370', 0),
                ('Adam Djurhuus', '6331243091', '5413123400920454', '130', 0),
                ('Adam Djurhuus', '6331243094', '5019123400920537', '365', 0),
                ('Adam Djurhuus', '6331243098', '5413123400920603', '826', 0),
                ('Adam Saidane', '6331244869', '5413123400922528', '075', 0),
                ('Adam Saidane', '6331244893', '5019123400922617', '882', 0)]

        for item in data:
            owner, acc_num, card_num, cvc, _ = item
            self.new_account(owner, acc_num, card_num, cvc)

    def print_tables(self):
        cursor = self._conn.cursor()
        try:
            cursor.execute("SELECT * FROM sqlite_master WHERE type='table';")
        except Error as e:
            print(e)
        pp(cursor.fetchall())

    def print_data(self):
        cursor = self._conn.cursor()
        try:
            cursor.execute("""  SELECT accounts.owner,accounts.accNum,cards.cardNum,cards.cvc,accounts.balance
                                FROM cards
                                JOIN accounts
                                    WHERE cards.accId = accounts.id""")
        except Error as e:
            print(e)
        pp(cursor.fetchall())


if __name__ == '__main__':
    dm = DataManager(r"db\bankolaj.db")
