import time
from datetime import datetime
import sqlite3
from database import *
from sqlite3 import dbapi2

class Expense:
    def __init__(self, value, name):
        self.value = value
        self.name = name
        self.day = time.strftime("%d")
        self.month = time.strftime("%m")
        self.year = time.strftime("%Y")
        self.week = datetime.today().date().isocalendar()[1]
        self.weekday = time.localtime(time.time()).tm_wday

class ExpenseController:
    def __init__(self):
        self.db = Db()
        self.week = datetime.today().date().isocalendar()[1]
        self.month = time.strftime("%m")
        self.year = time.strftime("%Y")

    def insertExpense(self, insert):
        self.db.insert(insert)

    def expenseString(self, expense):
        return "£" + str(expense / 100)

    def getDaysOfTheWeekExpenses(self):
        data = []
        day_expense = ["Day", "Expense"]
        days_of_the_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        Monday = 0
        Tuesday = 0
        Wednesday = 0
        Thursday = 0
        Friday = 0
        Saturday = 0
        Sunday = 0 

        for row in self.db.select_week(self.week, self.year):
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
        year = self.year
        if (self.month == 1) and (yesterday == 31):
            year = self.year - 1
        total = 0
        for row in self.db.select_day(yesterday, year):
            price = float('{0}'.format(row[0]))
            total += price
        return (total, "£" + str(total / 100) + " spent yesterday")

    def getDailyExpenses(self):
        total = 0
        for row in self.db.select_day(time.strftime("%d"), self.year):
            price = float('{0}'.format(row[0]))
            total += price
        return (total, "£" + str(total / 100) + " spent today")

    def getLastWeekExpenses(self):
        last_week = self.week - 1
        year = self.year
        if self.week <= 1:
            last_week = 52
            year = self.year - 1
        total = 0
        for row in self.db.select_week(last_week, year):
            price = float('{0}'.format(row[0]))
            if last_week == row[1]:
                total += price
        return (total, "£" + str(total / 100) + " spent last week")

    def getWeeksOfTheYearExpenses(self):
        num = [i for i in range(1, 53)]
        data = [0] * 53
        for row in self.db.select_weeks(self.year):
            week = row[1]
            price = float('{0}'.format(row[0]))
            for week_num in num:
                if week == week_num:
                    data[week_num - 1] += price
        for week, row in zip(num, data):
            price = self.expenseString(row)
            print("{0:1}{1:}".format(week, price))

    def getWeeklyExpenses(self):
        total = 0
        for row in self.db.select_week(self.week, self.year):
            price = float('{0}'.format(row[0]))
            total += price
        return (total, "£" + str(total / 100) + " spent this week")

    def getMonthsOfTheYearExpenses(self):
        data = []
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

        January = 0
        February = 0
        March = 0
        April = 0
        May = 0
        June = 0
        July = 0
        August = 0
        September = 0
        October = 0
        November = 0
        December = 0

        for row in self.db.select_month(self.year):
            month = row[1]
            price = float('{0}'.format(row[0]))
            if month == 1:
                January += price
            elif month == 2:
                February += price 
            elif month == 3:
                March += price
            elif month == 4:
                April += price
            elif month == 5:
                May += price
            elif month == 6:
                June += price
            elif month == 7:
                July += price
            elif month == 8:
                August += price
            elif month == 9:
                September += price
            elif month == 10:
                October += price
            elif month == 11:
                November += price
            elif month == 12:
                December += price

        data.append(self.expenseString(January))
        data.append(self.expenseString(February))
        data.append(self.expenseString(March))
        data.append(self.expenseString(April))
        data.append(self.expenseString(May))
        data.append(self.expenseString(June))
        data.append(self.expenseString(July))
        data.append(self.expenseString(August))
        data.append(self.expenseString(September))
        data.append(self.expenseString(October))
        data.append(self.expenseString(November))
        data.append(self.expenseString(December))

        for month, row in zip(months, data):
            print("{0:12}{1:}".format(month, row))

    def getAverageDailySpend(self):
        total = 0
        for row in self.db.select_week():
            price = float('{0}'.format(row[0]))
            if self.week == row[1]:
                total += price
        return (total, "£" + str(total / 7 / 100) + " average daily spend")

    def getPurchaseHistory(self):
        return self.db.select_all()
