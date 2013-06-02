import xlwt
import db
from db import ShopTable

class ShopExcel():
    TITLES = [
            "province",    # 0
            "city",        # 1
            "district",
            "full_name",
            "brand",
            "store",       # 5
            "addr",        # 6
            "tel",
            "begin_dt",
            "end_dt",
            "day_of_week",
            "card_level",
            "discription",
            "note",
            "include",
            "exclude",
            "dp_id",
            ]

    ROW_PROVINCE = 0;
    ROW_CITY = 1;
    ROW_NAME = 5;
    ROW_ADDRESS = 6;



def export():
    wb = xlwt.Workbook()
    ws = wb.add_sheet("My Sheet")
    #Add title.
    for i, title in enumerate(ShopExcel.TITLES):
        ws.write(0, i, title)

    conn = db.getConnection();
    c = conn.cursor();
    c.execute("SELECT * FROM shop where new == 1");
    conn.commit();
    row = 1;
    for r in c.fetchall():
        ws.write(row, ShopExcel.ROW_PROVINCE, r[ShopTable.COL_PROVINCE])
        ws.write(row, ShopExcel.ROW_CITY, r[ShopTable.COL_CITY])
        ws.write(row, ShopExcel.ROW_NAME, r[ShopTable.COL_NAME])
        ws.write(row, ShopExcel.ROW_ADDRESS, r[ShopTable.COL_ADDRESS])
        row += 1;
    c.close();
    wb.save("myworkbook.xls")

if __name__ == '__main__':
	export()
