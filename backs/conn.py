import sqlite3
import csv
from constants import *
from sqlite3 import dbapi2
from datetime import datetime
from datetime import date
from datetime import timedelta

conn = sqlite3.connect("expenses.db")
cur = conn.cursor()

cur.execute("SELECT price, date_entered FROM expenses;")
select_prices = cur.fetchall()
