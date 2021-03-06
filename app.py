import os
import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QLabel, QMainWindow, QDialog, QAction, QTableWidgetItem
from PyQt5.QtGui import QPixmap
from windows.authpage import Ui_Form
from check_db import *
from windows.mainwindowpage import Ui_MainWindow
from windows.goodwindow import Ui_GoodDialog
from windows.marketwindow import Ui_MarketDialog
from windows.goodtypewindow import Ui_GoodTypeDialog
from windows.marketplacewindow import Ui_MarketPlaceDialog
from windows.goodmarketwindow import Ui_GoodMarketDialog
from qt_material import apply_stylesheet
from data.models import Good, GoodType, Market, MarketPlace

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

        return wrapper

    @check_input
    def auth(self):
        ## print(1)
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
            QMessageBox.about(self, 'Оповещение', "Вы вошли как администратор")
            self.second_form = MainWindowPage(self, 'admin')
            self.hide()
            self.second_form.show()
        elif value == '-1':
            QMessageBox.about(self, 'Оповещение', "Вы вошли как пользователь")
            self.second_form = MainWindowPage(self, 'user')
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
   

class MainWindowPage(QMainWindow, Ui_MainWindow):
    def __init__(self, *args):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.statusbarX.showMessage(args[-1])
        if args[-1] == 'user':
            self.ui.menubar.setVisible(False)

        # список магазинов
        self.markets = []
        # список категорий товаров
        self.goodtypes = []
        # список товаров
        self.goods = []
        # список адресов
        self.marketplaces = []
        # список товаров в магазинах и цены
        self.goodmarkets = []
        # загрузка списка магазинов в комбобокс
        self.load_markets()
        # загрузка категорий в комбобокс
        self.load_goodtypes()
        # id выбранного товара
        self.goodid = None
        # id выбранного магазина
        self.marketid = None
        # id выбранного адреса
        self.marketplaceid = None
        # id выбранной категории
        self.goodtypeid = None
        self.address = None

        self.show_map(get_ll_span("Зеленодольск, ул.Карла-Маркса, 7"))
        self.ui.cmbGoodTypes.currentTextChanged.connect(self.load_goods)
        self.ui.cmbMarkets.currentTextChanged.connect(self.load_market_places)
        self.ui.btnSearch.clicked.connect(self.search_goods)
        self.ui.listWidgetPrices.itemSelectionChanged.connect(self.set_address)
        self.ui.listWidgetRealMarkets.itemSelectionChanged.connect(self.set_marketplace)
        self.ui.listWidgetGoods.itemSelectionChanged.connect(self.set_good)
        self.ui.btnShowMarket.clicked.connect(self.show_market)
        # self.ui.mnuGoods.triggered.connect(self.open_good_window)
        openGoodsAction = QAction("Товары", self)
        openGoodsAction.triggered.connect(self.open_good_window)
        self.ui.mnuGoods.addAction(openGoodsAction)
        openGoodTypesAction = QAction("Категории", self)
        openGoodTypesAction.triggered.connect(self.open_good_type_window)

        self.ui.mnuGoods.addAction(openGoodTypesAction)

        openGoodMarketsAction = QAction("Точки продаж", self)
        openGoodMarketsAction.triggered.connect(self.open_good_market_window)

        self.ui.mnuGoods.addAction(openGoodMarketsAction)

        openMarketsAction = QAction('Магазины', self)
        openMarketsAction.triggered.connect(self.open_market_window)

        self.ui.mnuMarkets.addAction(openMarketsAction)

        openAddressAction = QAction('Адреса', self)
        openAddressAction.triggered.connect(self.open_address_window)

        self.ui.mnuMarkets.addAction(openAddressAction)
        self.load_goods()
        self.load_market_places()
        # self.open_good_window()

    def open_good_window(self):
        self.new_form = GoodWindow()
        self.new_form.show()
        #self.load_goods()

    def open_good_type_window(self):
        self.new_form = GoodTypeWindow()
        self.new_form.show()
        #self.load_goodtypes()

    def open_market_window(self):
        self.new_form = MarketWindow()
        self.new_form.show()
        #self.load_markets()

    def open_address_window(self):
        self.new_form = MarketPlacesWindow()
        self.new_form.show()
        #self.load_market_places()

    def open_good_market_window(self):
        self.new_form = GoodMarketWindow()
        self.new_form.show()

    def show_market(self):
        # self.new_form = GoodWindow()
        # self.new_form.show()
        #
        if self.address:
            self.show_map(get_ll_span(f"Республика Татарстан, г.Зеленодольск, {self.address}"))

    def set_address(self):
        self.address = None
        if self.ui.listWidgetPrices.currentItem().text():
            address = str(self.ui.listWidgetPrices.currentItem().text().split('(')[1:])

            i = address.find(',')

            # address = address.split(',')
            self.address = address[i + 1:-3]
            # print(self.address)

    def set_marketplace(self):
        self.marketplaceid = None
         # print(self.ui.listWidgetRealMarkets.currentItem().text())
        if self.ui.listWidgetRealMarkets.currentItem().text():
            for x in self.marketplaces:
                if x.address == self.ui.listWidgetRealMarkets.currentItem().text():
                    self.marketplaceid = x.id

        # print(self.marketplaceid)

    def set_good(self):
        self.goodid = None
        # # print(self.ui.listWidgetRealMarkets.currentItem().text())
        if self.ui.listWidgetGoods.currentItem().text():
            for x in self.goods:
                # print(x.goodname)
                if x.goodname == self.ui.listWidgetGoods.currentItem().text():
                    self.goodid = x.id

        # print(self.goodid)

    def search_goods(self):
        self.ui.listWidgetPrices.clear()
        if self.goodid and self.marketplaceid:
            con = sqlite3.connect("data/my_market_db")
            # Создание курсора
            cur = con.cursor()
            result = cur.execute(f"""
                        SELECT Goods.Id as GoodId, 
                        Goods.GoodName,
                        Markets.Id as MarketId,
                        Markets.MarketName, 
                        Marketplaces.Id as MarketPlaceId,
                        Marketplaces.Address , GoodMarkets.Price   
                        from Goods
                        inner join GoodMarkets on goodmarkets.GoodId = goods.Id 
                        inner join Marketplaces on goodmarkets.MarketPlaceId == Marketplaces.Id 
                        Inner join markets on markets.Id == Marketplaces.MarketId
                        where goodmarkets.GoodId = {self.goodid}  and goodmarkets.MarketPlaceId = {self.marketplaceid} 
                        order by Goods.GoodName
                        """).fetchall()
        elif self.goodid and self.marketplaceid is None:
            if self.marketid is None:
                con = sqlite3.connect("data/my_market_db")
                # Создание курсора
                cur = con.cursor()
                result = cur.execute(f"""
                                        SELECT Goods.Id as GoodId, 
                                        Goods.GoodName,
                                        Markets.Id as MarketId,
                                        Markets.MarketName, 
                                        Marketplaces.Id as MarketPlaceId,
                                        Marketplaces.Address, 
                                        GoodMarkets.Price  
                                        from Goods
                                        inner join GoodMarkets on goodmarkets.GoodId = goods.Id 
                                        inner join Marketplaces on goodmarkets.MarketPlaceId == Marketplaces.Id 
                                        Inner join markets on markets.Id == Marketplaces.MarketId
                                        where goodmarkets.GoodId = {self.goodid}  
                                        order by Goods.GoodName
                                        """).fetchall()
            else:
                con = sqlite3.connect("data/my_market_db")
                # Создание курсора
                cur = con.cursor()
                result = cur.execute(f"""
                                SELECT Goods.Id as GoodId, 
                               Goods.GoodName,
                                Markets.Id as MarketId,
                               Markets.MarketName, 
                              Marketplaces.Id as MarketPlaceId,
                             Marketplaces.Address, 
                             GoodMarkets.Price  
                            from Goods
                              inner join GoodMarkets on goodmarkets.GoodId = goods.Id 
                            inner join Marketplaces on goodmarkets.MarketPlaceId == Marketplaces.Id 
                                Inner join markets on markets.Id == Marketplaces.MarketId
                       where goodmarkets.GoodId = {self.goodid} and Marketplaces.marketid = {self.marketid}
                        order by Goods.GoodName
                        """).fetchall()
        elif self.goodid is None and self.marketplaceid:
            if self.goodtypeid is None:
                con = sqlite3.connect("data/my_market_db")
                # Создание курсора
                cur = con.cursor()
                result = cur.execute(f"""
                                        SELECT Goods.Id as GoodId, 
                                        Goods.GoodName,
                                        Markets.Id as MarketId,
                                        Markets.MarketName, 
                                        Marketplaces.Id as MarketPlaceId,
                                        Marketplaces.Address, 
                                            GoodMarkets.Price  
                                        from Goods
                                        inner join GoodMarkets on goodmarkets.GoodId = goods.Id 
                                        inner join Marketplaces on goodmarkets.MarketPlaceId == Marketplaces.Id 
                                        Inner join markets on markets.Id == Marketplaces.MarketId
                                        where goodmarkets.MarketPlaceId = {self.marketplaceid} 
                                        order by Goods.GoodName
                                        """).fetchall()
            else:
                con = sqlite3.connect("data/my_market_db")
                # Создание курсора
                cur = con.cursor()
                result = cur.execute(f"""
                SELECT Goods.Id as GoodId, 
                Goods.GoodName,
                Markets.Id as MarketId,
                  Markets.MarketName, 
                  Marketplaces.Id as MarketPlaceId,
                    Marketplaces.Address, 
                     GoodMarkets.Price  
                   from Goods
                    inner join GoodMarkets on goodmarkets.GoodId = goods.Id 
                        inner join Marketplaces on goodmarkets.MarketPlaceId == Marketplaces.Id 
                        Inner join markets on markets.Id == Marketplaces.MarketId
                    where goodmarkets.MarketPlaceId = {self.marketplaceid} 
                    and goods.goodtypeid = {self.goodtypeid} 
                            order by Goods.GoodName
                                    """).fetchall()
        else:
            if self.goodtypeid is None and self.marketid is None:
                con = sqlite3.connect("data/my_market_db")
                # Создание курсора
                cur = con.cursor()
                result = cur.execute("""
                SELECT Goods.Id as GoodId, 
                Goods.GoodName,
                Markets.Id as MarketId,
                Markets.MarketName, 
                Marketplaces.Id as MarketPlaceId,
                Marketplaces.Address, 
                GoodMarkets.Price 
                from Goods
                inner join GoodMarkets on goodmarkets.GoodId = goods.Id 
                inner join Marketplaces on goodmarkets.MarketPlaceId == Marketplaces.Id 
                Inner join markets on markets.Id == Marketplaces.MarketId
                order by Goods.GoodName
                """).fetchall()
            elif self.goodtypeid and self.marketid is None:
                con = sqlite3.connect("data/my_market_db")
                # Создание курсора
                cur = con.cursor()
                result = cur.execute(f"""
                                SELECT Goods.Id as GoodId, 
                                Goods.GoodName,
                                Markets.Id as MarketId,
                                Markets.MarketName, 
                                Marketplaces.Id as MarketPlaceId,
                                Marketplaces.Address, 
                                GoodMarkets.Price 
                                from Goods
                                inner join GoodMarkets on goodmarkets.GoodId = goods.Id 
                                inner join Marketplaces on goodmarkets.MarketPlaceId == Marketplaces.Id 
                                Inner join markets on markets.Id == Marketplaces.MarketId
                                where goods.goodtypeid = {self.goodtypeid} 
                                order by Goods.GoodName
                                """).fetchall()
            elif self.goodtypeid is None and self.marketid:
                con = sqlite3.connect("data/my_market_db")
                # Создание курсора
                cur = con.cursor()
                result = cur.execute(f"""
                                SELECT Goods.Id as GoodId, 
                                Goods.GoodName,
                                Markets.Id as MarketId,
                                Markets.MarketName, 
                                Marketplaces.Id as MarketPlaceId,
                                Marketplaces.Address, 
                                GoodMarkets.Price 
                                from Goods
                                inner join GoodMarkets on goodmarkets.GoodId = goods.Id 
                                inner join Marketplaces on goodmarkets.MarketPlaceId == Marketplaces.Id 
                                Inner join markets on markets.Id == Marketplaces.MarketId
                                where Marketplaces.MarketId = {self.marketid}  
                                order by Goods.GoodName
                                """).fetchall()
            else:
                con = sqlite3.connect("data/my_market_db")
                # Создание курсора
                cur = con.cursor()
                result = cur.execute(f"""
                                                SELECT Goods.Id as GoodId, 
                                                Goods.GoodName,
                                                Markets.Id as MarketId,
                                                Markets.MarketName, 
                                                Marketplaces.Id as MarketPlaceId,
                                                Marketplaces.Address, 
                                                GoodMarkets.Price 
                                                from Goods
                                                inner join GoodMarkets on goodmarkets.GoodId = goods.Id 
                                                inner join Marketplaces on goodmarkets.MarketPlaceId == Marketplaces.Id 
                                                Inner join markets on markets.Id == Marketplaces.MarketId
                                                where goods.goodtypeid = {self.goodtypeid} and Marketplaces.MarketId = {self.marketid}  
                                                order by Goods.GoodName
                                                """).fetchall()

        for elem in result:
            self.ui.listWidgetPrices.addItem(f' {elem[1]} {elem[6]} руб. ({elem[3]}, {elem[5]})')
            # print(elem)


        # print(self.markets)

        con.close()

    # список магазинов
    def load_markets(self):
        #self.ui.cmbMarkets.clear()
        self.marketplaceid = None
        con = sqlite3.connect("data/my_market_db")
        # Создание курсора
        cur = con.cursor()

        # Выполнение запроса и получение всех результатов
        result = cur.execute("SELECT * FROM markets").fetchall()
        # g = Market(0, 'Все', '1')
        self.ui.cmbMarkets.addItem('Все')
        # Вывод результатов на экран
        for elem in result:
            self.ui.cmbMarkets.addItem(elem[1])
            market = Market(elem[0], elem[1])
            self.markets.append(market)

        # print(self.markets)

        con.close()

    # список типов продуктов
    def load_goodtypes(self):
        self.goodtypes = []
        #self.ui.cmbGoodTypes.clear()
        con = sqlite3.connect("data/my_market_db")
        # Создание курсора
        cur = con.cursor()

        # Выполнение запроса и получение всех результатов
        result = cur.execute("SELECT * FROM goodtypes").fetchall()

        self.ui.cmbGoodTypes.addItem('Все')

        # Вывод результатов на экран
        for elem in result:
            self.ui.cmbGoodTypes.addItem(elem[1])
            item = GoodType(elem[0], elem[1])
            self.goodtypes.append(item)

        con.close()

    # список продуктов
    def load_goods(self):
        self.goodid = None
        self.goodtypeid = None
        self.goods = []
        self.ui.listWidgetGoods.clear()
        con = sqlite3.connect("data/my_market_db")
        type = self.ui.cmbGoodTypes.currentText()
        # print(type)
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
            # print(typek)
            result = []
            self.goodtypeid = typek
            result = cur.execute(f'SELECT * FROM goods where goodtypeid = {typek}')

        for x in result:
            item = Good(x[0], x[1], x[2])
            self.goods.append(item)
            self.ui.listWidgetGoods.addItem(x[1])
        # print(self.goods)
        con.close()

    def load_market_places(self):
        self.marketplaceid = None
        self.ui.listWidgetRealMarkets.clear()
        con = sqlite3.connect("data/my_market_db")
        type = self.ui.cmbMarkets.currentText()
        # print(type)
        # Создание курсора
        cur = con.cursor()
        if type == 'Все':
            # Выполнение запроса и получение всех результатов
            result = cur.execute("SELECT * FROM marketplaces").fetchall()
            self.marketid = None
        else:
            typek = 0
            for x in self.markets:
                if type == x.marketname:
                    typek = x.id
            # print(typek)
            self.marketid = typek
            result = cur.execute(f'SELECT * FROM marketplaces where MarketId = {typek}')

        for x in result:
            item = MarketPlace(x[0], x[1], x[2])
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
        # # print("pressed key " + str(event.key()))

    def show_map(self, coords):
        if len(coords) == 2:
            ll = coords
            # print(ll)
            # if ll[0]:
            #     self.spinbox_longitude.setValue(ll[0])
            #     self.spinbox_lattitude.setValue(ll[1])
            z = self.ui.spinBoxScale.value()
            if os._exists("map.png"):
                os.remove("map.png")
            map = return_map(ll, "map", SCREEN_SIZE, z)
        else:
            ll, spn = coords[:2], coords[2:]
            # print(ll, spn)
            if os._exists("map.png"):
                os.remove("map.png")
            map = return_map(ll, "map", SCREEN_SIZE, z=13, spn=spn)
        # Отображаем содержимое QPixmap в объекте QLabel
        ## Изображение
        self.pixmap = QPixmap(map)
        # Если картинки нет, то QPixmap будет пустым,
        # а исключения не будет
        self.ui.image.setPixmap(self.pixmap)


