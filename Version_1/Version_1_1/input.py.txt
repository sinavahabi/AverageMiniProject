"""
    This is updated version of 'Calculating Average Mark' program, and it was writen in OOP method.
"""

from Classes.Colors import bcolors


# First we instantiate Input class to get each count of X modular lesson from the user.
class Input:

    def __init__(self):
        self.four_modular_count = 0
        self.three_modular_count = 0
        self.two_modular_count = 0
        self.one_modular_count = 0
        self.half_modular_count = 0

# Using try except method give us the ensurance that entering a wrong input won't crash or stop our program.
    def four_modular_input(self):
        while True:
            try:
                self.four_modular_count = int(
                    input(bcolors.BOLD + 'Enter number of your lessons for FOUR modular lessons: ' + bcolors.ENDC))
                if self.four_modular_count > 5:
                    print(bcolors.BOLD + bcolors.FAIL + 'something went wrong!, seems like'
                                                        ' you have entered an unusual number!' + bcolors.ENDC)
                    continue
                if self.four_modular_count < 0:
                    print(bcolors.BOLD + bcolors.FAIL + 'something went wrong!, seems like'
                                                        ' you have entered an unusual number!' + bcolors.ENDC)
                    continue
            except:
                print(bcolors.BOLD + bcolors.FAIL + '\'Please Just Enter an Integer Number\'' + bcolors.ENDC)
                continue
            break

    def three_modular_input(self):
        while True:
            try:
                self.three_modular_count = int(
                    input(bcolors.BOLD + 'Enter number of your lessons for THREE modular lessons: ' + bcolors.ENDC))
                if self.three_modular_count > 7:
                    print(bcolors.BOLD + bcolors.FAIL + 'something went wrong!, seems like'
                                                        ' you have entered an unusual number!' + bcolors.ENDC)
                    continue
                if self.three_modular_count < 0:
                    print(bcolors.BOLD + bcolors.FAIL + 'something went wrong!, seems like'
                                                        ' you have entered an unusual number!' + bcolors.ENDC)
                    continue
            except:
                print(bcolors.BOLD + bcolors.FAIL + '\'Please Just Enter an Integer Number\'' + bcolors.ENDC)
                continue
            break

    def two_modular_input(self):
        while True:
            try:
                self.two_modular_count = int(
                    input(bcolors.BOLD + 'Enter number of your lessons for TWO modular lessons: ' + bcolors.ENDC))
                if self.two_modular_count > 9:
                    print(bcolors.BOLD + bcolors.FAIL + 'something went wrong!, seems like'
                                                        ' you have entered an unusual number!' + bcolors.ENDC)
                    continue
                if self.two_modular_count < 0:
                    print(bcolors.BOLD + bcolors.FAIL + 'something went wrong!, seems like'
                                                        ' you have entered an unusual number!' + bcolors.ENDC)
                    continue
            except:
                print(bcolors.BOLD + bcolors.FAIL + '\'Please Just Enter an Integer Number\'' + bcolors.ENDC)
                continue
            break

    def one_modular_input(self):
        while True:
            try:
                self.one_modular_count = int(
                    input(bcolors.BOLD + 'Enter number of your lessons for ONE modular lessons: ' + bcolors.ENDC))
                if self.one_modular_count > 10:
                    print(bcolors.BOLD + bcolors.FAIL + 'something went wrong!, seems like'
                                                        ' you have entered an unusual number!' + bcolors.ENDC)
                    continue
                if self.one_modular_count < 0:
                    print(bcolors.BOLD + bcolors.FAIL + 'something went wrong!, seems like'
                                                        ' you have entered an unusual number!' + bcolors.ENDC)
                    continue
            except:
                print(bcolors.BOLD + bcolors.FAIL + '\'Please Just Enter an Integer Number\'' + bcolors.ENDC)
                continue
            break

    def half_modular_input(self):
        while True:
            try:
                self.half_modular_count = int(
                    input(bcolors.BOLD + 'Enter number of your lessons for HALF modular lessons: ' + bcolors.ENDC))
                if self.half_modular_count > 20:
                    print(bcolors.BOLD + bcolors.FAIL + 'something went wrong!, seems like'
                                                        ' you have entered an unusual number!' + bcolors.ENDC)
                    continue
                if self.half_modular_count < 0:
                    print(bcolors.BOLD + bcolors.FAIL + 'something went wrong!, seems like'
                                                        ' you have entered an unusual number!' + bcolors.ENDC)
                    continue
            except:
                print(bcolors.BOLD + bcolors.FAIL + '\'Please Just Enter an Integer Number\'' + bcolors.ENDC)
                continue
            break
