# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindowPage.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 725)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.splitter_8 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_8.setOrientation(QtCore.Qt.Vertical)
        self.splitter_8.setObjectName("splitter_8")
        self.splitter_5 = QtWidgets.QSplitter(self.splitter_8)
        self.splitter_5.setOrientation(QtCore.Qt.Vertical)
        self.splitter_5.setObjectName("splitter_5")
        self.splitter_4 = QtWidgets.QSplitter(self.splitter_5)
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setObjectName("splitter_4")
        self.groupBox = QtWidgets.QGroupBox(self.splitter_4)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter_2 = QtWidgets.QSplitter(self.groupBox)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.splitter = QtWidgets.QSplitter(self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.label_4 = QtWidgets.QLabel(self.splitter)
        self.label_4.setObjectName("label_4")
        self.cmbGoodTypes = QtWidgets.QComboBox(self.splitter)
        self.cmbGoodTypes.setObjectName("cmbGoodTypes")
        self.listWidgetGoods = QtWidgets.QListWidget(self.splitter_2)
        self.listWidgetGoods.setModelColumn(0)
        self.listWidgetGoods.setObjectName("listWidgetGoods")
        self.gridLayout.addWidget(self.splitter_2, 0, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.splitter_4)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.splitter_3 = QtWidgets.QSplitter(self.groupBox_2)
        self.splitter_3.setOrientation(QtCore.Qt.Vertical)
        self.splitter_3.setObjectName("splitter_3")
        self.cmbMarkets = QtWidgets.QComboBox(self.splitter_3)
        self.cmbMarkets.setObjectName("cmbMarkets")
        self.listWidgetRealMarkets = QtWidgets.QListWidget(self.splitter_3)
        self.listWidgetRealMarkets.setObjectName("listWidgetRealMarkets")
        self.gridLayout_2.addWidget(self.splitter_3, 0, 0, 1, 1)
        self.btnSearch = QtWidgets.QPushButton(self.splitter_5)
        self.btnSearch.setObjectName("btnSearch")
        self.splitter_7 = QtWidgets.QSplitter(self.splitter_8)
        self.splitter_7.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_7.setObjectName("splitter_7")
        self.splitter_6 = QtWidgets.QSplitter(self.splitter_7)
        self.splitter_6.setOrientation(QtCore.Qt.Vertical)
        self.splitter_6.setObjectName("splitter_6")
        self.listWidgetPrices = QtWidgets.QListWidget(self.splitter_6)
        self.listWidgetPrices.setObjectName("listWidgetPrices")
        self.btnShowMarket = QtWidgets.QPushButton(self.splitter_6)
        self.btnShowMarket.setObjectName("btnShowMarket")
        self.label = QtWidgets.QLabel(self.splitter_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.spinBoxScale = QtWidgets.QSpinBox(self.splitter_6)
        self.spinBoxScale.setMinimum(1)
        self.spinBoxScale.setMaximum(17)
        self.spinBoxScale.setProperty("value", 10)
        self.spinBoxScale.setObjectName("spinBoxScale")
        self.image = QtWidgets.QLabel(self.splitter_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image.sizePolicy().hasHeightForWidth())
        self.image.setSizePolicy(sizePolicy)
        self.image.setObjectName("image")
        self.gridLayout_4.addWidget(self.splitter_8, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbarX = QtWidgets.QStatusBar(MainWindow)
        self.statusbarX.setObjectName("statusbarX")
        MainWindow.setStatusBar(self.statusbarX)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Продукты"))
        self.label_4.setText(_translate("MainWindow", "Категория"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Магазины"))
        self.btnSearch.setText(_translate("MainWindow", "Найти"))
        self.btnShowMarket.setText(_translate("MainWindow", "Показать на карте"))
        self.label.setText(_translate("MainWindow", "Масштаб"))
        self.image.setText(_translate("MainWindow", "TextLabel"))

