import time
from datetime import datetime
import sqlite3
from database import *
from controller import Formatter
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
        self.day = time.strftime("%d")
        self.week = datetime.today().date().isocalendar()[1]
        self.month = time.strftime("%m")
        self.year = time.strftime("%Y")

    def insertExpense(self, insert):
        self.db.insert(insert)

    def getDaysOfTheWeekExpenses(self):
        formatter = Formatter()
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

        data.append(Monday)
        data.append(Tuesday)        
        data.append(Wednesday)
        data.append(Thursday)
        data.append(Friday)
        data.append(Saturday)
        data.append(Sunday)

        zipped = list(zip(days_of_the_week, map(formatter.pricify, data)))
        Formatter().formatTwo(zipped)

    def getYesterdayExpenses(self):
        from datetime import date
        yesterday = date.today() - timedelta(days=1)
        day = yesterday.strftime("%d")
        month = yesterday.strftime("%m")
        year = yesterday.strftime("%Y")
        total = 0
        for row in self.db.select_day(day, month, year):
            price = float('{0}'.format(row[0]))
            total += price
        return (total, "£" + str(total / 100) + " spent yesterday")

    def getDailyExpenses(self):
        total = 0
        for row in self.db.select_day(self.day, self.month, self.year):
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
        formatter = Formatter()
        num = [i for i in range(1, 53)]
        data = [0] * 53
        for row in self.db.select_weeks(self.year):
            week = row[1]
            price = float('{0}'.format(row[0]))
            for week_num in num:
                if week == week_num:
                    data[week_num - 1] += price
        zipped = list(zip(num, map(formatter.pricify, data)))
        Formatter().formatTwo(zipped)

    def getWeeklyExpenses(self):
        total = 0
        for row in self.db.select_week(self.week, self.year):
            price = float('{0}'.format(row[0]))
            total += price
        return (total, "£" + str(total / 100) + " spent this week")

    def getMonthsOfTheYearExpenses(self):
        formatter = Formatter()
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

        for row in self.db.select_months(self.year):
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

        data.append(January)
        data.append(February)
        data.append(March)
        data.append(April)
        data.append(May)
        data.append(June)
        data.append(July)
        data.append(August)
        data.append(September)
        data.append(October)
        data.append(November)
        data.append(December)

        zipped = list(zip(months, map(formatter.pricify, data)))
        Formatter().formatTwo(zipped)

    def getAverageDailySpend(self):
        total = 0
        for row in self.db.select_week():
            price = float('{0}'.format(row[0]))
            if self.week == row[1]:
                total += price
        return (total, "£" + str(total / 7 / 100) + " average daily spend")

    def getPurchaseHistoryWeek(self):
        data = []
        headings = ['Price', 'Expense', 'Date', 'Day']
        data.append(headings)
        for element in self.db.select_expenses_week(self.week, self.year):
            collect = []
            date = "-".join(list(map(str, element[2:5])))
            collect.append("£" + str(element[0] / 100))
            collect.append(element[1])
            collect.append(date)
            collect.append(element[5])
            data.append(collect)
        Formatter().formatFour(data)
