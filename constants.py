from datetime import datetime
from datetime import date
from datetime import timedelta

DAILY_UPPER_LIMIT = 1000
DAILY_LOWER_LIMIT = 800

class bcolors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

daily_limit = (800, 1000)

current_month = datetime.today().month
current_week = datetime.today().isocalendar()[1]
dotw = datetime.today().isocalendar()[2]
current_day = datetime.today().date()
