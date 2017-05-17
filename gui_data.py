
from PyQt5 import QtCore, QtGui, QtWidgets
from report import Ui_Form as dataForm
import sys


class DataGui(QtWidgets.QWidget,dataForm):
    def __init__(self):
        super(DataGui, self).__init__()
        self.setupUi(self)






if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    form = DataGui()
    form.show()
    sys.exit(app.exec_())





