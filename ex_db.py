

import sqlite3
import time
import datetime

conn=sqlite3.connect('vpdata.db')

c=conn.cursor()


def create_date_table():
    try:
        c.execute('CREATE TABLE IF NOT EXISTS date_table(date_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,date_stamp TEXT NOT NULL)')
    except sqlite3.OperationalError:
        print("err in table create")
def date_table_upd():
    tarih=datetime.date.today()
    c.execute('INSERT INTO date_table(date_id,date_stamp) VALUES(?,?)',(0,tarih))
    conn.commit()
def read_from_db():
    c.execute('SELECT * FROM date_table')
    data=c.fetchall()
    for row in data:
        print(row)

create_date_table()
date_table_upd()
read_from_db()
c.close()
conn.close()

print(datetime.date.today())