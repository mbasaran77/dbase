import sqlite3
import datetime
class d_base():
    def __init__(self):
        self.conn = sqlite3.connect('vpdata.db')
        self.c = self.conn.cursor()
        self.c.execute('pragma foreign_keys=ON')


    def create_table_rec_data(self,table_name,data_column_name):

        try:
            self.c.execute('CREATE TABLE IF NOT EXISTS {tn}(sicaklik_id INTEGER PRIMARY KEY AUTOINCREMENT, batch_id INTEGER,'
                           'prg_id INTEGER, date_stamp STRING, time_stamp STRING, {dn} REAL)'.format(tn=table_name,dn=data_column_name))
            print("db created")
        except sqlite3.OperationalError:
            print("err in table create")

    def create_table_prg(self,table_name):
        try:
            self.c.execute('CREATE TABLE IF NOT EXISTS {tn}(id INTEGER PRIMARY KEY AUTOINCREMENT, prg_name STRING)'.format(tn=table_name))
            print("prg table created")
        except sqlite3.OperationalError:
            print("err in prg table create")
    def delete_table(self,table_name):
        try:
            self.c.execute('DROP TABLE  {tn}'.format(tn=table_name))
            self.conn.commit()
            print("db deleted")
        except sqlite3.OperationalError:
            print("err in table delete")
    def insert_data(self,table_name,data_column_name,data_insert):
        an = datetime.datetime.now()
        tarih = datetime.datetime.strftime(an, '%x')
        saat = datetime.datetime.strftime(an, '%X')
        rec_bact_id = 112
        rec_prg_id = 123
        rec_date = tarih
        rec_time = saat
        rec_data = data_insert
        data_t =(rec_bact_id,rec_prg_id,rec_date,rec_time,rec_data)
        self.c.execute('INSERT INTO {tn}(batch_id,prg_id,date_stamp,time_stamp,{dn}) VALUES (?,?,?,?,?)'.format(tn=table_name,dn=data_column_name),data_t)
        self.conn.commit()
        print("data inserted")

    def view_data(self,table_name):
        self.c.execute("SELECT * FROM {tn}".format(tn=table_name))
        # cur.execute("SELECT * FROM yazar_ad")
        rows = self.c.fetchall()
        return rows


    def close_db(self):
        self.conn.close()

vt = d_base()

vt.create_table_rec_data('sicaklik_table',"isi")
# vt.delete_table('sicaklik_table')
vt.create_table_prg('program_table')
vt.insert_data('sicaklik_table','isi',5.5)

a = vt.view_data('sicaklik_table')
print(a)


vt.close_db()



