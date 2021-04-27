# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GoodWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_GoodDialog(object):
    def setupUi(self, GoodDialog):
        GoodDialog.setObjectName("GoodDialog")
        GoodDialog.resize(640, 480)
        self.tableWidgetGoods = QtWidgets.QTableWidget(GoodDialog)
        self.tableWidgetGoods.setGeometry(QtCore.QRect(10, 20, 601, 241))
        self.tableWidgetGoods.setObjectName("tableWidgetGoods")
        self.tableWidgetGoods.setColumnCount(0)
        self.tableWidgetGoods.setRowCount(0)
        self.lineEditGoodName = QtWidgets.QLineEdit(GoodDialog)
        self.lineEditGoodName.setGeometry(QtCore.QRect(52, 270, 161, 31))
        self.lineEditGoodName.setObjectName("lineEditGoodName")
        self.cmbGoodType = QtWidgets.QComboBox(GoodDialog)
        self.cmbGoodType.setGeometry(QtCore.QRect(220, 270, 181, 31))
        self.cmbGoodType.setObjectName("cmbGoodType")
        self.btnSave = QtWidgets.QPushButton(GoodDialog)
        self.btnSave.setGeometry(QtCore.QRect(104, 340, 91, 31))
        self.btnSave.setObjectName("btnSave")
        self.btnUpdate = QtWidgets.QPushButton(GoodDialog)
        self.btnUpdate.setGeometry(QtCore.QRect(194, 340, 81, 31))
        self.btnUpdate.setObjectName("btnUpdate")
        self.btnDelete = QtWidgets.QPushButton(GoodDialog)
        self.btnDelete.setGeometry(QtCore.QRect(280, 340, 81, 31))
        self.btnDelete.setObjectName("btnDelete")

        self.retranslateUi(GoodDialog)
        QtCore.QMetaObject.connectSlotsByName(GoodDialog)

    def retranslateUi(self, GoodDialog):
        _translate = QtCore.QCoreApplication.translate
        GoodDialog.setWindowTitle(_translate("GoodDialog", "Dialog"))
        self.btnSave.setText(_translate("GoodDialog", "Сохранить"))
        self.btnUpdate.setText(_translate("GoodDialog", "Изменить"))
        self.btnDelete.setText(_translate("GoodDialog", "Удалить"))

