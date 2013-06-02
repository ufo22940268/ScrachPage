import sqlite3
from shop import Shop
import hashlib
import util

class ShopTable():
    COL_CITY = "city";
    COL_PROVINCE = "province";
    COL_NAME = "name";
    COL_ADDRESS = "address";
    COL_NEW = "new";

    TABLE_NAME = "shop";

def getConnection():
    conn = sqlite3.connect("content.db");
    conn.row_factory = sqlite3.Row;
    return conn;

def createDb():
    conn = getConnection();
    c = conn.cursor();
    c.execute("DROP TABLE IF EXISTS shop");
    c.execute('''CREATE TABLE 
                shop(_id INTEGER PRIMARY KEY AUTOINCREMENT,  hash TEXT, new INTEGER DEFAULT 0,  province TEXT, city TEXT, name TEXT, address TEXT)''');
    conn.commit();
    c.close();

def insertShop(shop):
    conn = getConnection();
    c = conn.cursor();

    if hasInDb(shop):
        return False;

    c.execute("INSERT INTO shop(hash, new, province, city, name, address) values(?, ?, ?, ?, ?, ?)",
            (shop.hash(), 1, shop.province, shop.city, shop.name, shop.address));
    conn.commit();
    c.close();
    return True;

def hasInDb(shop):
    h = shop.hash();
    conn = getConnection();
    c = conn.cursor();
    #c.execute("SELECT * FROM " + ShopTable.TABLE_NAME + " where hash == ?", (h));
    c.execute("SELECT * FROM " + ShopTable.TABLE_NAME + " where hash == ?", (h,));
    conn.commit();
    count = len(c.fetchall());
    c.close();
    return count != 0;

def markAllAsOld():
    conn = getConnection();
    c = conn.cursor();
    c.execute("update " + ShopTable.TABLE_NAME + " set " + ShopTable.COL_NEW + "  = 0");
    conn.commit();
    c.close();

def getNewItemCount():
    conn = getConnection();
    c = conn.cursor();
    c.execute("select * from " + ShopTable.TABLE_NAME + " where " + ShopTable.COL_NEW + " == 1")
    conn.commit();
    count = len(c.fetchall());
    c.close();
    return count;

if __name__ == '__main__':
    #createDb();
    s = Shop();
    s.city = "adfa";
    s.name = "lkj";
    s.province = "iiii";
    s.address = "j88j8j";
    success = insertShop(s);
    if success:
        print("inserted"); 
    else:
        print("duplicated");

    util.printTable();
