import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from main import *
from defs_n_classes import *
from preferences import Ui_Set_Preferenses_Window
import os
from scipy.stats import chi2_contingency

class Ui_MainWindow(object):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_Stats = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Stats.setObjectName("btn_Stats")
        self.gridLayout.addWidget(self.btn_Stats, 1, 0, 1, 1)
        self.btn_SetPr = QtWidgets.QPushButton(self.centralwidget)
        self.btn_SetPr.setObjectName("btn_SetPr")
        self.gridLayout.addWidget(self.btn_SetPr, 1, 1, 1, 1)
        self.main_table = QtWidgets.QTableWidget(self.centralwidget)
        self.main_table.setObjectName("main_table")
        self.main_table.setColumnCount(0)
        self.main_table.setRowCount(0)
        self.gridLayout.addWidget(self.main_table, 2, 0, 1, 2)
        self.stats_text = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.stats_text.setMaximumSize(QtCore.QSize(16777215, 146))
        self.stats_text.setObjectName("stats_text")
        self.stats_text.setPlainText("Welcome! Please set preferences.\n\nFirst initialisation would take a little time.")
        self.gridLayout.addWidget(self.stats_text, 0, 0, 1, 2)
        self.text_about_chi2 = "This is chi2 contigency test. Dimensions: wild, domestic. Frequences: '+' and '-'. \n\n"
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        self.make_view()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TATA Z-Tester Database"))
        self.btn_Stats.setText(_translate("MainWindow", "Refresh"))
        self.btn_SetPr.setText(_translate("MainWindow", "Set Preferences"))
    
    def mt_funcs(self):
        self.btn_SetPr.clicked.connect(self.show_wait)
        self.btn_SetPr.clicked.connect(openOtherWindow)
        self.btn_Stats.clicked.connect(lambda: self.make_table())
        self.btn_Stats.clicked.connect(lambda: self.show_stats())
        
    def make_table(self):
        self.chosen_columns = np.load("chosen_columns.npy", allow_pickle=True)
        self.chosen_prefs = np.load("chosen_prefs.npy", allow_pickle=True)
        # try to pref the homology and pvalue
        self.chebs = ["Animal_DEG", "Tissue", "overexpression_sign", "human_feature", "underexpression_sign", "Animal", "Human_gene_homolog", "Homology"]
        table_query = self.make_table_query(self.chosen_columns, self.chosen_prefs, self.chebs)
        # self.create_view_query = "create or replace view refresh_table_view as " + table_query
        # print(self.create_view_query)
        self.clear_table()
        self.reopen(table_query)

    def clear_table(self):
        while (self.main_table.rowCount() > 0):
            self.main_table.removeRow(0)

    def make_table_query(self, chosen_cols, chosen_prefs, chebs):
        self.kill_null()
        self.added_funcs()
        try:
            pv = self.pvs
        except:
            pv = []
        try:
            padj = self.padjs
        except:
            padj = []
        try:
            homology = self.homology
        except:
            homology = []
        select = ConnectInit.select_clause(chosen_cols)
        where = ConnectInit.where_clause(chosen_prefs, chebs, homology=homology, pvalue=pv, padj=padj)
        query = select + " from make_view " + where
        ConnectInit.ret_query(f"create or replace view stats_view as {query}")
        # create -> select view(stats didnt counted)
        return query
    
    def make_view(self):
        ConnectInit.ret_query("create or replace view make_view as select dataapp.domanimals.*,\
                                if(Animal_DEG = Human_gene_homolog, 'ortholog', 'paralog') as Homology from dataapp.domanimals")
    
    def kill_null(self):
        all_cols = take_distinct(ConnectInit.query_for_cols())
        for i in all_cols:
            query = f"update make_view \
                    set {i} = 'None'\
                    where {i} is null"
            # print(query)
            ConnectInit.ret_query(query)

    def added_funcs(self):
        try:
            self.pvs = np.load("p_value.npy")
        except:
            pass
        try:
            self.padjs = np.load("padj_value.npy")
        except:
            pass
        try:
            self.homology = np.load("chosen_homology.npy")
        except:
            pass

    

    def show_wait(self):
        self.stats_text.setPlainText("downloading...")

    def show_stats(self):
        # ConnectInit.ret_query(self.create_view_query)
        self.mass_for_stats = []
        self.mass_for_stats = make_stats(self.mass_for_stats)
        self.chi2_thing()
        pass
    
    def chi2_thing(self):
        local_mass = []
        local_mass.append([0]*2)
        local_mass.append([0]*2)
        local_mass[0][0] += self.mass_for_stats[0] + self.mass_for_stats[1]
        local_mass[0][1] += self.mass_for_stats[2] + self.mass_for_stats[3]
        local_mass[1][0] += self.mass_for_stats[4] + self.mass_for_stats[5]
        local_mass[1][1] += self.mass_for_stats[6] + self.mass_for_stats[7]
        print(local_mass)
        _n = "\n"
        try:
            local_string = chi2_contingency(local_mass)[0:2]
            chi2 = local_string[0]
            p_val = local_string[1]
            self.stats_text.setPlainText(f"{self.text_about_chi2}chi2: {chi2}, p-value: {p_val}{_n}{_n}\
                                            Domestic: '+' {local_mass[0][0]}; '-' {local_mass[0][1]}{_n}\
                                            Wild:         '+' {local_mass[1][0]}; '-' {local_mass[1][1]}")
        except:
            
            self.stats_text.setPlainText(f"{self.text_about_chi2}Invalid data for chi2 test:{_n}{_n}\
                                            Domestic: '+' {local_mass[0][0]}; '-' {local_mass[0][1]}{_n}\
                                            Wild:         '+' {local_mass[1][0]}; '-' {local_mass[1][1]}")
              
        
    def delete_marks(self, a):
        marks = "[](),"
        for x in a:
            if x in marks:
                a = a.replace(x, "")
        return a
    
    def tryer(self):
        try:
            self.reopen("spdofpfne")
        except:
            print("Invalid query")


    def reopen(self, query):
        self.main_table.setColumnCount(len(self.chosen_columns))
        self.main_table.setHorizontalHeaderLabels(self.chosen_columns)
        # print(self.take_distinct(ConnectInit.query_for_chebox(self.Tissue_cb))) Засунуть уникальные значения в Чебокс
        for row_number, row_data in enumerate(ConnectInit.ret_query(query)):
            self.main_table.setRowHeight(row_number, 100)
            self.main_table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.main_table.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        
            
            



