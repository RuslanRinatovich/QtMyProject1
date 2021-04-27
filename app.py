import os
import io
import sys
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
from data.models import User, Good, GoodMarket, GoodType, Market, MarketPlace

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
        self.markets = []
        self.goodtypes = []
        self.goods = []
        self.marketplaces = []
        self.goodmarkets = []
        self.load_markets()
        self.load_goodtypes()
        self.show_map(get_coordinates("Зеленодольск, ул.Карла-Маркса, 7"))
        self.ui.cmbGoodTypes.currentTextChanged.connect(self.load_goods)
        self.ui.cmbMarkets.currentTextChanged.connect(self.load_market_places)


    # список магазинов
    def load_markets(self):
        con = sqlite3.connect("data/my_market_db")
        # Создание курсора
        cur = con.cursor()

        # Выполнение запроса и получение всех результатов
        result = cur.execute("SELECT * FROM markets").fetchall()
        #g = Market(0, 'Все', '1')
        self.ui.cmbMarkets.addItem('Все')
        # Вывод результатов на экран
        for elem in result:
            self.ui.cmbMarkets.addItem(elem[1])
            market = Market(elem[0], elem[1], elem[2])
            self.markets.append(market)

        print(self.markets)

        con.close()

    # список типов продуктов
    def load_goodtypes(self):
        con = sqlite3.connect("data/my_market_db")
        # Создание курсора
        cur = con.cursor()

        # Выполнение запроса и получение всех результатов
        result = cur.execute("SELECT * FROM goodtypes").fetchall()

        self.ui.cmbGoodTypes.addItem('Все')

        # Вывод результатов на экран
        for elem in result:
            self.ui.cmbGoodTypes.addItem(elem[1])
            item = GoodType(elem[0],elem[1])
            self.goodtypes.append(item)


        con.close()

    # список продуктов
    def load_goods(self):
        self.ui.listWidgetGoods.clear()
        con = sqlite3.connect("data/my_market_db")
        type = self.ui.cmbGoodTypes.currentText()
        print(type)
        # Создание курсора
        cur = con.cursor()
        if type == 'Все':
            # Выполнение запроса и получение всех результатов
            result = cur.execute("SELECT * FROM goods").fetchall()
        else:
            typek = 0
            for x in self.goodtypes:
                if type == x.goodtypename:
                    typek = x.id
            print(typek)
            result = []
            result = cur.execute(f'SELECT * FROM goods where goodtypeid = {typek}')
            for x in result:
                item = Good(x[0], x[1], x[2])
                self.goods.append(item)
                self.ui.listWidgetGoods.addItem(x[1])

        # # Вывод результатов на экран
        #     for elem in result:



        con.close()

    def load_market_places(self):
        self.ui.listWidgetRealMarkets.clear()
        con = sqlite3.connect("data/my_market_db")
        type = self.ui.cmbMarkets.currentText()
        print(type)
        # Создание курсора
        cur = con.cursor()
        if type == 'Все':
            # Выполнение запроса и получение всех результатов
            result = cur.execute("SELECT * FROM marketplaces").fetchall()
        else:
            typek = 0
            for x in self.markets:
                if type == x.marketname:
                    typek = x.id
            print(typek)
            result = cur.execute(f'SELECT * FROM marketplaces where MarketId = {typek}')


        for x in result:
            item = MarketPlace(x[0], x[1], x[2], x[3], x[4])
            self.marketplaces.append(item)
            self.ui.listWidgetRealMarkets.addItem(x[2])

        # # Вывод результатов на экран
        #     for elem in result:

        con.close()




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

    def show_map(self, coords):
        if len(coords) == 1:
            ll = coords
            print(ll)
        # if ll[0]:
        #     self.spinbox_longitude.setValue(ll[0])
        #     self.spinbox_lattitude.setValue(ll[1])
            z = self.ui.spinBoxScale.value()
            if os._exists("map.png"):
                os.remove("map.png")
            map = return_map(ll, "map", SCREEN_SIZE, z)
        else:
            ll, spn = coords
            if os._exists("map.png"):
                os.remove("map.png")
            map = return_map(ll, "map", SCREEN_SIZE, z=13, spn=spn)
        # Отображаем содержимое QPixmap в объекте QLabel
        ## Изображение
        self.pixmap = QPixmap(map)
        # Если картинки нет, то QPixmap будет пустым,
        # а исключения не будет
        self.ui.image.setPixmap(self.pixmap)