class GoodWindow(QDialog, Ui_GoodDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.modified = {}
        self.goodtypes = {}
        self.setModal(True)
        self.titles = None
        self.goodid = None
        self.goodtypeid = None
        self.load_data()
        self.load_goodtypes()
        self.tableWidgetGoods.itemSelectionChanged.connect(self.get_item)
        self.tableWidgetGoods.itemClicked.connect(self.get_item)
        self.cmbGoodType.currentTextChanged.connect(self.set_goodtypeid)
        self.btnUpdate.clicked.connect(self.update_result)
        self.btnSave.clicked.connect(self.save_results)
        self.btnDelete.clicked.connect(self.delete_result)

        # список продуктов

    def set_goodtypeid(self):
        self.goodtypeid = None
        if self.goodtypes:
            type = self.cmbGoodType.currentText()
            self.goodtypeid = self.goodtypes.get(type, None)

        # список типов продуктов

    def load_goodtypes(self):

        con = sqlite3.connect("data/my_market_db")
        # Создание курсора
        cur = con.cursor()

        # Выполнение запроса и получение всех результатов
        result = cur.execute("SELECT * FROM goodtypes").fetchall()

        # Вывод результатов на экран
        for elem in result:
            self.cmbGoodType.addItem(elem[1])
            self.goodtypes[elem[1]] = elem[0]

        con.close()

    def get_item(self):
        self.goodid = None
        k = self.tableWidgetGoods.currentItem().row()
        if k:
            self.goodid = int(self.tableWidgetGoods.item(k, 0).text())
            self.lineEditGoodName.setText(self.tableWidgetGoods.item(k, 1).text())
            self.cmbGoodType.setCurrentText(self.tableWidgetGoods.item(k, 2).text())
            # print(self.tableWidgetGoods.item(k, 0).text(), self.tableWidgetGoods.item(k, 1).text(),
            #self.tableWidgetGoods.item(k, 2).text())

    def load_data(self):
        con = sqlite3.connect("data/my_market_db")
        cur = con.cursor()

        result = cur.execute("""SELECT Goods.Id as id, Goods.GoodName as Название, GoodTypes.GoodTypeName as Категория 
        from goods inner join GoodTypes on goods.GoodTypeId = goodtypes.Id """).fetchall()

        self.tableWidgetGoods.setRowCount(len(result))

        self.tableWidgetGoods.setColumnCount(len(result[0]))
        self.titles = [description[0] for description in cur.description]
        self.tableWidgetGoods.setHorizontalHeaderLabels(self.titles)
        headers = self.tableWidgetGoods.horizontalHeader()
        headers.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        headers.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        headers.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        # Заполнили таблицу полученными элементами
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                # print(val, end='\t')
                item = QTableWidgetItem(str(val))
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.tableWidgetGoods.setItem(i, j, item)
            # print()
        self.modified = {}

        con.close()

    def update_result(self):
        con = sqlite3.connect("data/my_market_db")
        cur = con.cursor()
        if (self.lineEditGoodName.text()) and self.goodtypeid and self.goodid:
            ## print(self.lineEditGoodName.text(), self.goodtypeid, self.goodid)
            que = f"""UPDATE goods SET GoodName='{self.lineEditGoodName.text()}', 
                          GoodTypeId={self.goodtypeid} WHERE Id= {self.goodid};"""
            cur.execute(que)
            con.commit()
            ## print('updated')
            self.load_data()
            con.close()
        else:
            return

    def delete_result(self, item):

        if self.goodid:
            ## print(self.lineEditGoodName.text(), self.goodtypeid)
            ret = QMessageBox.question(self, '', "Вы действительно хотите удалить запись?",
                                       QMessageBox.Yes | QMessageBox.No)

            if ret == QMessageBox.Yes:
                con = sqlite3.connect("data/my_market_db")
                cur = con.cursor()
                result = int(list(cur.execute(
                    f"Select Count(GoodId) from GoodMarkets where GoodMarkets.GoodId = {self.goodid}"))[0][
                                 0])
                if result > 0:
                    QMessageBox.critical(self, 'Ошибка', "есть связанные записи")
                    return

                que = f"""DELETE FROM Goods WHERE Id= {self.goodid};"""
                cur.execute(que)
                con.commit()
                ## print('deleted')
                con.close()
                self.load_data()
            else:
                return

    def save_results(self):
        con = sqlite3.connect("data/my_market_db")
        cur = con.cursor()

        if (self.lineEditGoodName.text()) and self.goodtypeid:
            # print(self.lineEditGoodName.text(), self.goodtypeid)
            goodname = self.lineEditGoodName.text()
            result = int(list(cur.execute(
                f"Select Count(GoodName) from Goods where goods.GoodName = '{self.lineEditGoodName.text()}'"))[0][0])
            if result > 0:
                QMessageBox.about(self, 'Ошибка', "Такой товар уже существует")
                return
            cur = con.cursor()
            que = f"""INSERT INTO Goods (goodname, goodtypeid) 
                           VALUES ('{goodname}',{self.goodtypeid})"""
            cur.execute(que)
            con.commit()
            # print('inserted')
            con.close()
            self.load_data()
        else:
            con.close()
            return


class MarketWindow(QDialog, Ui_MarketDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.modified = {}
        self.markets = {}
        self.setModal(True)
        self.titles = None
        self.marketid = None
        self.load_data()
        self.tableWidgetMarkets.itemSelectionChanged.connect(self.get_item)
        self.tableWidgetMarkets.itemClicked.connect(self.get_item)
        self.btnUpdate.clicked.connect(self.update_result)
        self.btnSave.clicked.connect(self.save_results)
        self.btnDelete.clicked.connect(self.delete_result)

    def get_item(self):
        self.marketid = None
        k = self.tableWidgetMarkets.currentItem().row()
        if k:
            self.marketid = int(self.tableWidgetMarkets.item(k, 0).text())
            self.lineEditGoodName.setText(self.tableWidgetMarkets.item(k, 1).text())
        # print(self.tableWidgetMarkets.item(k, 0).text(), self.tableWidgetMarkets.item(k, 1).text())

    def load_data(self):
        con = sqlite3.connect("data/my_market_db")
        cur = con.cursor()

        result = cur.execute("""SELECT Markets.Id as id, Markets.MarketName as Название From Markets""").fetchall()

        self.tableWidgetMarkets.setRowCount(len(result))

        self.tableWidgetMarkets.setColumnCount(len(result[0]))
        self.titles = [description[0] for description in cur.description]
        self.tableWidgetMarkets.setHorizontalHeaderLabels(self.titles)
        headers = self.tableWidgetMarkets.horizontalHeader()
        headers.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        headers.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)

        # Заполнили таблицу полученными элементами
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                # print(val, end='\t')
                item = QTableWidgetItem(str(val))
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.tableWidgetMarkets.setItem(i, j, item)
            # print()
        self.modified = {}

        con.close()

    def update_result(self):
        con = sqlite3.connect("data/my_market_db")
        cur = con.cursor()
        if (self.lineEditGoodName.text()) and self.marketid:
            # print(self.lineEditGoodName.text(), self.marketid)
            que = f"""UPDATE Markets SET MarketName='{self.lineEditGoodName.text()}'
                           WHERE Id= {self.marketid};"""
            cur.execute(que)
            con.commit()
            # print('updated')
            self.load_data()
            con.close()
        else:
            return

    def delete_result(self):

        if self.marketid:
            # print(self.lineEditGoodName.text(), self.marketid)
            ret = QMessageBox.question(self, '', "Вы действительно хотите удалить запись?",
                                       QMessageBox.Yes | QMessageBox.No)

            if ret == QMessageBox.Yes:
                con = sqlite3.connect("data/my_market_db")
                cur = con.cursor()
                result = int(list(cur.execute(
                    f"Select Count(MarketId) from MarketPlaces where MarketPlaces.MarketId = {self.marketid}"))[0][
                                 0])
                if result > 0:
                    QMessageBox.critical(self, 'Ошибка', "есть связанные записи")
                    return

                que = f"""DELETE FROM Markets WHERE Id= {self.marketid};"""
                cur.execute(que)
                con.commit()
                # print('deleted')
                con.close()
                self.load_data()
            else:
                return

    def save_results(self):
        con = sqlite3.connect("data/my_market_db")
        cur = con.cursor()

        if (self.lineEditGoodName.text()):
            # print(self.lineEditGoodName.text())
            marketname = self.lineEditGoodName.text()
            result = int(list(cur.execute(
                f"Select Count(MarketName) from Markets where Markets.MarketName = '{self.lineEditGoodName.text()}'"))[0][0])
            if result > 0:
                QMessageBox.about(self, 'Ошибка', "Такой магазин уже существует")
                return
            cur = con.cursor()
            que = f"""INSERT INTO markets (MarketName)
                           VALUES ('{marketname}')"""
            cur.execute(que)
            con.commit()
            # print('inserted')
            con.close()
            self.load_data()
        else:
            con.close()
            return

class MarketPlacesWindow(QDialog, Ui_MarketPlaceDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.modified = {}
        self.markets = {}
        self.setModal(True)
        self.titles = None
        self.marketplaceid = None
        self.marketid = None
        self.load_data()
        self.load_markets()
        self.tableWidget.itemSelectionChanged.connect(self.get_item)
        self.tableWidget.itemClicked.connect(self.get_item)
        self.cmbMarket.currentTextChanged.connect(self.set_marketid)
        self.btnUpdate.clicked.connect(self.update_result)
        self.btnSave.clicked.connect(self.save_results)
        self.btnDelete.clicked.connect(self.delete_result)

        # список продуктов

    def set_marketid(self):
        self.marketid = None
        if self.markets:
            type = self.cmbMarket.currentText()
            self.marketid = self.markets.get(type, None)

        # список типов продуктов

    def load_markets(self):

        con = sqlite3.connect("data/my_market_db")
        # Создание курсора
        cur = con.cursor()

        # Выполнение запроса и получение всех результатов
        result = cur.execute("SELECT * FROM markets").fetchall()

        # Вывод результатов на экран
        for elem in result:
            self.cmbMarket.addItem(elem[1])
            self.markets[elem[1]] = elem[0]

        con.close()

    def get_item(self):
        self.marketplaceid = None
        k = self.tableWidget.currentItem().row()
        if k != None:
            self.marketplaceid = int(self.tableWidget.item(k, 0).text())
            self.lineEditAddress.setText(self.tableWidget.item(k, 2).text())
            self.cmbMarket.setCurrentText(self.tableWidget.item(k, 1).text())
            # print(self.tableWidget.item(k, 0).text(), self.tableWidget.item(k, 1).text(),
             # self.tableWidget.item(k, 2).text())

    def load_data(self):
        con = sqlite3.connect("data/my_market_db")
        cur = con.cursor()

        result = cur.execute("""SELECT MarketPlaces.Id as id, Markets.MarketName as Магазин, MarketPlaces.Address as Адрес 
        from MarketPlaces inner join Markets on MarketPlaces.MarketId = Markets.Id """).fetchall()

        self.tableWidget.setRowCount(len(result))

        self.tableWidget.setColumnCount(len(result[0]))
        self.titles = [description[0] for description in cur.description]
        self.tableWidget.setHorizontalHeaderLabels(self.titles)
        headers = self.tableWidget.horizontalHeader()
        headers.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        headers.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        headers.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        # Заполнили таблицу полученными элементами
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                # print(val, end='\t')
                item = QTableWidgetItem(str(val))
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.tableWidget.setItem(i, j, item)
            # print()
        self.modified = {}

        con.close()

    def update_result(self):
        con = sqlite3.connect("data/my_market_db")
        cur = con.cursor()
        if (self.lineEditAddress.text()) and self.marketid and self.marketplaceid:
            # print(self.lineEditAddress.text(), self.marketid, self.marketplaceid)
            que = f"""UPDATE MarketPlaces SET Address='{self.lineEditAddress.text()}', 
                          MarketId={self.marketid} WHERE Id= {self.marketplaceid};"""
            cur.execute(que)
            con.commit()
            # print('updated')
            self.load_data()
            con.close()
        else:
            return

    def delete_result(self):

        if self.marketplaceid:
            # print(self.lineEditAddress.text(), self.marketid)
            ret = QMessageBox.question(self, '', "Вы действительно хотите удалить запись?",
                                       QMessageBox.Yes | QMessageBox.No)

            if ret == QMessageBox.Yes:
                con = sqlite3.connect("data/my_market_db")
                cur = con.cursor()
                result = int(list(cur.execute(
                    f"Select Count(MarketPlaceId) from GoodMarkets where GoodMarkets.MarketPlaceId = {self.marketplaceid}"))[0][
                                 0])
                if result > 0:
                    QMessageBox.critical(self, 'Ошибка', "есть связанные записи")
                    return

                que = f"""DELETE FROM GoodMarkets WHERE Id= {self.marketplaceid};"""
                cur.execute(que)
                con.commit()
                # print('deleted')
                con.close()
                self.load_data()
            else:
                return

    def save_results(self):
        con = sqlite3.connect("data/my_market_db")
        cur = con.cursor()

        if (self.lineEditAddress.text()) and self.marketid:
            # print(self.lineEditAddress.text(), self.marketid)
            name = self.lineEditAddress.text()
            result = int(list(cur.execute(
                f"""Select Count(Address) from MarketPlaces 
                where MarketPlaces.Address = '{self.lineEditAddress.text()}' and MarketPlaces.MarketId ={self.marketid}"""))[0][0])
            if result > 0:
                QMessageBox.about(self, 'Ошибка', "Такой адрес для данного магазина уже существует")
                return
            cur = con.cursor()
            que = f"""INSERT INTO MarketPlaces (marketid, address) 
                           VALUES ({self.marketid},'{name}')"""
            cur.execute(que)
            con.commit()
            # print('inserted')
            con.close()
            self.load_data()
        else:
            con.close()
            return

# товары в магазинах
class GoodMarketWindow(QDialog, Ui_GoodMarketDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.modified = {}
        self.marketplaces = {}
        self.goods = {}
        self.setModal(True)
        self.titles = None
        self.goodid = None
        self.marketplaceid = None
        self.goodmarketid = None
        self.marketid = None
        self.load_data()
        self.load_market_places()
        self.load_goods()
        self.tableWidget.itemSelectionChanged.connect(self.get_item)
        self.tableWidget.itemClicked.connect(self.get_item)
        self.cmbGoods.currentTextChanged.connect(self.set_goodid)
        self.cmbMarketPlaces.currentTextChanged.connect(self.set_marketplaceid)
        self.btnUpdate.clicked.connect(self.update_result)
        self.btnSave.clicked.connect(self.save_results)
        self.btnDelete.clicked.connect(self.delete_result)

        # список продуктов

    def set_goodid(self):
        self.goodid = None
        if self.goods:
            type = self.cmbGoods.currentText()
            self.goodid = self.goods.get(type, None)

    def set_marketplaceid(self):
        self.marketplaceid = None
        if self.marketplaces:
            type = self.cmbMarketPlaces.currentText()
            self.marketplaceid = self.marketplaces.get(type, None)

        # список типов продуктов

    def load_market_places(self):

        con = sqlite3.connect("data/my_market_db")
        # Создание курсора
        cur = con.cursor()

        # Выполнение запроса и получение всех результатов
        result = cur.execute("""SELECT MarketPlaces.Id,
         MarketPlaces.Address,
          Markets.MarketName FROM markets inner join marketplaces on MarketPlaces.MarketId = Markets.Id""").fetchall()

        # Вывод результатов на экран
        for elem in result:
            m = f"{elem[2]} ({elem[1]})"
            # print(m)
            self.cmbMarketPlaces.addItem(m)
            self.marketplaces[m] = elem[0]

        con.close()


    def load_goods(self):
        con = sqlite3.connect("data/my_market_db")
        # Создание курсора
        cur = con.cursor()
        # Выполнение запроса и получение всех результатов
        result = cur.execute("""SELECT * from goods""").fetchall()
        # Вывод результатов на экран
        for elem in result:

            self.cmbGoods.addItem(elem[1])
            self.goods[elem[1]] = elem[0]

        con.close()

    def get_item(self):
        self.goodmarketid = None
        k = self.tableWidget.currentItem().row()
        if k != None:
            self.goodmarketid = int(self.tableWidget.item(k, 0).text())
            self.cmbGoods.setCurrentText(self.tableWidget.item(k, 2).text())
            market = f"{self.tableWidget.item(k, 4).text()} ({self.tableWidget.item(k, 5).text()})"
            self.cmbMarketPlaces.setCurrentText(market)
            self.spinBoxPrice.setValue(float(self.tableWidget.item(k, 6).text()))
        # print(self.tableWidget.item(k, 0).text(), self.tableWidget.item(k, 2).text(), market)

    def load_data(self):
        con = sqlite3.connect("data/my_market_db")
        cur = con.cursor()

        result = cur.execute("""SELECT GoodMarkets.Id, 
    GoodMarkets.GoodId, 
    Goods.GoodName, 
    GoodMarkets.MarketPlaceId, 
    Markets.MarketName,
     MarketPlaces.Address, 
     GoodMarkets.Price from 
    (Goods inner join GoodMarkets on Goods.Id == GoodMarkets.GoodId)  
    inner join  (MarketPlaces inner join Markets on MarketPlaces.MarketId = Markets.Id) 
    on  GoodMarkets.MarketPlaceId == MarketPlaces.Id order by Goods.GoodName""").fetchall()

        self.tableWidget.setRowCount(len(result))

        self.tableWidget.setColumnCount(len(result[0]))
        self.titles = [description[0] for description in cur.description]
        self.tableWidget.setHorizontalHeaderLabels(self.titles)
        headers = self.tableWidget.horizontalHeader()
        headers.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget.setColumnHidden(1, True)
        headers.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.setColumnHidden(3, True)
        headers.setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
        headers.setSectionResizeMode(5, QtWidgets.QHeaderView.Stretch)
        headers.setSectionResizeMode(6, QtWidgets.QHeaderView.Stretch)

        # Заполнили таблицу полученными элементами
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                # print(val, end='\t')
                item = QTableWidgetItem(str(val))
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.tableWidget.setItem(i, j, item)
            # print()

        con.close()

    def update_result(self):
        con = sqlite3.connect("data/my_market_db")
        cur = con.cursor()
        if self.goodid and self.marketplaceid and self.goodmarketid:
            # print(self.goodid, self.marketplaceid)
            price = float(self.spinBoxPrice.value())
            que = f"""UPDATE GoodMarkets SET GoodId={self.goodid},
                          MarketPlaceId={self.marketplaceid}, Price = {price}  WHERE Id= {self.goodmarketid};"""
            cur.execute(que)
            con.commit()
            # print('updated')
            self.load_data()
            con.close()
        else:
            return

    def delete_result(self):
        if self.goodmarketid:
            # print(self.goodmarketid)
            ret = QMessageBox.question(self, '', "Вы действительно хотите удалить запись?",
                                       QMessageBox.Yes | QMessageBox.No)

            if ret == QMessageBox.Yes:
                con = sqlite3.connect("data/my_market_db")
                cur = con.cursor()


                que = f"""DELETE FROM GoodMarkets WHERE Id= {self.goodmarketid};"""
                cur.execute(que)
                con.commit()
                # print('deleted')
                con.close()
                self.load_data()
            else:
                return

    def save_results(self):

        con = sqlite3.connect("data/my_market_db")
        cur = con.cursor()

        if self.goodid and self.marketplaceid:
            # print(self.goodid, self.marketplaceid)
            price = float(self.spinBoxPrice.value())
            result = int(list(cur.execute(
                        f"""Select Count(Id) from GoodMarkets where GoodMarkets.MarketPlaceId = {self.marketplaceid}
                            and GoodMarkets.GoodId = {self.goodid}"""))[0][0])
            if result > 0:
                QMessageBox.critical(self, 'Ошибка', "такой товар уже существует")
                return
            cur = con.cursor()
            que = f"""INSERT INTO GoodMarkets (goodid, marketplaceid, price)
                           VALUES ({self.goodid},{self.marketplaceid},{price})"""
            cur.execute(que)
            con.commit()
            # print('inserted')
            con.close()
            self.load_data()
        else:
            con.close()
            return

# Категории товаров
class GoodTypeWindow(QDialog, Ui_GoodTypeDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Категории товаров")
        self.setupUi(self)
        self.modified = {}
        self.goodtypes = {}
        self.setModal(True)
        self.titles = None
        self.goodtypeid = None
        self.load_data()
        self.tableWidget.itemSelectionChanged.connect(self.get_item)
        self.tableWidget.itemClicked.connect(self.get_item)
        self.btnUpdate.clicked.connect(self.update_result)
        self.btnSave.clicked.connect(self.save_results)
        self.btnDelete.clicked.connect(self.delete_result)

    def get_item(self):
        self.goodtypeid = None
        k = self.tableWidget.currentItem().row()
        if k:
            self.goodtypeid = int(self.tableWidget.item(k, 0).text())
            self.lineEditName.setText(self.tableWidget.item(k, 1).text())
        # print(self.tableWidget.item(k, 0).text(), self.tableWidget.item(k, 1).text())

    def load_data(self):
        con = sqlite3.connect("data/my_market_db")
        cur = con.cursor()

        result = cur.execute("""SELECT GoodTypes.Id as id, GoodTypes.GoodTypeName as Категория From GoodTypes""").fetchall()

        self.tableWidget.setRowCount(len(result))

        self.tableWidget.setColumnCount(len(result[0]))
        self.titles = [description[0] for description in cur.description]
        self.tableWidget.setHorizontalHeaderLabels(self.titles)
        headers = self.tableWidget.horizontalHeader()
        headers.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        headers.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)

        # Заполнили таблицу полученными элементами
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                # print(val, end='\t')
                item = QTableWidgetItem(str(val))
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.tableWidget.setItem(i, j, item)
            # print()

        con.close()

    def update_result(self):
        con = sqlite3.connect("data/my_market_db")
        cur = con.cursor()
        if (self.lineEditName.text()) and self.goodtypeid:
            # print(self.lineEditName.text(), self.goodtypeid)
            que = f"""UPDATE GoodTypes SET GoodTypeName='{self.lineEditName.text()}'
                           WHERE Id= {self.goodtypeid};"""
            cur.execute(que)
            con.commit()
            # print('updated')
            self.load_data()
            con.close()
        else:
            return

    def delete_result(self):

        if self.goodtypeid:
            # print(self.lineEditName.text(), self.goodtypeid)
            ret = QMessageBox.question(self, '', "Вы действительно хотите удалить запись?",
                                       QMessageBox.Yes | QMessageBox.No)

            if ret == QMessageBox.Yes:
                con = sqlite3.connect("data/my_market_db")
                cur = con.cursor()
                result = int(list(cur.execute(
                    f"Select Count(GoodTypeId) from Goods where Goods.GoodTypeId = {self.goodtypeid}"))[0][
                                 0])
                if result > 0:
                    QMessageBox.critical(self, 'Ошибка', "есть связанные записи")
                    return

                que = f"""DELETE FROM GoodTypes WHERE Id= {self.goodtypeid};"""
                cur.execute(que)
                con.commit()
                # print('deleted')
                con.close()
                self.load_data()
            else:
                return

    def save_results(self):
        con = sqlite3.connect("data/my_market_db")
        cur = con.cursor()

        if (self.lineEditName.text()):
            # print(self.lineEditName.text())
            name = self.lineEditName.text()
            result = int(list(cur.execute(
                f"Select Count(GoodTypeName) from GoodTypes where GoodTypes.GoodTypeName = '{self.lineEditName.text()}'"))[0][0])
            if result > 0:
                QMessageBox.about(self, 'Ошибка', "Такая категория уже существует")
                return
            cur = con.cursor()
            que = f"""INSERT INTO GoodTypes (GoodTypeName)
                           VALUES ('{name}')"""
            cur.execute(que)
            con.commit()
            # print('inserted')
            con.close()
            self.load_data()
        else:
            con.close()
            return



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
        map_request = f"http://static-maps.yandex.ru/1.x/?ll={ll[0]},{ll[1]}&spn={spn[0]},{spn[1]}&l={map_type}&size={s}&pt={ll[0]},{ll[1]},pm2gnm"
        # print(1)
    elif ll and spn == None:
        # print(2)
        map_request = f"http://static-maps.yandex.ru/1.x/?ll={ll[0]},{ll[1]}&l={map_type}&size={s}&z={z}&pt={ll[0]},{ll[1]},pm2gnm"
    elif ll == None and spn:
        # print(3)
        map_request = f"http://static-maps.yandex.ru/1.x/?l={map_type}&spn={spn[0]},{spn[1]}&size={s}&pt={ll[0]},{ll[1]},pm2gnm"
    else:
        # print(4)
        map_request = f"http://static-maps.yandex.ru/1.x/?l={map_type}&size={s}&z={z}&pt={ll[0]},{ll[1]},pm2gnm"

    response = requests.get(map_request)

    if not response:
        # print("Ошибка выполнения запроса:")
        # print(map_request)
        # print("Http статус:", response.status_code, "(", response.reason, ")")
        sys.exit(1)

    # Запишем полученное изображение в файл.
    map_file = "map.png"
    try:
        with open(map_file, "wb") as file:
            file.write(response.content)
    except IOError as ex:
        # print("Ошибка записи временного файла:", ex)
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

    return float(toponym_longitude), float(toponym_lattitude), dx, dy


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
