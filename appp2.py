import os
import io
from goompy import GooMPy
import sys
import folium
import requests
import sqlite3
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QLabel, QMainWindow,QVBoxLayout, QSpinBox, QDoubleSpinBox, QComboBox
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap
from authpage import Ui_Form
from check_db import *
from mainwindowpage import Ui_MainWindow
from qt_material import apply_stylesheet

SCREEN_SIZE = [650, 450]
STEP = 1
API_KEY = '40d1649f-0493-4b70-98ba-98533de7710b'

class MyWidget(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.btnAuth.clicked.connect(self.auth)
        self.ui.btnRegs.clicked.connect(self.reg)
        self.base_line_edit = [self.ui.lineEditLogin, self.ui.lineEditPassword]
        self.check_db = CheckThread()
        self.check_db.mysignal.connect(self.signal_handler)

    def check_input(funct):
        def wrapper(self):
            for line_edit in self.base_line_edit:
                if len(line_edit.text()) == 0:
                    return
            funct(self)
        return  wrapper

    @check_input
    def auth(self):
        print(1)
        name = self.ui.lineEditLogin.text()
        passw = self.ui.lineEditPassword.text()
        self.check_db.thr_login(name, passw)

    @check_input
    def reg(self):
        name = self.ui.lineEditLogin.text()
        passw = self.ui.lineEditPassword.text()
        self.check_db.thr_register(name, passw)

    def signal_handler(self, value):
        if value == '1':
            QMessageBox.about(self, 'Оповещение', "Успешно")
            self.second_form = MainWindowPage(self, self.ui.lineEditLogin.text())
            self.hide()
            self.second_form.show()
        elif value == '2':
            QMessageBox.about(self, 'Оповещение', "Проверьте логин и пароль")
        elif value == '3':
            QMessageBox.about(self, 'Оповещение', "Такой пользоватлеь уже существует")
        elif value == '4':
            QMessageBox.about(self, 'Оповещение', "Вы успешно зарегистрировались")
        else:
            QMessageBox.about(self, 'Оповещение', "Ошибка подключения")

    def run(self):
        showdialog()


def showdialog():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)

    msg.setText("This is a message box")
    msg.setInformativeText("This is additional information")
    msg.setWindowTitle("MessageBox demo")
    msg.setDetailedText("The details are as follows:")
    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    msg.buttonClicked.connect(msgbtn)

    retval = msg.exec_()
    print("value of pressed message box button:", retval)

def msgbtn(i):
   print ("Button pressed is:",i.text())

class SecondForm(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.initUI(args)

    def initUI(self, args):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Вторая форма')
        self.lbl = QLabel(args[-1], self)
        self.lbl.adjustSize()

class MainWindowPage(QMainWindow, Ui_MainWindow):
    def __init__(self, *args):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.statusbarX.showMessage(args[-1])
        coordinate = (55.848563748830024, 48.50656478853732)
        self.m = folium.Map(
            tiles='Stamen Terrain',
            zoom_start=13,
            location=coordinate
        )
        self.m.add_child(folium.LatLngPopup())

        # save map data to data object
        data = io.BytesIO()
        self.m.save(data, close_file=False)

        webView = QWebEngineView()
        webView.setHtml(data.getvalue().decode())
        self.ui.verticalLayout.addWidget(webView)

    def keyPressEvent(self, event):
        if (event.key() == 16777238):
            self.spinbox.setValue(self.spinbox.value() + 1)
        if (event.key() == 16777239):
            self.spinbox.setValue(self.spinbox.value() - 1)
        step = float(self.combo.currentText())
        lattitude, longitude = self.spinbox_lattitude.value(), self.spinbox_longitude.value()
        if (event.key() == 16777235):
            self.spinbox_lattitude.setValue(lattitude + step)
        if (event.key() == 16777237):
            self.spinbox_lattitude.setValue(lattitude - step)
        if (event.key() == 16777234):
            self.spinbox_longitude.setValue(longitude - step)
        if (event.key() == 16777236):
            self.spinbox_longitude.setValue(longitude + step)
        #print("pressed key " + str(event.key()))

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Folium in PyQt Example')
        self.window_width, self.window_height = 1600, 1200
        self.setMinimumSize(self.window_width, self.window_height)

        layout = QVBoxLayout()
        self.setLayout(layout)

        coordinate = (37.8199286, -122.4782551)
        m = folium.Map(
        	tiles='Stamen Terrain',
        	zoom_start=13,
        	location=coordinate
        )
        m.add_child(folium.LatLngPopup())

        # save map data to data object
        data = io.BytesIO()
        m.save(data, close_file=False)

        webView = QWebEngineView()
        webView.setHtml(data.getvalue().decode())
        layout.addWidget(webView)



def main():
    app = QApplication(sys.argv)
    ex = MyWidget()
    apply_stylesheet(app, theme='dark_cyan.xml')
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()


