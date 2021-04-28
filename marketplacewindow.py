# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'marketplacewindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MarketPlaceDialog(object):
    def setupUi(self, MarketPlaceDialog):
        MarketPlaceDialog.setObjectName("MarketPlaceDialog")
        MarketPlaceDialog.resize(723, 454)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("location.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MarketPlaceDialog.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(MarketPlaceDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(MarketPlaceDialog)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(MarketPlaceDialog)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEditGoodName = QtWidgets.QLineEdit(MarketPlaceDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditGoodName.sizePolicy().hasHeightForWidth())
        self.lineEditGoodName.setSizePolicy(sizePolicy)
        self.lineEditGoodName.setObjectName("lineEditGoodName")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEditGoodName)
        self.label_2 = QtWidgets.QLabel(MarketPlaceDialog)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.cmbGoodType = QtWidgets.QComboBox(MarketPlaceDialog)
        self.cmbGoodType.setObjectName("cmbGoodType")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.cmbGoodType)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnSave = QtWidgets.QPushButton(MarketPlaceDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSave.sizePolicy().hasHeightForWidth())
        self.btnSave.setSizePolicy(sizePolicy)
        self.btnSave.setObjectName("btnSave")
        self.horizontalLayout.addWidget(self.btnSave)
        self.btnUpdate = QtWidgets.QPushButton(MarketPlaceDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnUpdate.sizePolicy().hasHeightForWidth())
        self.btnUpdate.setSizePolicy(sizePolicy)
        self.btnUpdate.setObjectName("btnUpdate")
        self.horizontalLayout.addWidget(self.btnUpdate)
        self.btnDelete = QtWidgets.QPushButton(MarketPlaceDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnDelete.sizePolicy().hasHeightForWidth())
        self.btnDelete.setSizePolicy(sizePolicy)
        self.btnDelete.setObjectName("btnDelete")
        self.horizontalLayout.addWidget(self.btnDelete)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(MarketPlaceDialog)
        QtCore.QMetaObject.connectSlotsByName(MarketPlaceDialog)

    def retranslateUi(self, MarketPlaceDialog):
        _translate = QtCore.QCoreApplication.translate
        MarketPlaceDialog.setWindowTitle(_translate("MarketPlaceDialog", "Адреса магазинов"))
        self.label.setText(_translate("MarketPlaceDialog", "Адрес магазина"))
        self.label_2.setText(_translate("MarketPlaceDialog", "Торговая сеть"))
        self.btnSave.setText(_translate("MarketPlaceDialog", "Добавить"))
        self.btnUpdate.setText(_translate("MarketPlaceDialog", "Изменить"))
        self.btnDelete.setText(_translate("MarketPlaceDialog", "Удалить"))

