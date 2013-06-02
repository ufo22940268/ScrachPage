from bs4 import BeautifulSoup
from util import *
import os
import db
import urllib
import shop
import excel

tags = [
	"a1",
	"a2",
	"a3",
	"a4",
	"a5",
	"a6",
	"a7",
	"a8",
	"a9",
	"a10",
	"b1",
	"b2",
	"b3",
	"b4",
	"b5",
	"b6",
	"b7",
	"b8",
	"b9",
	"b10",
	"c1",
	"c2",
	"c3",
	"c4",
	"c5",
	];

def parseShop(raw):
    contents = raw.contents;
    p = shop.Shop();
    p.city = contents[real(1)].string;
    p.name = contents[real(2)].string;
    p.address = contents[real(3)].string;
    return p;

def real(n):
    return n*2 - 1;

def isPrimaryItem(shop):
    return len(shop.contents) == 9;

def parseProvince(shop):
    return shop.contents[1].string;

def main():
    for tag in tags:
	#soup = BeautifulSoup(urllib.urlopen("http://creditcard.bankcomm.com/resource/cc_bankcomm_com/upload/activity/article//2012_4/12_21/legou_list(2).html#" + tag));
	#soup = BeautifulSoup(open("old.html"));
	soup = BeautifulSoup(open("new.html"));
	i = 1;
	while True: 
	    node = soup.find("td", id="a" + str(i));
	    if node != None:
		count = node["rowspan"];
		province = node.string;
		parent = node.parent;
		del parent.contents[0:2];
		insertProvince(parent, province, int(count));
		i += 1;
	    else:
		break;

def insertProvince(firstItem, province, count):
    insertItem(firstItem, province);
    for i in range(count - 1):
        firstItem = firstItem.next_sibling.next_sibling;
        insertItem(firstItem, province);

def insertItem(item, province):
    p = parseShop(item);
    p.province = province;
    db.insertShop(p);
    
if __name__ == '__main__':
    db.markAllAsOld();
    main();
    #os.system("sqlite3 content.db \"select * from shop\"");
    excel.export();
    print(str(db.getNewItemCount()) + " new items added!");
