# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AuthPage.ui'
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
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(10, 10, 251, 221))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEditLogin = QtWidgets.QLineEdit(self.widget)
        self.lineEditLogin.setObjectName("lineEditLogin")
        self.verticalLayout.addWidget(self.lineEditLogin)
        self.lineEditPassword = QtWidgets.QLineEdit(self.widget)
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.verticalLayout.addWidget(self.lineEditPassword)
        self.btnRegs = QtWidgets.QPushButton(self.widget)
        self.btnRegs.setObjectName("btnRegs")
        self.verticalLayout.addWidget(self.btnRegs)
        self.btnAuth = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnAuth.sizePolicy().hasHeightForWidth())
        self.btnAuth.setSizePolicy(sizePolicy)
        self.btnAuth.setObjectName("btnAuth")
        self.verticalLayout.addWidget(self.btnAuth)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Войти"))
        self.lineEditLogin.setPlaceholderText(_translate("Form", "Login"))
        self.lineEditPassword.setPlaceholderText(_translate("Form", "Password"))
        self.btnRegs.setText(_translate("Form", "Регистрация"))
        self.btnAuth.setText(_translate("Form", "Войти"))

