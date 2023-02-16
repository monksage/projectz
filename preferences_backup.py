import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from main import *
from main_table import *
from defs_n_classes import *
import numpy as np
import os


class Ui_Set_Preferenses_Window(object):

    def setupUi(self, Set_Preferenses_Window):
        
        self.mass_of_cheboxes = []

        Set_Preferenses_Window.setObjectName("Set_Preferenses_Window")
        Set_Preferenses_Window.resize(800, 600)
        self.gridLayout = QtWidgets.QGridLayout(Set_Preferenses_Window)
        self.gridLayout.setObjectName("gridLayout")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Set_Preferenses_Window)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout.addWidget(self.plainTextEdit, 10, 6, 5, 2)
        self.btn_clear_Tissue = QtWidgets.QPushButton(Set_Preferenses_Window)
        self.btn_clear_Tissue.setMaximumSize(QtCore.QSize(16777215, 24))
        self.btn_clear_Tissue.setObjectName("btn_clear_Tissue")
        self.gridLayout.addWidget(self.btn_clear_Tissue, 3, 3, 1, 1)
        self.btn_show = QtWidgets.QPushButton(Set_Preferenses_Window)
        self.btn_show.setObjectName("pushButton")
        self.gridLayout.addWidget(self.btn_show, 0, 6, 1, 1)
        self.Animal_DEG_cb = CheckableComboBox(Set_Preferenses_Window)
        self.mass_of_cheboxes.append(self.Animal_DEG_cb)
        self.Animal_DEG_cb.setMaximumSize(QtCore.QSize(16777215, 21))
        self.Animal_DEG_cb.setObjectName("Animal_DEG")
        self.gridLayout.addWidget(self.Animal_DEG_cb, 9, 3, 1, 3)
        self.label_6 = QtWidgets.QLabel(Set_Preferenses_Window)
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 16))
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 3, 1, 3)
        self.Tissue_cb = CheckableComboBox(Set_Preferenses_Window)
        self.mass_of_cheboxes.append(self.Tissue_cb)
        self.Tissue_cb.setMaximumSize(QtCore.QSize(16777215, 21))
        self.Tissue_cb.setObjectName("Tissue")
        self.gridLayout.addWidget(self.Tissue_cb, 2, 3, 1, 3)
        self.btn_clear_human_features = QtWidgets.QPushButton(Set_Preferenses_Window)
        self.btn_clear_human_features.setMaximumSize(QtCore.QSize(16777215, 24))
        self.btn_clear_human_features.setObjectName("btn_clear_human_features")
        self.gridLayout.addWidget(self.btn_clear_human_features, 10, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(Set_Preferenses_Window)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 16))
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        self.chosen_text_Animal_DEG = QtWidgets.QPlainTextEdit(Set_Preferenses_Window)
        self.chosen_text_Animal_DEG.setObjectName("chosen_text_Animal_DEG")
        self.gridLayout.addWidget(self.chosen_text_Animal_DEG, 15, 6, 1, 1)
        self.Overexpression_sign = CheckableComboBox(Set_Preferenses_Window)
        self.mass_of_cheboxes.append(self.Overexpression_sign)
        self.Overexpression_sign.setMaximumSize(QtCore.QSize(16777215, 21))
        self.Overexpression_sign.setObjectName("overexpression_sign")
        self.gridLayout.addWidget(self.Overexpression_sign, 11, 1, 1, 1)
        self.Human_features_cb = CheckableComboBox(Set_Preferenses_Window)
        self.mass_of_cheboxes.append(self.Human_features_cb)
        self.Human_features_cb.setObjectName("human_feature")
        self.gridLayout.addWidget(self.Human_features_cb, 9, 0, 1, 2)
        self.btn_clear_Human_gene_homolog = QtWidgets.QPushButton(Set_Preferenses_Window)
        self.btn_clear_Human_gene_homolog.setMaximumSize(QtCore.QSize(16777215, 24))
        self.btn_clear_Human_gene_homolog.setObjectName("btn_clear_Human_gene_homolog")
        self.gridLayout.addWidget(self.btn_clear_Human_gene_homolog, 6, 3, 1, 1)
        self.btn_cancel_SPW = QtWidgets.QPushButton(Set_Preferenses_Window)
        self.btn_cancel_SPW.setMaximumSize(QtCore.QSize(16777215, 24))
        self.btn_cancel_SPW.setObjectName("btn_cancel_SPW")
        self.gridLayout.addWidget(self.btn_cancel_SPW, 15, 3, 1, 1, QtCore.Qt.AlignBottom)
        self.btn_clear_Animal_DEG = QtWidgets.QPushButton(Set_Preferenses_Window)
        self.btn_clear_Animal_DEG.setMaximumSize(QtCore.QSize(16777215, 24))
        self.btn_clear_Animal_DEG.setObjectName("btn_clear_Animal_DEG")
        self.gridLayout.addWidget(self.btn_clear_Animal_DEG, 10, 3, 1, 1)
        self.label_8 = QtWidgets.QLabel(Set_Preferenses_Window)
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 21))
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 12, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(Set_Preferenses_Window)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 16))
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 2)
        self.Underexpression_sign = CheckableComboBox(Set_Preferenses_Window)
        self.mass_of_cheboxes.append(self.Underexpression_sign)
        self.Underexpression_sign.setMaximumSize(QtCore.QSize(16777215, 21))
        self.Underexpression_sign.setObjectName("underexpression_sign")
        self.gridLayout.addWidget(self.Underexpression_sign, 11, 0, 1, 1)
        self.btn_selectall_human_features = QtWidgets.QPushButton(Set_Preferenses_Window)
        self.btn_selectall_human_features.setMaximumSize(QtCore.QSize(16777215, 24))
        self.btn_selectall_human_features.setObjectName("btn_selectall_human_features")
        self.gridLayout.addWidget(self.btn_selectall_human_features, 10, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(Set_Preferenses_Window)
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 16))
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 7, 3, 1, 1)
        self.Columns_cb = CheckableComboBox(Set_Preferenses_Window)
        self.Columns_cb.setMaximumSize(QtCore.QSize(16777215, 21))
        self.Columns_cb.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.Columns_cb.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.Columns_cb.setObjectName("Columns_cb")
        self.gridLayout.addWidget(self.Columns_cb, 2, 0, 1, 2)
        self.label_9 = QtWidgets.QLabel(Set_Preferenses_Window)
        self.label_9.setMaximumSize(QtCore.QSize(16777215, 21))
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 12, 1, 1, 1)
        self.Animal_cb = CheckableComboBox(Set_Preferenses_Window)
        self.mass_of_cheboxes.append(self.Animal_cb)
        self.Animal_cb.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Animal_cb.sizePolicy().hasHeightForWidth())
        self.Animal_cb.setSizePolicy(sizePolicy)
        self.Animal_cb.setMaximumSize(QtCore.QSize(16777215, 21))
        self.Animal_cb.setObjectName("Animal")
        self.gridLayout.addWidget(self.Animal_cb, 5, 0, 1, 2)
        self.btn_clear_Animal = QtWidgets.QPushButton(Set_Preferenses_Window)
        self.btn_clear_Animal.setMaximumSize(QtCore.QSize(16777215, 24))
        self.btn_clear_Animal.setObjectName("btn_clear_Animal")
        self.gridLayout.addWidget(self.btn_clear_Animal, 6, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 3, 2, 1, 1)
        self.chosen_text_Tissue = QtWidgets.QPlainTextEdit(Set_Preferenses_Window)
        self.chosen_text_Tissue.setObjectName("chosen_text_Tissue")
        self.gridLayout.addWidget(self.chosen_text_Tissue, 1, 7, 9, 1)
        self.btn_selectall_Columns_cb = QtWidgets.QPushButton(Set_Preferenses_Window)
        self.btn_selectall_Columns_cb.setMaximumSize(QtCore.QSize(16777215, 24))
        self.btn_selectall_Columns_cb.setObjectName("btn_selectall_Columns_cb")
        self.gridLayout.addWidget(self.btn_selectall_Columns_cb, 3, 1, 1, 1)
        self.chosen_text_Human_gene_homolog = QtWidgets.QPlainTextEdit(Set_Preferenses_Window)
        self.chosen_text_Human_gene_homolog.setObjectName("chosen_text_Human_gene_homolog")
        self.gridLayout.addWidget(self.chosen_text_Human_gene_homolog, 15, 7, 1, 1)
        self.label = QtWidgets.QLabel(Set_Preferenses_Window)
        self.label.setMaximumSize(QtCore.QSize(16777215, 16))
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 4)
        self.chosen_text_Animals = QtWidgets.QTextEdit(Set_Preferenses_Window)
        self.chosen_text_Animals.setObjectName("chosen_text_Animals")
        self.gridLayout.addWidget(self.chosen_text_Animals, 1, 6, 9, 1)
        self.label_4 = QtWidgets.QLabel(Set_Preferenses_Window)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 16))
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(Set_Preferenses_Window)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 7, 0, 1, 1)
        self.btn_selectall_Tissue = QtWidgets.QPushButton(Set_Preferenses_Window)
        self.btn_selectall_Tissue.setMaximumSize(QtCore.QSize(16777215, 24))
        self.btn_selectall_Tissue.setObjectName("btn_selectall_Tissue")
        self.gridLayout.addWidget(self.btn_selectall_Tissue, 3, 4, 1, 2)
        self.btn_selectall_Human_gene_homolog = QtWidgets.QPushButton(Set_Preferenses_Window)
        self.btn_selectall_Human_gene_homolog.setMaximumSize(QtCore.QSize(16777215, 24))
        self.btn_selectall_Human_gene_homolog.setObjectName("btn_selectall_Human_gene_homolog")
        self.gridLayout.addWidget(self.btn_selectall_Human_gene_homolog, 6, 4, 1, 2)
        self.btn_selectall_Animal = QtWidgets.QPushButton(Set_Preferenses_Window)
        self.btn_selectall_Animal.setMaximumSize(QtCore.QSize(16777215, 24))
        self.btn_selectall_Animal.setObjectName("btn_selectall_Animal")
        self.gridLayout.addWidget(self.btn_selectall_Animal, 6, 1, 1, 1)
        self.HumanGH_cb = CheckableComboBox(Set_Preferenses_Window)
        self.mass_of_cheboxes.append(self.HumanGH_cb)
        self.HumanGH_cb.setMaximumSize(QtCore.QSize(16777215, 21))
        self.HumanGH_cb.setObjectName("Human_gene_homolog")
        self.gridLayout.addWidget(self.HumanGH_cb, 5, 3, 1, 3)
        self.btn_selectall_Animal_DEG = QtWidgets.QPushButton(Set_Preferenses_Window)
        self.btn_selectall_Animal_DEG.setMaximumSize(QtCore.QSize(16777215, 24))
        self.btn_selectall_Animal_DEG.setObjectName("btn_selectall_Animal_DEG")
        self.gridLayout.addWidget(self.btn_selectall_Animal_DEG, 10, 5, 1, 1)
        self.btn_clear_Columns_cb = QtWidgets.QPushButton(Set_Preferenses_Window)
        self.btn_clear_Columns_cb.setMaximumSize(QtCore.QSize(16777215, 24))
        self.btn_clear_Columns_cb.setObjectName("btn_clear_Columns_cb")
        self.gridLayout.addWidget(self.btn_clear_Columns_cb, 3, 0, 1, 1)
        self.btn_OK_SPW = QtWidgets.QPushButton(Set_Preferenses_Window)
        self.btn_OK_SPW.setMaximumSize(QtCore.QSize(16777215, 24))
        self.btn_OK_SPW.setObjectName("btn_OK_SPW")
        self.gridLayout.addWidget(self.btn_OK_SPW, 15, 5, 1, 1, QtCore.Qt.AlignBottom)

        self.retranslateUi(Set_Preferenses_Window)
        QtCore.QMetaObject.connectSlotsByName(Set_Preferenses_Window)
        

    def retranslateUi(self, Set_Preferenses_Window):
        _translate = QtCore.QCoreApplication.translate
        Set_Preferenses_Window.setWindowTitle(_translate("Set_Preferenses_Window", "Preferences"))
        self.plainTextEdit.setPlainText(_translate("Set_Preferenses_Window", "Human features:"))
        self.btn_clear_Tissue.setText(_translate("Set_Preferenses_Window", "Clear"))
        self.btn_show.setText(_translate("Set_Preferenses_Window", "Show selected preferences"))
        self.label_6.setText(_translate("Set_Preferenses_Window", "Human gene-homolog"))
        self.btn_clear_human_features.setText(_translate("Set_Preferenses_Window", "Clear"))
        self.label_3.setText(_translate("Set_Preferenses_Window", "Animal"))
        self.chosen_text_Animal_DEG.setPlainText(_translate("Set_Preferenses_Window", "Animal DEGs:\n"
""))
        self.btn_clear_Human_gene_homolog.setText(_translate("Set_Preferenses_Window", "Clear"))
        self.btn_cancel_SPW.setText(_translate("Set_Preferenses_Window", "Cancel"))
        self.btn_clear_Animal_DEG.setText(_translate("Set_Preferenses_Window", "Clear"))
        self.label_8.setText(_translate("Set_Preferenses_Window", "Underexpression effect"))
        self.label_2.setText(_translate("Set_Preferenses_Window", "Choose columns"))
        self.btn_selectall_human_features.setText(_translate("Set_Preferenses_Window", "Select all"))
        self.label_7.setText(_translate("Set_Preferenses_Window", "Animal DEG"))
        self.Columns_cb.setItemText(0, _translate("Set_Preferenses_Window", "Новый элемент"))
        self.Columns_cb.setItemText(1, _translate("Set_Preferenses_Window", "Новый элемент"))
        self.Columns_cb.setItemText(2, _translate("Set_Preferenses_Window", "Новый элемент"))
        self.Columns_cb.setItemText(3, _translate("Set_Preferenses_Window", "Новый элемент"))
        self.Columns_cb.setItemText(4, _translate("Set_Preferenses_Window", "Новый элемент"))
        self.Columns_cb.setItemText(5, _translate("Set_Preferenses_Window", "Новый элемент"))
        self.Columns_cb.setItemText(6, _translate("Set_Preferenses_Window", "Новый элемент"))
        self.label_9.setText(_translate("Set_Preferenses_Window", "Overexpression effect"))
        self.btn_clear_Animal.setText(_translate("Set_Preferenses_Window", "Clear"))
        self.chosen_text_Tissue.setPlainText(_translate("Set_Preferenses_Window", "Tissue:\n"
""))
        self.btn_selectall_Columns_cb.setText(_translate("Set_Preferenses_Window", "Select all"))
        self.chosen_text_Human_gene_homolog.setPlainText(_translate("Set_Preferenses_Window", "Human gene-homologs:"))
        self.label.setText(_translate("Set_Preferenses_Window", "Welcome to SNP TATA Z-Tester Database"))
        self.chosen_text_Animals.setHtml(_translate("Set_Preferenses_Window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9.07087pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9.07087pt;\">Animal:</span></p></body></html>"))
        self.label_4.setText(_translate("Set_Preferenses_Window", "Tissue"))
        self.label_5.setText(_translate("Set_Preferenses_Window", "Human features"))
        self.btn_selectall_Tissue.setText(_translate("Set_Preferenses_Window", "Select all"))
        self.btn_selectall_Human_gene_homolog.setText(_translate("Set_Preferenses_Window", "Select all"))
        self.btn_selectall_Animal.setText(_translate("Set_Preferenses_Window", "Select all"))
        self.btn_selectall_Animal_DEG.setText(_translate("Set_Preferenses_Window", "Select all"))
        self.btn_clear_Columns_cb.setText(_translate("Set_Preferenses_Window", "Clear"))
        self.btn_OK_SPW.setText(_translate("Set_Preferenses_Window", "OK"))
        self.object_names_mass = []
    
        for cheb in self.mass_of_cheboxes:
            self.object_names_mass.append(cheb.objectName())


        #mass of cheboxes: 
        # Animal_DEG 
        # Tissue
        # overexpression_sign
        # human_feature
        # underexpression_sign
        # Animal
        # Human_gene_homolog
        try:
            self.prefs_of_Columns = []
            self.prefs_of_each = []
            self.prefs_of_Columns = np.load("prefs_of_Columns.npy")
            for i in range(len(self.prefs_of_Columns)):
                self.Columns_cb.addItem("")
                self.Columns_cb.setItemText(i, _translate("Widget", self.prefs_of_Columns[i]))
            self.prefs_of_each = np.load("prefs_of_each.npy", allow_pickle=True)
            for mass in range(len(self.mass_of_cheboxes)):
                for chebox_value in range(len(self.prefs_of_each[mass])):
                    self.mass_of_cheboxes[mass].addItem("")
                    self.mass_of_cheboxes[mass].setItemText(chebox_value, _translate("Widget", f"{str(self.prefs_of_each[mass][chebox_value])}"))
                    # print(self.prefs_of_each[mass][chebox_value])
        except:
            for i in range(len(ConnectInit.query_for_cols())):
                self.Columns_cb.addItem("")
                self.Columns_cb.setItemText(i, _translate("Widget", f"{take_distinct(ConnectInit.query_for_cols())[i]}"))
                self.prefs_of_Columns.append(take_distinct(ConnectInit.query_for_cols())[i])
            np.save("prefs_of_Columns.npy", self.prefs_of_Columns)

            for j in range(len(self.mass_of_cheboxes)):
                query_mass = []
                for i in range(len(take_distinct(ConnectInit.query_for_chebox(self.mass_of_cheboxes[j])))):
                    self.mass_of_cheboxes[j].addItem("")
                    self.mass_of_cheboxes[j].setItemText(i, _translate("Widget", f"{take_distinct(ConnectInit.query_for_chebox(self.mass_of_cheboxes[j]))[i]}"))
                    query_mass.append(take_distinct(ConnectInit.query_for_chebox(self.mass_of_cheboxes[j]))[i])
                self.prefs_of_each.append(query_mass)
            np.save("prefs_of_each.npy", self.prefs_of_each)
            
    def make_temp_choice(self, Set_Preferenses_Window):
        temp_choice = []
        for chebox in self.mass_of_cheboxes:
            temp_col_choice = []
            for value in what_items(self, chebox):
                temp_col_choice.append(value)
            temp_choice.append(temp_col_choice)
        # for cheb in self.mass_of_cheboxes:
        #     print(cheb.objectName())
        return temp_choice
    
    def dict_of_choices(self, Set_Preferenses_Window):
        mass_of_choices = dict()
        for index_of_cheb in range(len(self.object_names_mass)):
            mass_of_choices[self.object_names_mass[index_of_cheb]] = self.make_temp_choice(Set_Preferenses_Window)[index_of_cheb] 
        # for key, value in mass_of_choices.items():
        #     print(key, value)
        return mass_of_choices

    def clear_chebox(self, chebox, Set_Preferenses_Window):
        for value in range(len(chebox)):
            self.clear_one_value(chebox, value, Set_Preferenses_Window)

    def clear_one_value(self, chebox, index, Set_Preferenses_Window):
        return chebox.itemUnselected(index)

    def select_all_chebox(self, chebox, Set_Preferenses_Window):
        for value in range(len(chebox)):
            self.select_one_value(chebox, value, Set_Preferenses_Window)
    
    def select_one_value(self, chebox, index, Set_Preferenses_Window):
        return chebox.itemSelected(index)

    def save_prefs(self, Set_Preferenses_Window):
        chosen_columns = what_items(self, self.Columns_cb)
        self.chosen_prefs = self.make_temp_choice(Set_Preferenses_Window)
        a = ["Record_number", "Animal_DEG_No", "Animal", "Tissue",\
        "Domestic_form", "Wild_form", "Experiment", "Animal_DEG",\
        "Log2_Domestic_WT", "p_value", "Padj_value", "PMID_animal",\
        "Underexpression_versus_most_recent_common_ancestor",\
        "Overexpression_versus_most_recent_common_ancestor",\
        "Human_gene_homolog", "UniqueNCBIEntrezGeneID", "human_feature",\
        "Effects_of_underexpression_of_the_gene_on_the_feature_in_human", \
        "underexpression_sign", "PMID_deficit", "Effects_of_overexpressions_of_the_gene_on_the_feature_in_human", \
        "overexpression_sign", "PMID_excess", "PMID_record"]

        self.chosen_columns = []
        dict_of_number = dict()
        for i in range(len(a)):
            dict_of_number[i] = a[i]
        for value in dict_of_number.values():
            for i in range(len(chosen_columns)):
                if value == chosen_columns[i]:
                    self.chosen_columns.append(value)
        


        np.save("chosen_columns.npy", self.chosen_columns)
        np.save("chosen_prefs.npy", self.chosen_prefs)
        Set_Preferenses_Window.hide()

    
    def show_prefs(self, Set_Preferenses_Window):
        bschar = "\n"
        self.plainTextEdit.setPlainText(f"{self.object_names_mass[3]}:{bschar}{f',{bschar}'.join(self.dict_of_choices(Set_Preferenses_Window)[self.object_names_mass[3]])}")
        self.chosen_text_Animal_DEG.setPlainText(f"{self.object_names_mass[0]}:{bschar}{f',{bschar}'.join(self.dict_of_choices(Set_Preferenses_Window)[self.object_names_mass[0]])}")
        self.chosen_text_Animals.setPlainText(f"{self.object_names_mass[5]}:{bschar}{f',{bschar}'.join(self.dict_of_choices(Set_Preferenses_Window)[self.object_names_mass[5]])}")
        self.chosen_text_Human_gene_homolog.setPlainText(f"{self.object_names_mass[6]}:{bschar}{f',{bschar}'.join(self.dict_of_choices(Set_Preferenses_Window)[self.object_names_mass[6]])}")
        self.chosen_text_Tissue.setPlainText(f"{self.object_names_mass[1]}:{bschar}{f',{bschar}'.join(self.dict_of_choices(Set_Preferenses_Window)[self.object_names_mass[1]])}")

    def pref_funcs(self, Set_Preferenses_Window):
        #clear btns
        self.btn_clear_Animal.clicked.connect(lambda: self.clear_chebox(self.Animal_cb, Set_Preferenses_Window))
        self.btn_clear_Animal_DEG.clicked.connect(lambda: self.clear_chebox(self.Animal_DEG_cb, Set_Preferenses_Window))
        self.btn_clear_Columns_cb.clicked.connect(lambda: self.clear_chebox(self.Columns_cb, Set_Preferenses_Window))
        self.btn_clear_human_features.clicked.connect(lambda: self.clear_chebox(self.Human_features_cb, Set_Preferenses_Window))
        self.btn_clear_Human_gene_homolog.clicked.connect(lambda: self.clear_chebox(self.HumanGH_cb, Set_Preferenses_Window))
        self.btn_clear_Tissue.clicked.connect(lambda: self.clear_chebox(self.Tissue_cb, Set_Preferenses_Window))
        #select_all btns
        self.btn_selectall_Animal.clicked.connect(lambda: self.select_all_chebox(self.Animal_cb, Set_Preferenses_Window))
        self.btn_selectall_Animal_DEG.clicked.connect(lambda: self.select_all_chebox(self.Animal_DEG_cb, Set_Preferenses_Window))
        self.btn_selectall_Columns_cb.clicked.connect(lambda: self.select_all_chebox(self.Columns_cb, Set_Preferenses_Window))
        self.btn_selectall_human_features.clicked.connect(lambda: self.select_all_chebox(self.Human_features_cb, Set_Preferenses_Window))
        self.btn_selectall_Tissue.clicked.connect(lambda: self.select_all_chebox(self.Tissue_cb, Set_Preferenses_Window))
        self.btn_selectall_Human_gene_homolog.clicked.connect(lambda: self.select_all_chebox(self.HumanGH_cb, Set_Preferenses_Window))
        #btn show
        self.btn_show.clicked.connect(lambda: (self.show_prefs(Set_Preferenses_Window)))
        #btn ok
        self.btn_OK_SPW.clicked.connect(lambda: (self.save_prefs(Set_Preferenses_Window)))



    def show_window(self, Set_Preferences_Window):
        self.show()