def geocode(address):
    # Собираем запрос для геокодера.
    geocoder_request = f"http://geocode-maps.yandex.ru/1.x/"
    geocoder_params = {
        "apikey": API_KEY,
        "geocode": address,
        "format": "json"}

    # Выполняем запрос.
    response = requests.get(geocoder_request, params=geocoder_params)

    if response:
        # Преобразуем ответ в json-объект
        json_response = response.json()
    else:
        raise RuntimeError(
            f"""Ошибка выполнения запроса:
            {geocoder_request}
            Http статус: {response.status_code} ({response.reason})""")

    # Получаем первый топоним из ответа геокодера.
    # Согласно описанию ответа он находится по следующему пути:
    features = json_response["response"]["GeoObjectCollection"]["featureMember"]
    return features[0]["GeoObject"] if features else None


def return_map(ll=None, map_type="map", size=(450, 450), z=13, spn=None):
    s = ','.join([str(x) for x in size])
    if ll and spn:
        map_request = f"http://static-maps.yandex.ru/1.x/?ll={ll[0]},{ll[1]}&l={map_type}&size={s}&spn={spn}"
    elif ll and spn == None:
        map_request = f"http://static-maps.yandex.ru/1.x/?ll={ll[0]},{ll[1]}&l={map_type}&size={s}&z={z}"
    elif ll == None and spn:
        map_request = f"http://static-maps.yandex.ru/1.x/?l={map_type}&size={s}&spn={spn}"
    else:
        map_request = f"http://static-maps.yandex.ru/1.x/?l={map_type}&size={s}&z={z}"

    response = requests.get(map_request)

    if not response:
        print("Ошибка выполнения запроса:")
        print(map_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")
        sys.exit(1)

    # Запишем полученное изображение в файл.
    map_file = "map.png"
    try:
        with open(map_file, "wb") as file:
            file.write(response.content)
    except IOError as ex:
        print("Ошибка записи временного файла:", ex)
        sys.exit(2)

    return map_file


# Получаем координаты объекта по его адресу.
def get_coordinates(address):
    toponym = geocode(address)
    if not toponym:
        return None, None

    # Координаты центра топонима:
    toponym_coodrinates = toponym["Point"]["pos"]
    # Широта, преобразованная в плавающее число:
    toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")
    return float(toponym_longitude), float(toponym_lattitude)

# Получаем параметры объекта для рисования карты вокруг него.
def get_ll_span(address):
    toponym = geocode(address)
    if not toponym:
        return (None, None)

    # Координаты центра топонима:
    toponym_coodrinates = toponym["Point"]["pos"]
    # Долгота и Широта :
    toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")

    # Собираем координаты в параметр ll
    ll = ",".join([toponym_longitude, toponym_lattitude])

    # Рамка вокруг объекта:
    envelope = toponym["boundedBy"]["Envelope"]

    # левая, нижняя, правая и верхняя границы из координат углов:
    l, b = envelope["lowerCorner"].split(" ")
    r, t = envelope["upperCorner"].split(" ")

    # Вычисляем полуразмеры по вертикали и горизонтали
    dx = abs(float(l) - float(r)) / 2.0
    dy = abs(float(t) - float(b)) / 2.0

    # Собираем размеры в параметр span
    span = f"{dx},{dy}"

    return ll, span


# Находим ближайшие к заданной точке объекты заданного типа.
def get_nearest_object(point, kind):
    ll = "{0},{1}".format(point[0], point[1])
    geocoder_request = f"http://geocode-maps.yandex.ru/1.x/"
    geocoder_params = {
        "apikey": API_KEY,
        "geocode": ll,
        "format": "json"}
    if kind:
        geocoder_params['kind'] = kind
    # Выполняем запрос к геокодеру, анализируем ответ.
    response = requests.get(geocoder_request, params=geocoder_params)
    if not response:
        raise RuntimeError(
            f"""Ошибка выполнения запроса:
            {geocoder_request}
            Http статус: {response.status_code,} ({response.reason})""")

    # Преобразуем ответ в json-объект
    json_response = response.json()

    # Получаем первый топоним из ответа геокодера.
    features = json_response["response"]["GeoObjectCollection"]["featureMember"]
    return features[0]["GeoObject"]["name"] if features else None


def main():
    app = QApplication(sys.argv)
    ex = MyWidget()
    apply_stylesheet(app, theme='dark_cyan.xml')
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()


