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

    def getWeeksOfTheYearExpenses(self):
        num = [i for i in range(53)]
        data = [0] * 52
        for row in self.db.select():
            week = datetime.strptime(row[1], '%d, %m, %y').date().isocalendar()[1]
            price = float('{0}'.format(row[0]))
            for week_num in range(1, 52):
                if week_num == week:
                    data[week_num] += price
        for week, row in zip(num, data):
            price = self.expenseString(row)
            print("{0:1}{1:}".format(week, price))

    def getWeeklyExpenses(self):
        this_week = datetime.today().date().isocalendar()[1]
        total = 0
        for row in self.db.select():
            date = datetime.strptime(row[1], '%d, %m, %y').date()
            price = float('{0}'.format(row[0]))
            if this_week == date.isocalendar()[1]:
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

        for row in self.db.select():
            month = datetime.strptime(row[1], '%d, %m, %y').date().month
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
