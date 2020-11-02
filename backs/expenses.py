import time
import sqlite3
from sqlite3 import dbapi2
from datetime import date

date_entered = time.strftime("%d, %m, %y")

print(date.today())
price = float(input("Enter p: "))
expense = input("Enter thing: ")

insert = [(price, expense, date_entered)]

conn = sqlite3.connect("expenses.db")
cur = conn.cursor()
cur.executemany("INSERT INTO expenses VALUES (?, ?, ?)", insert)
conn.commit()

import total_expenses
