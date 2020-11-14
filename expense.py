import time
import sqlite3
from database import *
from sqlite3 import dbapi2

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

    def expenseString(self, expense):
        return "£" + str(expense / 100)

    def getDaysOfTheWeekExpenses(self):
        data = []
        day_expense = ["Day", "Expense"]
        days_of_the_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        this_week = datetime.today().date().isocalendar()[1]
        Monday = 0
        Tuesday = 0
        Wednesday = 0
        Thursday = 0
        Friday = 0
        Saturday = 0
        Sunday = 0 

        for row in self.db.select_dotw():
            date = datetime.strptime(row[1], '%d, %m, %y').date()
            if this_week == date.isocalendar()[1]:
                day = int(row[2])
                price = float('{0}'.format(row[0]))
                if day == 0:
                    Monday += price
                if day == 1:
                    Tuesday += price
                if day == 2:
                    Wednesday += price 
                if day == 3:
                    Thursday += price
                if day == 4:
                    Friday += price
                if day == 5:
                    Saturday += price
                if day == 6:
                    Sunday += price

        data.append(self.expenseString(Monday))
        data.append(self.expenseString(Tuesday))        
        data.append(self.expenseString(Wednesday))
        data.append(self.expenseString(Thursday))
        data.append(self.expenseString(Friday))
        data.append(self.expenseString(Saturday))
        data.append(self.expenseString(Sunday))

        for day, row in zip(days_of_the_week, data):
            print("{0:12}{1:}".format(day, row))

    def getYesterdayExpenses(self):
        from datetime import date
        yesterday = date.today() - timedelta(days=1)
        total = 0
        for row in self.db.select():
            row_date = datetime.strptime(row[1], '%d, %m, %y').date()
            price = float('{0}'.format(row[0]))
            if yesterday == row_date:
                total += price
        return (total, "£" + str(total / 100) + " spent yesterday")

    def getDailyExpenses(self):
        today = time.localtime(time.time()).tm_mday
        total = 0
        for row in self.db.select():
            row_date = datetime.strptime(row[1], '%d, %m, %y').date()
            price = float('{0}'.format(row[0]))
            if row_date == date.today():
                total += price
        return (total, "£" + str(total / 100) + " spent today")

    def getLastWeekExpenses(self):
        this_week = datetime.today().date().isocalendar()[1]
        last_week = this_week - 1
        if this_week <= 1:
            last_week = 52
        total = 0
        for row in self.db.select():
            date = datetime.strptime(row[1], '%d, %m, %y').date()
            price = float('{0}'.format(row[0]))
            if last_week == date.isocalendar()[1]:
                total += price
        return (total, "£" + str(total / 100) + " spent last week")

    def getWeeklyExpenses(self):
        this_week = datetime.today().date().isocalendar()[1]
        total = 0
        for row in self.db.select():
            date = datetime.strptime(row[1], '%d, %m, %y').date()
            price = float('{0}'.format(row[0]))
            if this_week == date.isocalendar()[1]:
                total += price
        return (total, "£" + str(total / 100) + " spent this week")

    def getMonthlyExpenses(self):
        this_month = datetime.today().date().month
        total = 0
        for row in self.db.select():
            date = datetime.strptime(row[1], '%d, %m, %y').date()
            price = float('{0}'.format(row[0]))
            if this_month == date.month:
                total += price
        return (total, "£" + str(total / 100) + " spent this month")

    def getAverageDailySpend(self):
        this_week = datetime.today().date().isocalendar()[1]
        total = 0
        for row in self.db.select():
            date = datetime.strptime(row[1], '%d, %m, %y').date()
            price = float('{0}'.format(row[0]))
            if this_week == date.isocalendar()[1]:
                total += price
        return (total, "£" + str(total / 7 / 100) + " average daily spend")

    def getPurchaseHistory(self):
        return self.db.select_all()
