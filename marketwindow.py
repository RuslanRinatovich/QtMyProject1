# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'marketwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MarketDialog(object):
    def setupUi(self, MarketDialog):
        MarketDialog.setObjectName("MarketDialog")
        MarketDialog.resize(723, 454)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("shop.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MarketDialog.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(MarketDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidgetMarkets = QtWidgets.QTableWidget(MarketDialog)
        self.tableWidgetMarkets.setObjectName("tableWidgetMarkets")
        self.tableWidgetMarkets.setColumnCount(0)
        self.tableWidgetMarkets.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidgetMarkets)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(MarketDialog)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEditGoodName = QtWidgets.QLineEdit(MarketDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditGoodName.sizePolicy().hasHeightForWidth())
        self.lineEditGoodName.setSizePolicy(sizePolicy)
        self.lineEditGoodName.setObjectName("lineEditGoodName")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEditGoodName)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnSave = QtWidgets.QPushButton(MarketDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSave.sizePolicy().hasHeightForWidth())
        self.btnSave.setSizePolicy(sizePolicy)
        self.btnSave.setObjectName("btnSave")
        self.horizontalLayout.addWidget(self.btnSave)
        self.btnUpdate = QtWidgets.QPushButton(MarketDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnUpdate.sizePolicy().hasHeightForWidth())
        self.btnUpdate.setSizePolicy(sizePolicy)
        self.btnUpdate.setObjectName("btnUpdate")
        self.horizontalLayout.addWidget(self.btnUpdate)
        self.btnDelete = QtWidgets.QPushButton(MarketDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnDelete.sizePolicy().hasHeightForWidth())
        self.btnDelete.setSizePolicy(sizePolicy)
        self.btnDelete.setObjectName("btnDelete")
        self.horizontalLayout.addWidget(self.btnDelete)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(MarketDialog)
        QtCore.QMetaObject.connectSlotsByName(MarketDialog)

    def retranslateUi(self, MarketDialog):
        _translate = QtCore.QCoreApplication.translate
        MarketDialog.setWindowTitle(_translate("MarketDialog", "Магазины"))
        self.label.setText(_translate("MarketDialog", "Название магазина"))
        self.btnSave.setText(_translate("MarketDialog", "Добавить"))
        self.btnUpdate.setText(_translate("MarketDialog", "Изменить"))
        self.btnDelete.setText(_translate("MarketDialog", "Удалить"))

