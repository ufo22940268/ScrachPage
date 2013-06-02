all:
	python main.py

db:
	python db.py

print-db:
	sqlite3 content.db "select * from shop"

clear-db:
	sqlite3 content.db "delete from shop"
