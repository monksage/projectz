import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from main_table import *
from preferences import *
import defs_n_classes as defs
import os


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    global ui
    global MainWindow
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.mt_funcs()
    MainWindow.show()
    
    # os.remove("prefs_of_Columns.npy")
    # os.remove("prefs_of_each.npy")
    sys.exit(app.exec_())
        
    