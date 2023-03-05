# First we import our Input class.
from AverageMiniProject.Version_1.Version_1_1.input import Input, bcolors
import sys


# By inheritance from Input class defining methods we get each lesson's marks from user.
class Calculation(Input):

    four_modular, three_modular, two_modular, one_modular, half_modular = [], [], [], [], []

# Also here, using try except method give us the ensurance that entering a wrong input won't crash or stop our program.
    def get_four_modular_mark(self):
        for i in range(0, self.four_modular_count):
            while True:
                try:
                    num4 = i + 1
                    self.four_modular_marks = float(input(bcolors.OKBLUE + 'Enter lesson number '
                                                    + str(num4) + ' mark from FOUR modular lessons: ' + bcolors.ENDC))
                    if self.four_modular_marks > 20:
                        print(bcolors.FAIL + bcolors.BOLD + "Your lesson mark must be between 0-20."
                                                            " Try again!" + bcolors.ENDC)
                        continue
                    if self.four_modular_marks < 0:
                        print(bcolors.FAIL + bcolors.BOLD + "Your lesson mark must be between 0-20."
                                                            " Try again!" + bcolors.ENDC)
                        continue
                except:
                    print(bcolors.FAIL + '\'you Can Only Enter Numbers\'' + bcolors.ENDC)
                    continue
                break
            self.four_modular.append(self.four_modular_marks)

        self.four_modular = list(map(lambda x: x * 4, self.four_modular))
        return self.four_modular

    def get_three_modular_mark(self):
        for i in range(0, self.three_modular_count):
            while True:
                try:
                    num3 = i + 1
                    self.three_modular_marks = float(input(bcolors.OKBLUE + 'Enter lesson number '
                                                     + str(num3) + ' mark from THREE modular lessons: ' + bcolors.ENDC))
                    if self.three_modular_marks > 20:
                        print(bcolors.FAIL + bcolors.BOLD + "Your lesson mark must be between 0-20."
                                                            " Try again!" + bcolors.ENDC)
                        continue
                    if self.three_modular_marks < 0:
                        print(bcolors.FAIL + bcolors.BOLD + "Your lesson mark must be between 0-20."
                                                            " Try again!" + bcolors.ENDC)
                        continue
                except:
                    print(bcolors.FAIL + '\'you Can Only Enter Numbers\'' + bcolors.ENDC)
                    continue
                break
            self.three_modular.append(self.three_modular_marks)

        self.three_modular = list(map(lambda x: x * 3, self.three_modular))
        return self.three_modular

    def get_two_modular_mark(self):
        for i in range(0, self.two_modular_count):
            while True:
                try:
                    num2 = i + 1
                    self.two_modular_marks = float(input(bcolors.OKBLUE + 'Enter lesson number '
                                                   + str(num2) + ' mark from TWO modular lessons: ' + bcolors.ENDC))
                    if self.two_modular_marks > 20:
                        print(bcolors.FAIL + bcolors.BOLD + "Your lesson mark must be between 0-20."
                                                            " Try again!" + bcolors.ENDC)
                        continue
                    if self.two_modular_marks < 0:
                        print(bcolors.FAIL + bcolors.BOLD + "Your lesson mark must be between 0-20."
                                                            " Try again!" + bcolors.ENDC)
                        continue
                except:
                    print(bcolors.FAIL + '\'you Can Only Enter Numbers\'' + bcolors.ENDC)
                    continue
                break
            self.two_modular.append(self.two_modular_marks)

        self.two_modular = list(map(lambda x: x * 2, self.two_modular))
        return self.two_modular

    def get_one_modular_mark(self):
        for i in range(0, self.one_modular_count):
            while True:
                try:
                    num1 = i + 1
                    self.one_modular_marks = float(input(bcolors.OKBLUE + 'Enter lesson number '
                                                   + str(num1) + ' mark from ONE modular lessons: ' + bcolors.ENDC))
                    if self.one_modular_marks > 20:
                        print(bcolors.FAIL + bcolors.BOLD + "Your lesson mark must be between 0-20."
                                                            " Try again!" + bcolors.ENDC)
                        continue
                    if self.one_modular_marks < 0:
                        print(bcolors.FAIL + bcolors.BOLD + "Your lesson mark must be between 0-20."
                                                            " Try again!" + bcolors.ENDC)
                        continue
                except:
                    print(bcolors.FAIL + '\'you Can Only Enter Numbers\'' + bcolors.ENDC)
                    continue
                break
            self.one_modular.append(self.one_modular_marks)

        self.one_modular = list(map(lambda x: x * 1, self.one_modular))
        return self.one_modular

    def get_half_modular_mark(self):
        for i in range(0, self.half_modular_count):
            while True:
                try:
                    num = i + 1
                    self.half_modular_marks = float(input(bcolors.OKBLUE + 'Enter lesson number '
                                                    + str(num) + ' mark from HALF modular lessons: ' + bcolors.ENDC))
                    if self.half_modular_marks > 20:
                        print(bcolors.FAIL + bcolors.BOLD + "Your lesson mark must be between 0-20."
                                                            " Try again!" + bcolors.ENDC)
                        continue
                    if self.half_modular_marks < 0:
                        print(bcolors.FAIL + bcolors.BOLD + "Your lesson mark must be between 0-20."
                                                            " Try again!" + bcolors.ENDC)
                        continue
                except:
                    print(bcolors.FAIL + '\'you Can Only Enter Numbers\'' + bcolors.ENDC)
                    continue
                break
            self.half_modular.append(self.half_modular_marks)

        self.half_modular = list(map(lambda x: x * 0.5, self.half_modular))
        return self.half_modular

# Last function will do the main calculation part and will print the result whit conditional operators.
    def final_calculate(self):
        # By using this block of codes, all values of the list been added (final_marks) together.
        final_marks = self.four_modular + self.three_modular + self.two_modular + self.one_modular + self.half_modular
        sum_num = 0
        for i in final_marks:
            sum_num += i

        math1 = self.four_modular_count * 4 + self.three_modular_count * 3
        math2 = self.two_modular_count * 2 + self.one_modular_count * 1 + self.half_modular_count * 0.5
        sum_ele = math1 + math2
        # If user kept entering zero, in order to avoid ZeroDivisionError we use sys.exit() method.
        if sum_ele == 0:
            print(
                bcolors.FAIL + bcolors.BOLD + 'Oops! Your final mark is 0 obviously.'
                                              ' You\'re beyond saving.' + bcolors.ENDC)
            sys.exit()

        if sum_num / sum_ele > 17.0:
            print(bcolors.OKGREEN + 'Your final mark is: ', str(sum_num / sum_ele) + bcolors.ENDC)
        elif sum_num / sum_ele < 12.0:
            print(bcolors.FAIL + 'Your final mark is: ', str(sum_num / sum_ele) + bcolors.ENDC)
        else:
            print(bcolors.OKBLUE + 'Your final mark is: ', str(sum_num / sum_ele) + bcolors.ENDC)
