
from PyQt5 import QtCore, QtGui, QtWidgets
from report import Ui_Form as dataForm
import sys
from d_base_mdl import d_base
import random

class DataGui(QtWidgets.QWidget,dataForm):
    def __init__(self):
        super(DataGui, self).__init__()
        self.setupUi(self)
        self.timer_1 = QtCore.QTimer()
        self.timer_1.setInterval(1000)
        self.meter_count = 0
        self.start_stop = 0.0


        self.timer_1.timeout.connect(self.random_deger_uret)
        self.pushButton_start_time.clicked.connect(self.start_timer)
        self.pushButton_stop_time.clicked.connect(self.stop_timer)
        self.pushButton_show.clicked.connect(self.show_data)
        self.creat_vt()
    def show_data(self):
        print("show_clicked")
        a = self.vt.view_data('speed_act_table')
        for row in a:
            print(row)
        #print(a)
    def start_timer(self):
        self.timer_1.start()

    def stop_timer(self):
        self.timer_1.stop()

    def creat_vt(self):
        self.vt = d_base()
        self.vt.create_table_rec_data('oven_1_act_table', "act_temp")
        self.vt.create_table_rec_data('oven_2_act_table', "act_temp")
        self.vt.create_table_rec_data('speed_act_table', "act_speed")
        self.vt.create_table_rec_data('counter_act_table', 'act_counter')
        self.vt.create_table_rec_data('oven_1_set_table', "set_temp")
        self.vt.create_table_rec_data('oven_2_set_table', "set_temp")
        self.vt.create_table_rec_data('speed_set_table', "set_speed")
        self.vt.create_table_rec_data('counter_set_table', 'set_counter')
        self.vt.create_table_rec_data('makina_run_time_table', 'start_stop')
        self.vt.create_table_rec_data('makina_error_table', 'error')
        self.vt.create_table_prg('program_table')

    def random_deger_uret(self):
        act_tepm_ov_1 = random.randrange(145.0,155.0)
        act_tepm_ov_2 = random.randrange(145.0, 155.0)
        act_speed = random.randrange(33, 36)
        self.meter_count = self.meter_count + 10
        act_counter = self.meter_count
        if self.meter_count>=1500:
            self.meter_count = 0
        set_temp_ov_1 = 150
        set_temp_ov_2 = 145
        set_speed = 35
        set_counter = 1500
        self.start_stop = self.start_stop + 1.0
        if self.start_stop<1000:
            start_stop = 1.0
        elif self.start_stop>= 1000 and self.start_stop<1200:
            start_stop =0.0
        elif self.start_stop>=1200:
            start_stop = 1.0
            self.start_stop = 0.0
        error = random.randrange(15,25)
        print(start_stop)
        print(self.meter_count)
        print(act_tepm_ov_1,act_tepm_ov_2)
        self.vt.insert_table_prg('program_table', 'alaca_desen')
        self.vt.insert_data('oven_1_act_table', 'act_temp', act_tepm_ov_1)
        self.vt.insert_data('oven_2_act_table', 'act_temp', act_tepm_ov_2)
        self.vt.insert_data('speed_act_table', 'act_speed', act_speed)
        self.vt.insert_data('oven_1_set_table', 'set_temp', set_temp_ov_1)
        self.vt.insert_data('oven_2_set_table', 'set_temp', set_temp_ov_2)
        self.vt.insert_data('speed_set_table', 'set_speed', set_speed)
        self.vt.insert_data('counter_set_table', 'set_counter', set_counter)
        self.vt.insert_data('makina_run_time_table', 'start_stop', start_stop)
        self.vt.insert_data('makina_error_table', 'error', error)

    def closeEvent(self, QCloseEvent):
        print("kapatıldı")
        self.vt.close_db()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # hata yakalama için ilave edildi
    sys._excepthook = sys.excepthook


    def my_exception_hook(exctype, value, traceback):
        # Print the error and traceback
        print("program hatalar", exctype, value, traceback)
        # Call the normal Exception hook after
        sys._excepthook(exctype, value, traceback)
        sys.exit(1)


    # Set the exception hook to our wrapping function
    sys.excepthook = my_exception_hook

    form = DataGui()
    form.show()
    sys.exit(app.exec_())





