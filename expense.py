import time
import sqlite3
from database import *
from sqlite3 import dbapi2
from datetime import date

class Expense:
    def __init__(self, value, name):
        self.value = value
        self.name = name
        self.date_entered = time.strftime("%d, %m, %y")

class ExpenseController:
    def __init__(self):
        self.db = Db()

    def insertExpense(self, insert):
        self.db.insert(insert)

    def getDailyExpenses(self):
        today = time.localtime(time.time()).tm_mday
        total = 0
        for row in self.db.select():
            date = datetime.strptime(row[1], '%d, %m, %y').date()
            price = float('{0}'.format(row[0]))
            if today == date.day:
                total += price
        return "£" + str(total / 100) + " spent today"

    def getWeeklyExpenses(self):
        this_week = datetime.today().date().isocalendar()[1]
        total = 0
        for row in self.db.select():
            date = datetime.strptime(row[1], '%d, %m, %y').date()
            price = float('{0}'.format(row[0]))
            if this_week == date.isocalendar()[1]:
                total += price
        return "£" + str(total / 100) + " spent this week"

    def getMonthlyExpenses(self):
        this_month = datetime.today().date().month
        total = 0
        for row in self.db.select():
            date = datetime.strptime(row[1], '%d, %m, %y').date()
            price = float('{0}'.format(row[0]))
            if this_month == date.month:
                total += price
        return "£" + str(total / 100) + " spent this month"

    def getPurchaseHistory(self):
        return self.db.select_all()
