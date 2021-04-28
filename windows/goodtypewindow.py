# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'goodtypewindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_GoodTypeDialog(object):
    def setupUi(self, GoodTypeDialog):
        GoodTypeDialog.setObjectName("GoodTypeDialog")
        GoodTypeDialog.resize(723, 454)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("categories.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        GoodTypeDialog.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(GoodTypeDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(GoodTypeDialog)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(GoodTypeDialog)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEditName = QtWidgets.QLineEdit(GoodTypeDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditName.sizePolicy().hasHeightForWidth())
        self.lineEditName.setSizePolicy(sizePolicy)
        self.lineEditName.setObjectName("lineEditName")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEditName)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnSave = QtWidgets.QPushButton(GoodTypeDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSave.sizePolicy().hasHeightForWidth())
        self.btnSave.setSizePolicy(sizePolicy)
        self.btnSave.setObjectName("btnSave")
        self.horizontalLayout.addWidget(self.btnSave)
        self.btnUpdate = QtWidgets.QPushButton(GoodTypeDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnUpdate.sizePolicy().hasHeightForWidth())
        self.btnUpdate.setSizePolicy(sizePolicy)
        self.btnUpdate.setObjectName("btnUpdate")
        self.horizontalLayout.addWidget(self.btnUpdate)
        self.btnDelete = QtWidgets.QPushButton(GoodTypeDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnDelete.sizePolicy().hasHeightForWidth())
        self.btnDelete.setSizePolicy(sizePolicy)
        self.btnDelete.setObjectName("btnDelete")
        self.horizontalLayout.addWidget(self.btnDelete)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(GoodTypeDialog)
        QtCore.QMetaObject.connectSlotsByName(GoodTypeDialog)

    def retranslateUi(self, GoodTypeDialog):
        _translate = QtCore.QCoreApplication.translate
        GoodTypeDialog.setWindowTitle(_translate("GoodTypeDialog", "Категории товаров"))
        self.label.setText(_translate("GoodTypeDialog", "Категория"))
        self.btnSave.setText(_translate("GoodTypeDialog", "Добавить"))
        self.btnUpdate.setText(_translate("GoodTypeDialog", "Изменить"))
        self.btnDelete.setText(_translate("GoodTypeDialog", "Удалить"))

