class GoodType:
    def __init__(self, id, goodtypename):
        self.id = id
        self.goodtypename = goodtypename

    def __repr__(self):
        return f"{self.id} {self.goodtypename}"

    def __str__(self):
        return f"{self.id} {self.goodtypename}"


class Good:
    def __init__(self, id, goodname, goodtypeid):
        self.id = id
        self.goodname = goodname
        self.goodtypeid = goodtypeid

    def __repr__(self):
        return f"{self.id} {self.goodtypeid} {self.goodname}"

    def __str__(self):
        return f"{self.id} {self.goodtypeid} {self.goodname}"


class GoodMarket:
    def __init__(self, id, goodid, marketplaceid, price):
        self.id = id
        self.goodid = goodid
        self.marketplaceid = marketplaceid
        self.price = price

    def __repr__(self):
        return f"{self.id} {self.goodid} {self.marketplaceid} {self.price}"

    def __repr__(self):
        return f"{self.id} {self.goodid} {self.marketplaceid} {self.price}"


class Market:
    def __init__(self, id, marketname, logo):
        self.id = id
        self.marketname = marketname
        self.logo = logo

    def __repr__(self):
        return f"{self.id} {self.marketname} {self.logo}"

    def __str__(self):
        return f"{self.id} {self.marketname} {self.logo}"


class MarketPlace:
    def __init__(self, id, marketid, address, latitide, longitude):
        self.id = id
        self.marketid = marketid
        self.address = address
        self.latitide = latitide
        self.longitude = longitude

    def __repr__(self):
        return f"{self.id} {self.marketid} {self.address} {self.latitide} {self.longitude}"

    def __repr__(self):
        return f"{self.id} {self.marketid} {self.address} {self.latitide} {self.longitude}"


class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role

    def __repr__(self):
        return f"{self.username} {self.password} {self.role}"

    def __str__(self):
        return f"{self.username} {self.password} {self.role}"
