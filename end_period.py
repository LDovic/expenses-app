import sqlite3
import csv
from sqlite3 import dbapi2
from datetime import date

conn = sqlite3.connect("expenses.db")
cur = conn.cursor()
cur.execute("SELECT price FROM expenses;")

select_price = cur.fetchall()
total_price = 0
for row in select_price:
	total_price += float('{0}'.format(row[0]))

total = total_price/100
print("Total price: ",total)

def write_csv():
	print("Writing CSV...")
	today = date.today()
	write_date_as_filename = today.strftime("%d.%m.%y") + ".csv"
	get_data = cur.execute("SELECT * FROM expenses;")
	with open(write_date_as_filename, "w", newline='') as csv_file:
		csv_writer = csv.writer(csv_file)
		csv_writer.writerow(['Total Expenses: ', total, '', ''])
		csv_writer.writerow(['Expenses', 'Date Worked', 'Date Of Entry', 'Time Of Entry'])
		for i in get_data:
			csv_writer.writerow(i)
			csv_writer.writerows(cur)

def wipe_db():
	print("Deleting table...")
	cur.execute("DELETE FROM expenses;")
	conn.commit()
	conn.close()

def end_pay_period_confirm(answer):
	print("Are you sure? (Y/N)")
	answer = input()
	if answer is "Y":	
		write_csv()
		wipe_db()
		quit()
	elif answer is "N":
		quit()
	else:
		end_pay_period_confirm(answer)

def end_pay_period():
	print("End period? (Y/N)")
	answer = input()
	if answer is "Y":
		end_pay_period_confirm(answer)
	elif answer is "N":
		quit()
	else:
		end_pay_period()

end_pay_period()
