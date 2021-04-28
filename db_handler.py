import sqlite3
import hashlib
from werkzeug.security import generate_password_hash, check_password_hash

def login(login, password, signal):
    try:
        con = sqlite3.connect('data/my_market_db')
        cur = con.cursor()
        cur.execute(f'SELECT * from users where username ="{login}";')
        value = cur.fetchall()

        if value != [] and check_password_hash(value[0][1], password):
            if value[0][2] == 'admin':
                signal.emit('1')
            else:
                signal.emit('-1')
        else:
            signal.emit('2')

        cur.close()
        con.close()
    except:
        signal.emit('0')


def register(login, password, signal):
    try:
        con = sqlite3.connect('data/my_market_db')
        cur = con.cursor()


        cur.execute(f'SELECT * from users where username ="{login}";')
        value = cur.fetchall()


        if value != []:
            signal.emit('3')
        elif value == []:
            hashed_password = generate_password_hash(password)
            cur.execute(f"INSERT INTO users (username, password, role) VALUES ('{login}','{hashed_password}','{'user'}')")
            signal.emit('4')
            con.commit()

        cur.close()
        con.close()
    except:
        signal.emit('0')

