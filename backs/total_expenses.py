from conn import *
from constants import *

if current_month == 1:
	previous_month = 12
else:
	previous_month = datetime.today().month - 1
if current_week == 1:
	previous_week = 52
else:
	previous_week = datetime.today().isocalendar()[1] - 1

previous_day = datetime.today().date() - timedelta(days=1) 

monthly_total = 0
weekly_total = 0
daily_total = 0
pmonthly_total = 0
pweekly_total = 0
pdaily_total = 0

def calc_total(period, price, cperiod):
	if period == cperiod:
		return price
	else:
		return 0

def colors(total, period_string):
	if total > daily_limit[1]:
		print(bcolors.FAIL + period_string.capitalize() + " total: £", round(total/100, 2))
	elif total > daily_limit[0]:
		print(bcolors.WARNING + period_string.capitalize() + " total: £", round(total/100, 2))
	else:
		print(bcolors.OKGREEN + period_string.capitalize() + " total: £", round(total/100, 2))

for row in select_prices:
	price = float('{0}'.format(row[0]))
	date = datetime.strptime(row[1], '%d, %m, %y').date()
	monthly_total += calc_total(date.month, price, current_month)
	weekly_total += calc_total(date.isocalendar()[1], price, current_week)
	daily_total += calc_total(date, price, current_day)	
	pmonthly_total += calc_total(date.month, price, previous_month)
	pweekly_total += calc_total(date.isocalendar()[1], price, previous_week)
	pdaily_total += calc_total(date, price, previous_day)

print("Last month total: £", pmonthly_total/100)
print("Monthly total: £",monthly_total/100)
print(bcolors.ENDC)
print("Last week total: £",pweekly_total/100)
colors(pweekly_total/7, 'last week average')
print(bcolors.ENDC)
print("Weekly total: £",weekly_total/100)
colors(weekly_total/dotw, 'week average')
print(bcolors.ENDC)
colors(pdaily_total, 'yesterday')
colors(daily_total, 'daily')

print(bcolors.ENDC)
