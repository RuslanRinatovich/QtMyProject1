# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'windows\AuthPage.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(269, 237)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(269, 237))
        Form.setMaximumSize(QtCore.QSize(269, 111111))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("key.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 251, 221))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEditLogin = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEditLogin.setObjectName("lineEditLogin")
        self.verticalLayout.addWidget(self.lineEditLogin)
        self.lineEditPassword = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.verticalLayout.addWidget(self.lineEditPassword)
        self.btnAuth = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnAuth.sizePolicy().hasHeightForWidth())
        self.btnAuth.setSizePolicy(sizePolicy)
        self.btnAuth.setObjectName("btnAuth")
        self.verticalLayout.addWidget(self.btnAuth)
        self.btnRegs = QtWidgets.QPushButton(self.layoutWidget)
        self.btnRegs.setObjectName("btnRegs")
        self.verticalLayout.addWidget(self.btnRegs)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Войти"))
        self.lineEditLogin.setPlaceholderText(_translate("Form", "Login"))
        self.lineEditPassword.setPlaceholderText(_translate("Form", "Password"))
        self.btnAuth.setText(_translate("Form", "Войти"))
        self.btnRegs.setText(_translate("Form", "Регистрация"))

