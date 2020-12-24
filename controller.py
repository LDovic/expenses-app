from constants import *

class Formatter:
    def pricify(self, price):
       return "£" + str(int(price) / 100)

    def formatTwo(self, data):
        output = "{0:<10}{1:>8}" 
        for datum in data:
            datum = list(map(str, datum))
            print(output.format(datum[0], datum[1]))

    def formatFour(self, data):
        output = "{0:<10}{1:>10}{2:>10}{3:>10}"
        for datum in data:
            datum = list(map(str, datum))
            print(output.format(datum[0], datum[1], datum[2], datum[3]))

class Coloriser:
    def coloriseCommunication(self, text):
        print(bcolors.BLUE + text + bcolors.ENDC)

    def coloriseExpense(self, value_text):
        value = value_text[0]
        text = value_text[1]
        if value > DAILY_UPPER_LIMIT:
                print(bcolors.RED + text + bcolors.ENDC)
        elif value > DAILY_LOWER_LIMIT:
                print(bcolors.YELLOW + text + bcolors.ENDC)
        else:
                print(bcolors.GREEN + text + bcolors.ENDC)
