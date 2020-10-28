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

    def select(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def insert(self, query, insert):
        self.cursor.executemany(query, insert)
        self.connection.commit()
