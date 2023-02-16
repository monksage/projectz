import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import preferences
import main_table
from main import *
import mysql.connector as mc
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QVBoxLayout
import mysql.connector as mc
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtCore import Qt, QStringListModel
import numpy as np
import os




def what_items(self, k):
    check_list = []
    for i in range(k.count()):
        if k.itemChecked(i):
            check_list.append(k.itemText(i))
    check_list = list(filter(None, check_list))
    return check_list





def take_distinct(row):
    copy = []
    for i in row:
        if i is None:
            copy.append("No")
        else:
            copy.append(str(i[0]))
    return copy

def delete_marks(a):
        marks = "[](),"
        for x in a:
            if x in marks:
                a = a.replace(x, "")
        return a

def make_stats(mass):
        domestic_plus = 0
        domestic_minus = 0
        wild_plus = 0
        wild_minus = 0
        sign = ["underexpression_sign", "overexpression_sign"]
        undorov = ["Underexpression_versus_most_recent_common_ancestor", "Overexpression_versus_most_recent_common_ancestor"]
        dom_or_wild = ["'domestic'", "'wild'"]
        plusmin = ["'+'", "'-'"]
        view_name = "stats_view"
        for i in range(2):
            for j in range(2):
                for l in range(2):
                    query = f"select count({sign[l]}) from {view_name} where\
                            {sign[l]} = {plusmin[j]} and {undorov[l]} = {dom_or_wild[i]}"
                    # print("result: ",ConnectInit.ret_query(query), sign[l], plusmin[j], undorov[l], dom_or_wild[i])
                    mass.append(int(delete_marks(str(ConnectInit.ret_query(query)))))
                    # first domestic, uu+, oo+, uu-, oo-; second wild, uu+, oo+, uu-, oo-
        return mass
         


# def reopen(self, query):
#     ui.main_table.setColumnCount(len(self.what_items(self.Columns_cb)))
#     ui.main_table.setHorizontalHeaderLabels(self.what_items(self.Columns_cb))
#     # print(self.take_distinct(ConnectInit.query_for_chebox(self.Tissue_cb))) Засунуть уникальные значения в Чебокс

#     for row_number, row_data in enumerate(ConnectInit.ret_query(query)):
#         ui.main_table.setRowHeight(row_number, 100)
#         ui.main_table.insertRow(row_number)
#         for column_number, data in enumerate(row_data):
#             if data is None:
#                 ui.main_table.setItem(row_number, column_number, QTableWidgetItem(str(0)))
#             else:
#                 ui.main_table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
       

def openOtherWindow():
    global Set_Preferenses_Window
    global pref_ui
    Set_Preferenses_Window = QtWidgets.QDialog()
    pref_ui = preferences.Ui_Set_Preferenses_Window()
    pref_ui.setupUi(Set_Preferenses_Window)
    pref_ui.pref_funcs(Set_Preferenses_Window)
    # print(Set_Preferenses_Window.isVisible())
    Set_Preferenses_Window.show()
    try:
        os.remove("p_value.npy")
    except:
        pass
    try:
        os.remove("padj_value.npy")
    except:
        pass

    




class CheckableComboBox(QtWidgets.QComboBox):
    def addItem(self, item):
        super(CheckableComboBox, self).addItem(item)
        item = self.model().item(self.count()-1,0)
        item.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        item.setCheckState(QtCore.Qt.Checked)
    
    def item_pressed(self):
        super(CheckableComboBox, self).view().pressed.connect()
    
    def handle_item_pressed(self, index):
        item = self.model().itemFromIndex(index)
        

    def itemChecked(self, index):
        item = self.model().item(index,0)
        return item.checkState() == QtCore.Qt.Checked
    
    def itemUnselected(self, index):
        item = self.model().item(index,0)
        return item.setCheckState(QtCore.Qt.Unchecked)
    
    def itemSelected(self, index):
        item = self.model().item(index,0)
        return item.setCheckState(QtCore.Qt.Checked)

    
        



class ConnectInit():
    def ret_query (query):
        mydb = mc.connect(
            host="localhost",
            user="root",
            password="t171n010306Nonbato_7",
            database="dataapp")
        cursor = mydb.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    

    # def create_query(list_of_cols, where = []):
    #     columns = ", ".join(list_of_cols)
    #     query = f"Select {columns} from dataapp.domanimals\
    #         where {where}"
    #     return(query)

    def select_clause(chosen_cols):
        homology_column = ", if(Animal_DEG = Human_gene_homolog, 'ortholog', 'paralog') as Homology"
        chosen_cols = ", ".join(chosen_cols)
        return "select "+ chosen_cols + homology_column
    
    def where_clause(chosen_prefs, chebs, pvalue = False, padj = False, homology = False):
        where_mass = []
        for i in range(len(chosen_prefs)):
            # print(chosen_prefs[i])
            if chosen_prefs[i]:
                for j in range(len(chosen_prefs[i])):
                    if chosen_prefs[i][j].find("'") != -1:
                        chosen_prefs[i][j] = chosen_prefs[i][j].replace("'", "`")
                new = chebs[i] + " in ('" + "', '".join(chosen_prefs[i]) + "') "
                where_mass.append(new)
        
        
        if len(pvalue):
            pv_clause = f"p_value {pvalue[0]} {pvalue[1]}"
            where_mass.append(pv_clause)
        if len(padj):
            padj_clause = f" Log2_Domestic_WT {padj[0]} {padj[1]}"
            where_mass.append(padj_clause)
        
        
        for i in range(len(homology)):
            homology_clause = f"homology in ('"+ "', '".join(homology) + "')"
        where_mass.append(homology_clause)


        where_clause = " AND ".join(where_mass)
        # for i in where_mass:
        #     print(i)
        return " where " + where_clause
    


    def query_for_chebox(k):
        query = f"select distinct {k.objectName()} from dataapp.domanimals order by {k.objectName()}"
        return ConnectInit.ret_query(query)
    
    def query_for_cols():
        query = f"select COLUMN_NAME FROM information_schema.COLUMNS \
         WHERE TABLE_SCHEMA = DATABASE() AND TABLE_NAME = 'domanimals'"
        return ConnectInit.ret_query(query) 

    

