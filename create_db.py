
import sqlite3
import time
import datetime
import random
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import style
style.use('fivethirtyeight')
conn=sqlite3.connect('example.db')

c=conn.cursor()

#create table

# c.execute('''CREATE TABLE stocks
#             (date text,  trans text, symbol text,    qty real,   price real)''')

#insert row of data

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS stuffToPilot(unix REAL,date_stamp TEXT,keyword TEXT,value REAL)')

def data_entry():
    c.execute("INSERT INTO stuffToPilot VALUES(123456,'2016-01-01','Python',4)")
    conn.commit()
    c.close()
    conn.close()

def dynamic_data_entry():
    unix=time.time()
    date=str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%M-%D %h    -%m-%s'))
    keyword='Python'
    value=random.randrange(0,10)
    c.execute("INSERT INTO stuffToPilot(unix,date_stamp,keyword,value) VALUES(?,?,?,?)",(unix,date,keyword,value))
    conn.commit()

def read_from_db():
    #c.execute("SELECT * FROM stuffToPilot WHERE value=6 and keyword='Python'")
    c.execute('SELECT * FROM stuffToPilot')
    #c.execute('SELECT keyword, unix, value, date_stamp FROM stuffToPilot WHERE unix>1485151690')
    data=c.fetchall()
    for row in data:
        print(row[0],row[1])

def graph_data():
    c.execute('SELECT unix, value FROM stuffToPilot WHERE unix>1485151685')
    dates = []
    values = []
    for row in c.fetchall():
        dates.append(datetime.datetime.fromtimestamp(row[0]))
        values.append(row[1])

    plt.plot_date(dates, values, '-')
    plt.show()

def del_and_update():
    c.execute('SELECT * FROM stuffToPilot')
    [print(row) for row in c.fetchall()]
    # c.execute('UPDATE stuffToPilot SET value = 99 WHERE value = 8 ')
    # conn.commit()
    # c.execute('SELECT * FROM stuffToPilot')
    # [print(row) for row in c.fetchall()]
    c.execute('DELETE FROM stuffToPilot WHERE value = 99')
    conn.commit()
    c.execute('SELECT * FROM stuffToPilot')
    [print(row) for row in c.fetchall()]

graph_data()
#create_table()
#data_entry()

#for i in range(10):
#    dynamic_data_entry()
#    time.sleep(1)
#    print('writing')
#read_from_db()
# del_and_update()
# c.close()
# conn.close()