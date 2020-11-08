from constants import *

class Coloriser:
    def colorise(self, value_text):
        value = value_text[0]
        text = value_text[1]
        if value > DAILY_UPPER_LIMIT:
                print(bcolors.RED + text + bcolors.ENDC)
        elif value > DAILY_LOWER_LIMIT:
                print(bcolors.YELLOW + text + bcolors.ENDC)
        else:
                print(bcolors.GREEN + text + bcolors.ENDC)
