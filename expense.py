import time
import sqlite3
from database import *
from sqlite3 import dbapi2
from datetime import date

class Expense:
    def __init__(self):
        self.value = float(input("Enter £: "))
        self.name = input("Enter thing: ")
        self.date_entered = time.strftime("%d, %m, %y")

class ExpenseController:
    def insertExpense(self, insert):
        db = Db()
        db.insert("INSERT INTO expenses VALUES (?, ?, ?)", insert)
