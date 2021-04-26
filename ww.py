import os
import sys
import requests

from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QSpinBox, QDoubleSpinBox, QComboBox

SCREEN_SIZE = [650, 450]
STEP = 1
API_KEY = '40d1649f-0493-4b70-98ba-98533de7710b'


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


def return_map(ll=None, map_type="map", size=(450, 450), z=13):
    s = ','.join([str(x) for x in size])
    if ll:
        map_request = f"http://static-maps.yandex.ru/1.x/?ll={ll[0]},{ll[1]}&l={map_type}&size={s}&z={z}"
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


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def show_map(self, coords):
        ll = coords
        print(ll)
        if ll[0]:
            self.spinbox_longitude.setValue(ll[0])
            self.spinbox_lattitude.setValue(ll[1])
        z = self.spinbox.value()
        if os._exists("map.png"):
            os.remove("map.png")
        map = return_map(ll, "map", SCREEN_SIZE, z)
        # Отображаем содержимое QPixmap в объекте QLabel
        ## Изображение
        self.pixmap = QPixmap(map)
        # Если картинки нет, то QPixmap будет пустым,
        # а исключения не будет
        self.image.setPixmap(self.pixmap)

    def initUI(self):
        self.setGeometry(400, 400, 770, 470)
        self.setWindowTitle('Карта')

        self.label = QLabel(self)
        self.label.move(5, 5)
        self.label.setText("Масштаб")

        self.spinbox = QSpinBox(self)
        self.spinbox.setRange(1, 17)
        self.spinbox.setValue(10)
        self.spinbox.move(5, 30)
        self.spinbox.setFocusPolicy(0)

        self.label = QLabel(self)
        self.label.move(5, 60)
        self.label.setText("Шаг")

        self.combo = QComboBox(self)
        self.combo.addItems(["10", "1",
                             "0.1", "0.01", "0.001", "0.0001", "0.00001", "0.000001"])
        self.combo.move(5, 90)
        self.combo.activated[str].connect(self.onActivated)
        self.combo.setFocusPolicy(0)

        self.label1 = QLabel(self)
        self.label1.move(5, 120)
        self.label1.setText("Долгота")

        self.spinbox_longitude = QDoubleSpinBox(self)
        self.spinbox_longitude.setRange(-180, 180)
        self.spinbox_longitude.move(5, 150)
        self.spinbox_longitude.setDecimals(7)
        self.spinbox_longitude.setFocusPolicy(0)
        self.spinbox_longitude.valueChanged.connect(self.valuechange)

        self.label2 = QLabel(self)
        self.label2.move(5, 180)
        self.label2.setText("Широта")

        self.spinbox_lattitude = QDoubleSpinBox(self)
        self.spinbox_lattitude.setRange(-90, 90)
        self.spinbox_lattitude.move(5, 210)
        self.spinbox_lattitude.setDecimals(7)

        self.spinbox_lattitude.setFocusPolicy(0)
        self.spinbox_lattitude.valueChanged.connect(self.valuechange)

        self.image = QLabel(self)
        self.image.move(110, 5)
        self.image.resize(*SCREEN_SIZE)
        self.show_map(get_coordinates("Зеленодольск, ул.Карла-Маркса, 7"))

        self.spinbox.valueChanged.connect(self.valuechange)

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

    def valuechange(self):
        coords = self.spinbox_longitude.value(), self.spinbox_lattitude.value()
        self.show_map(coords)

    def onActivated(self, text):
        x = float(text)
        self.spinbox_longitude.setSingleStep(x)
        self.spinbox_lattitude.setSingleStep(x)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
class MainWindowPage(QMainWindow, Ui_MainWindow):
    def __init__(self, *args):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.labelUserName.setText(args[-1])
        self.ui.statusbar.showMessage(args[-1])

        self.label = QLabel(self)
        self.label.move(5, 5)
        self.label.setText("Масштаб")

        self.spinbox = QSpinBox(self)
        self.spinbox.setRange(1, 17)
        self.spinbox.setValue(10)
        self.spinbox.move(5, 30)
        self.spinbox.setFocusPolicy(0)

        self.label = QLabel(self)
        self.label.move(5, 60)
        self.label.setText("Шаг")

        self.combo = QComboBox(self)
        self.combo.addItems(["10", "1",
                             "0.1", "0.01", "0.001", "0.0001", "0.00001", "0.000001"])
        self.combo.move(5, 90)
        self.combo.activated[str].connect(self.onActivated)
        self.combo.setFocusPolicy(0)

        self.label1 = QLabel(self)
        self.label1.move(5, 120)
        self.label1.setText("Долгота")

        self.spinbox_longitude = QDoubleSpinBox(self)
        self.spinbox_longitude.setRange(-180, 180)
        self.spinbox_longitude.move(5, 150)
        self.spinbox_longitude.setDecimals(7)
        self.spinbox_longitude.setFocusPolicy(0)
        self.spinbox_longitude.valueChanged.connect(self.valuechange)

        self.label2 = QLabel(self)
        self.label2.move(5, 180)
        self.label2.setText("Широта")

        self.spinbox_lattitude = QDoubleSpinBox(self)
        self.spinbox_lattitude.setRange(-90, 90)
        self.spinbox_lattitude.move(5, 210)
        self.spinbox_lattitude.setDecimals(7)

        self.spinbox_lattitude.setFocusPolicy(0)
        self.spinbox_lattitude.valueChanged.connect(self.valuechange)

        self.image = (self)
        self.image.move(110, 5)
        self.image.resize(*SCREEN_SIZE)
        self.show_map(get_coordinates("Зеленодольск, ул.Карла-Маркса, 7"))

        self.spinbox.valueChanged.connect(self.valuechange)

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

    def valuechange(self):
        coords = self.spinbox_longitude.value(), self.spinbox_lattitude.value()
        self.show_map(coords)

    def onActivated(self, text):
        x = float(text)
        self.spinbox_longitude.setSingleStep(x)
        self.spinbox_lattitude.setSingleStep(x)

    def show_map(self, coords):
        ll = coords
        print(ll)
        if ll[0]:
            self.spinbox_longitude.setValue(ll[0])
            self.spinbox_lattitude.setValue(ll[1])
        z = self.spinbox.value()
        if os._exists("map.png"):
            os.remove("map.png")
        map = return_map(ll, "map", SCREEN_SIZE, z)
        # Отображаем содержимое QPixmap в объекте QLabel
        ## Изображение
        self.pixmap = QPixmap(map)
        # Если картинки нет, то QPixmap будет пустым,
        # а исключения не будет
        self.image.setPixmap(self.pixmap)



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


def return_map(ll=None, map_type="map", size=(450, 450), z=13):
    s = ','.join([str(x) for x in size])
    if ll:
        map_request = f"http://static-maps.yandex.ru/1.x/?ll={ll[0]},{ll[1]}&l={map_type}&size={s}&z={z}"
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




