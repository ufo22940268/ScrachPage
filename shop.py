import hashlib

class Shop():
    def __init__(self):
        self.province = "";
        self.city = "";
        self.name = "";
        self.address = "";

    def __str__(self):
        return "province:" + self.province.encode("utf-8") + "\tcity:" + self.city.encode("utf-8") + "\tname:" + self.name.encode("utf-8") + "\taddress:" + self.address.encode("utf-8");


    def hash(self):
        m = hashlib.md5();
        m.update(self.__str__());
        return m.hexdigest();

