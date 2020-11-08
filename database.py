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

    def select(self):
        self.cursor.execute("SELECT price, date_entered FROM expenses")
        return self.cursor.fetchall()

    def select_all(self):
        self.cursor.execute("SELECT * FROM expenses;")
        return self.cursor.fetchall()

    def select_dotw(self):
        self.cursor.execute("SELECT price, date_entered, day_of_the_week FROM expenses")
        return self.cursor.fetchall()

    def insert(self, insert):
        self.cursor.executemany("INSERT INTO expenses VALUES (?, ?, ?, ?)", insert)
        self.connection.commit()
