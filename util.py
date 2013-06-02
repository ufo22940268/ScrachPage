import os

def printTable():
    os.system("sqlite3 content.db \"select * from shop\"");

def deleteTable(table):
    conn = getConnection();
    c = conn.cursor();
    c.execute("DELETE FROM " + table);
    conn.commit();
    c.close();

if __name__ == '__main__':
    printTable("shop");
