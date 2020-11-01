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
        self.day_of_the_week = time.localtime(time.time()).tm_wday

class ExpenseController:
    def __init__(self):
        self.db = Db()

    def insertExpense(self, insert):
        self.db.insert(insert)

    def getDaysOfTheWeekExpenses(self):
        days_of_the_week = {"Monday": 0, "Tuesday": 0, "Wednesday": 0, "Thursday": 0, "Friday": 0, "Saturday": 0, "Sunday": 0}
        for row in self.db.select_dotw():
            day = int(row[1])
            price = float('{0}'.format(row[0]))
            if day == 0:
                days_of_the_week["Monday"] += price
            if day == 1:
                days_of_the_week["Tuesday"] += price
            if day == 2:
                days_of_the_week["Wednesday"] += price 
            if day == 3:
                days_of_the_week["Thursday"] += price
            if day == 4:
                days_of_the_week["Friday"] += price
            if day == 5:
                days_of_the_week["Saturday"] += price
            if day == 6:
                days_of_the_week["Sunday"] += price
        return days_of_the_week

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
