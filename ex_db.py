

import sqlite3
import time
import datetime

conn=sqlite3.connect('vpdata.db')

c=conn.cursor()


def create_date_table():
    try:
        c.execute('CREATE TABLE IF NOT EXISTS datetable(date_id INTEGER PRIMARY KEY AUTOINCREMENT,date_stamp TEXT NOT NULL)')
    except sqlite3.OperationalError:
        print("err in table create")

def create_time_table():
    try:
        c.execute('CREATE TABLE IF NOT EXISTS timetable(date_id INTEGER PRIMARY KEY AUTOINCREMENT,time_stamp TEXT NOT NULL)')
    except sqlite3.OperationalError:
        print("err in table create")
def date_table_upd():
    tarih=datetime.date.today()
    c.execute('INSERT INTO datetable(date_stamp) VALUES(?)',(tarih,))
    conn.commit()

def time_table_upd():
    now = datetime.datetime.now()
    tarih = datetime.date.today()
    saat = datetime.time(now.hour, now.minute, now.second) #datetime.datetime.now().time() #
    c.execute("INSERT INTO timetable(time_stamp) VALUES(TIME('now'))")
    conn.commit()


def read_from_db():
    c.execute('SELECT * FROM datetable')
    data=c.fetchall()
    for row in data:
        print(row)
def read_from_time_db():
    c.execute('SELECT * FROM timetable')
    data=c.fetchall()
    for row in data:
        print(row)
def drop_table():
    c.execute('drop table datetable')

#create_date_table()
#date_table_upd()
create_time_table()
time_table_upd()
# drop_table()
read_from_time_db()
c.close()
conn.close()

print(datetime.date.today())