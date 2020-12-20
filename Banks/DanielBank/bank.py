import sqlite3
import random
from datetime import datetime

def gen_account():
    a = {}
    a["public"] = ""
    a["private"] = "45710000"
    a["secret"] = ""
    
    for _ in range(10):
        a["public"] += str(random.randint(0, 9))
        
    for _ in range(8):
        a["private"] += str(random.randint(0, 9))
        
    for _ in range(3):
        a["secret"] += str(random.randint(0, 9))
    
    return a

def db_make_tables(conn):
    c = conn.cursor()
    c.execute("PRAGMA foreign_keys = ON;")
    
    c.execute("DROP TABLE IF EXISTS account;")
    c.execute("DROP TABLE IF EXISTS movement;")

    c.execute("""
        CREATE TABLE account(
        public text PRIMARY KEY,
        private text UNIQUE,
        secret text
    );""")

    c.execute("""
        CREATE TABLE movement(
        id integer PRIMARY KEY AUTOINCREMENT,
        plus text,
        regplus text,
        minus text,
        regminus text,
        amount integer,
        created_at timestamp DEFAULT CURRENT_TIMESTAMP NOT NULL
    );""")
    
    conn.commit()
    
def db_populate(conn):
    c = conn.cursor()
    
    a1 = {'public': '9774867114', 'private': '4571000070531467', 'secret': '775'}
    a2 = {'public': '8016618372', 'private': '4571000074376340', 'secret': '144'}
    a3 = {'public': '9895380531', 'private': '4571000061079602', 'secret': '837'}
    a4 = {'public': '0361653903', 'private': '4571000083893619', 'secret': '349'}
    a5 = {'public': '0926613919', 'private': '4571000088051266', 'secret': '960'}
    accs = [a1,a2,a3,a4,a5]
    
    for acc in accs:
        c.execute('INSERT INTO account VALUES (?, ?, ?);', (*acc.values(),))
        
    m1 = {'plus': '9774867114', 'regplus': '0000', 'minus': '8016618372', 'regminus': '0000', 'amount': 5000}
    m2 = {'plus': '9774867114', 'regplus': '0000', 'minus': '8016618372', 'regminus': '0000', 'amount': 9001}
    movs = [m1,m2]
    
    for mov in movs:
        c.execute('INSERT INTO movement VALUES (?,?,?,?,?,?,?);', (None, *mov.values(), datetime.now()))
    
    conn.commit()
    
def db_get_accounts(conn):
    c = conn.cursor()
    
    c.execute("SELECT * FROM account")
    data = c.fetchall()
    conn.commit()
    
    return data

def db_get_movements(conn):
    c = conn.cursor()
    

    c.execute("SELECT * FROM movement")
    data = c.fetchall()
    conn.commit()
    
    return data
    
def db_get_movements_plus_target(conn, public, reg):
    c = conn.cursor()
    
    c.execute("SELECT * FROM movement WHERE plus = ? AND regplus = ?", (public, reg))
    data = c.fetchall()
    conn.commit()
    
    return data
    
def db_get_movements_minus_target(conn, public, reg):
    c = conn.cursor()
    
    c.execute("SELECT * FROM movement WHERE minus = ? AND regminus = ?", (public, reg))
    data = c.fetchall()
    conn.commit()
    
    return data

def db_get_balance(conn, public, reg):
    pos = db_get_movements_plus_target(conn, public, reg)
    neg = db_get_movements_minus_target(conn, public, reg)
    
    pos = sum([int(x[5]) for x in pos])
    neg = sum([int(x[5]) for x in neg])
    
    return -50 + pos - neg


def db_make_movement(conn, amount, froom, to, froomReg="0000", toReg="0000"):
    
    c = conn.cursor()
    
    c.execute('INSERT INTO movement VALUES (?,?,?,?,?,?,?);', (None, to, toReg, froom, froomReg, amount,datetime.now()))
    
    conn.commit()
    
    return True

def db_validate_card(conn, cardNumber, cvc):
    c = conn.cursor()
    
    c.execute("SELECT public FROM account WHERE private = ? AND secret = ? LIMIT 1", (cardNumber, cvc))
    data = c.fetchone()
    conn.commit()
    
    if data is not None:
        data = data[0]
    
    return data