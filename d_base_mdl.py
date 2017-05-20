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
                           'prg_id INTEGER, date_stamp STRING, time_stamp STRING, {dn} REAL, FOREIGN KEY (prg_id) REFERENCES program_table(id))'.format(tn=table_name,dn=data_column_name))
            print("db created")
        except sqlite3.OperationalError:
            print("err in table create")

    def create_table_prg(self,table_name):
        try:
            self.c.execute('CREATE TABLE IF NOT EXISTS {tn}(id INTEGER PRIMARY KEY AUTOINCREMENT, prg_name STRING NOT NULL UNIQUE)'.format(tn=table_name))
            print("prg table created")
        except sqlite3.OperationalError:
            print("err in prg table create")
    def insert_table_prg(self,table_name,prg_name):
        data_t = (prg_name,)
        try:
            self.c.execute('INSERT INTO {tn}(prg_name) VALUES (?)'.format(tn=table_name),data_t)
            self.conn.commit()
            print("data inserted")

        except sqlite3.Error as e:
            print("err in prg table insert",e.args[0])

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
        rec_bact_id = 115
        rec_prg_id = 2 # burada çalışan program_sorgulanıp id nin alınması gerek şimdilik el ile yazıldı
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

# vt = d_base()
#
# vt.create_table_rec_data('oven_1_act',"act_temp")
# vt.create_table_rec_data('oven_2_act',"act_temp")
# vt.create_table_rec_data('speed_act',"act_speed")
# vt.create_table_rec_data('counter_act','act_counter')
# vt.create_table_rec_data('oven_1_set',"set_temp")
# vt.create_table_rec_data('oven_2_set',"set_temp")
# vt.create_table_rec_data('speed_set',"set_speed")
# vt.create_table_rec_data('counter_set','set_counter')
#
#
# vt.delete_table('program_table')
# vt.delete_table('sicaklik_table')
#
# vt.create_table_prg('program_table')
# vt.insert_data('sicaklik_table','isi',5.5)
#
# vt.insert_table_prg('program_table','alaca_desen')
# a = vt.view_data('sicaklik_table')
# print(a)
# a = vt.view_data('program_table')
# print(a)
#
# vt.close_db()



