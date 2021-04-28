# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'goodwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_GoodDialog(object):
    def setupUi(self, GoodDialog):
        GoodDialog.setObjectName("GoodDialog")
        GoodDialog.resize(723, 454)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("box.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        GoodDialog.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(GoodDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidgetGoods = QtWidgets.QTableWidget(GoodDialog)
        self.tableWidgetGoods.setObjectName("tableWidgetGoods")
        self.tableWidgetGoods.setColumnCount(0)
        self.tableWidgetGoods.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidgetGoods)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(GoodDialog)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEditGoodName = QtWidgets.QLineEdit(GoodDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditGoodName.sizePolicy().hasHeightForWidth())
        self.lineEditGoodName.setSizePolicy(sizePolicy)
        self.lineEditGoodName.setObjectName("lineEditGoodName")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEditGoodName)
        self.label_2 = QtWidgets.QLabel(GoodDialog)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.cmbGoodType = QtWidgets.QComboBox(GoodDialog)
        self.cmbGoodType.setObjectName("cmbGoodType")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.cmbGoodType)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnSave = QtWidgets.QPushButton(GoodDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSave.sizePolicy().hasHeightForWidth())
        self.btnSave.setSizePolicy(sizePolicy)
        self.btnSave.setObjectName("btnSave")
        self.horizontalLayout.addWidget(self.btnSave)
        self.btnUpdate = QtWidgets.QPushButton(GoodDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnUpdate.sizePolicy().hasHeightForWidth())
        self.btnUpdate.setSizePolicy(sizePolicy)
        self.btnUpdate.setObjectName("btnUpdate")
        self.horizontalLayout.addWidget(self.btnUpdate)
        self.btnDelete = QtWidgets.QPushButton(GoodDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnDelete.sizePolicy().hasHeightForWidth())
        self.btnDelete.setSizePolicy(sizePolicy)
        self.btnDelete.setObjectName("btnDelete")
        self.horizontalLayout.addWidget(self.btnDelete)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(GoodDialog)
        QtCore.QMetaObject.connectSlotsByName(GoodDialog)

    def retranslateUi(self, GoodDialog):
        _translate = QtCore.QCoreApplication.translate
        GoodDialog.setWindowTitle(_translate("GoodDialog", "Товары"))
        self.label.setText(_translate("GoodDialog", "Название товара"))
        self.label_2.setText(_translate("GoodDialog", "Категория товара"))
        self.btnSave.setText(_translate("GoodDialog", "Добавить"))
        self.btnUpdate.setText(_translate("GoodDialog", "Изменить"))
        self.btnDelete.setText(_translate("GoodDialog", "Удалить"))

