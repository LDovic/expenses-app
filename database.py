import sqlite3
import csv
from constants import *
from sqlite3 import dbapi2
from datetime import datetime
from datetime import date
from datetime import timedelta

class Db:
    def __init__(self):
        self.connection = sqlite3.connect("expenses.db")
        self.cursor = self.connection.cursor()

    def insert(self, insert):
        self.cursor.executemany("INSERT INTO expenses VALUES (?, ?, ?, ?, ?, ?, ?)", insert)
        self.connection.commit()

    def delete(self, id):
        self.cursor.execute("DELETE FROM expenses WHERE rowid = ?", (id,))
        self.connection.commit()

    def select(self, id):
        self.cursor.execute("SELECT rowid FROM expenses WHERE rowid = ?", (id,))
        return self.cursor.fetchall()

    def select_expenses_week(self, week, year):
        self.cursor.execute("SELECT rowid, price, expense, day, month, year, weekday FROM expenses WHERE week = ? AND year = ?", (week, year))
        return self.cursor.fetchall()

    def select_day(self, day, month, year):
        self.cursor.execute("SELECT price, day FROM expenses WHERE day = ? AND month = ? AND year = ?", (day, month, year))
        return self.cursor.fetchall()        

    def select_week(self, week, year):
        self.cursor.execute("SELECT price, week, weekday FROM expenses WHERE week = ? AND year = ?", (week, year))
        return self.cursor.fetchall()

    def select_weeks(self, year):
        self.cursor.execute("SELECT price, week FROM expenses WHERE year = ?", (year,))
        return self.cursor.fetchall()

    def select_months(self, year):
        self.cursor.execute("SELECT price, month FROM expenses WHERE year = ?", (year,))
        return self.cursor.fetchall()    
