import time
import sqlite3
from expense import *
from sqlite3 import dbapi2
from datetime import date

print("Welcome to the expenses app")
print(date.today())

expense = Expense()
expenseController = ExpenseController()

expenseController.insertExpense([(expense.value, expense.name, expense.date_entered)])
