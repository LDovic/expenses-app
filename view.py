import time
import sqlite3
from expense import *
from sqlite3 import dbapi2
from datetime import date


class View:
    def __init__(self):
        self.expenseController = ExpenseController()

    def switch(self, string):
        switcher = input(string)
        try:
            return int(switcher)
        except ValueError:
            pass

    def insertExpense(self):
        try:
            value = input("Enter £: ")
            int(value)
        except:
            print('Incorrect datatype')
            return
        try:
            name = input("Enter thing: ")
            str(name)
        except:
            print('Incorrect datatype')
            return
        expense = Expense(value, name)
        self.expenseController.insertExpense([(expense.value, expense.name, expense.date_entered, expense.day_of_the_week)])

    def getPurchases(self):
        string = "1. Daily\n2. Weekly\n3. Monthly\n4. Days of the week\n5. Average daily\n6. Quit\n"
        switcher = self.switch(string)
        if switcher == 1:
            for days, total in self.expenseController.getDaysOfTheWeekExpenses().items():
                print(days + ": £" + str(total / 100))
        elif switcher == 2:
            print(self.expenseController.getWeeklyExpenses()) 
        elif switcher == 3:
            print(self.expenseController.getMonthlyExpenses()) 
        elif switcher == 4:
            print(self.expenseController.getDaysOfTheWeekExpenses())
        elif switcher == 5:
            print(self.expenseController.getAverageDailySpend())
        elif switcher == 6:
            return False
        else:
            switcher = switch(string)

    def getPurchaseHistory(self):
        for purchase in self.expenseController.getPurchaseHistory():
            print(purchase)

    def app(self):
        print("Welcome to the expenses app")
        print("Today: " + str(date.today()))
        print(self.expenseController.getDailyExpenses())
        print(self.expenseController.getWeeklyExpenses())
        print(self.expenseController.getMonthlyExpenses())
        string = "1. Insert expense\n2. Total expenses\n3. Purchase history\n4. Quit\n"
        switcher = self.switch(string)
        if switcher == 1:
            self.insertExpense()
        elif switcher == 2:
            self.getPurchases()
        elif switcher == 3:
            self.getPurchaseHistory()
        elif switcher == 4:
            return True

