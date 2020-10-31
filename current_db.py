import sqlite3
from sqlite3 import dbapi2

conn = sqlite3.connect("expenses.db")
cur = conn.cursor()
cur.execute("SELECT * FROM expenses;")

select_hours = cur.fetchall()


print(['Price', 'Expense', 'Date Of Entry'])
for row in select_hours:
	print(row)

import total_expenses
