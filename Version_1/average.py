"""
    This program has 5 functions which do almost an exact action for 5 times.
    First they capture counts of each X modular lessons and by using a loop after that,
    they make a list of lesson's marks. Also using try except method give us the ensurance that entering
    a wrong input won't crash or stop our program.
"""

import sys
from Classes.Colors import bcolors


four_modular, three_modular, two_modular, one_modular, half_modular = [], [], [], [], []
ele_num4, ele_num3, ele_num2, ele_num1, ele_num_half = 0, 0, 0, 0, 0
ele4, ele3, ele2, ele1, ele_half = 0, 0, 0, 0, 0


# defining function for 4 modular lessons. By using this function we capture counts and marks of each lesson.
def four_modular_lesson():
    global four_modular
    global ele_num4
    global ele4
    while True:
        try:
            ele_num4 = int(
                input(bcolors.BOLD + 'Enter number of your lessons for FOUR modular lessons: ' + bcolors.ENDC))
            if ele_num4 > 5:
                print(bcolors.BOLD + bcolors.FAIL + 'something went wrong!,'
                                                    ' seems like you have entered an unusual number!' + bcolors.ENDC)
                continue
            if ele_num4 < 0:
                print(bcolors.BOLD + bcolors.FAIL + 'something went wrong!,'
                                                    ' seems like you have entered an unusual number!' + bcolors.ENDC)
                continue
        except:
            print(bcolors.BOLD + bcolors.FAIL + '\'Please Just Enter an Integer Number\'' + bcolors.ENDC)
            continue
        break

    for i in range(0, ele_num4):
        while True:
            try:
                num4 = i + 1
                ele4 = float(input(bcolors.OKBLUE + 'Enter lesson number ' + str(num4) +
                                   ' mark from four modular lessons: ' + bcolors.ENDC))
                if ele4 > 20:
                    print(bcolors.FAIL + bcolors.BOLD + "Your lesson mark must be between 0-20."
                                                        " Try again!" + bcolors.ENDC)
                    continue
                if ele4 < 0:
                    print(bcolors.FAIL + bcolors.BOLD + "Your lesson mark must be between 0-20."
                                                        " Try again!" + bcolors.ENDC)
                    continue
            except:
                print(bcolors.FAIL + '\'you Can Only Enter Numbers\'' + bcolors.ENDC)
                continue
            break
        four_modular.append(ele4)

    four_modular = list(map(lambda x: x * 4, four_modular))


def three_modular_lessons():
    global three_modular
    global ele_num3
    global ele3
    while True:
        try:
            ele_num3 = int(
                input(bcolors.BOLD + 'Enter number of your lessons for THREE modular lessons: ' + bcolors.ENDC))
            if ele_num3 > 7:
                print(bcolors.BOLD + bcolors.FAIL + 'something went wrong!,'
                                                    ' seems like you have entered an unusual number!' + bcolors.ENDC)
                continue
            if ele_num3 < 0:
                print(bcolors.BOLD + bcolors.FAIL + 'something went wrong!,'
                                                    ' seems like you have entered an unusual number!' + bcolors.ENDC)
                continue
        except:
            print(bcolors.BOLD + bcolors.FAIL + '\'Please Just Enter an Integer Number\'' + bcolors.ENDC)
            continue
        break

    for i in range(0, ele_num3):
        while True:
            try:
                num3 = i + 1
                ele3 = float(input(bcolors.OKBLUE + 'Enter lesson number ' + str(num3) +
                                   ' mark from three modular lessons: ' + bcolors.ENDC))
                if ele3 > 20:
                    print(bcolors.FAIL + bcolors.BOLD + "Your lesson mark must be between 0-20."
                                                        " Try again!" + bcolors.ENDC)
                    continue
                if ele3 < 0:
                    print(bcolors.FAIL + bcolors.BOLD + "Your lesson mark must be between 0-20."
                                                        " Try again!" + bcolors.ENDC)
                    continue
            except:
                print(bcolors.FAIL + '\'you Can Only Enter Numbers\'' + bcolors.ENDC)
                continue
            break
        three_modular.append(ele3)

    three_modular = list(map(lambda x: x * 3, three_modular))


def two_modular_lessons():
    global two_modular
    global ele_num2
    global ele2
    while True:
        try:
            ele_num2 = int(
                input(bcolors.BOLD + 'Enter number of your lessons for TWO modular lessons: ' + bcolors.ENDC))
            if ele_num2 > 9:
                print(bcolors.BOLD + bcolors.FAIL + 'something went wrong!,'
                                                    ' seems like you have entered an unusual number!' + bcolors.ENDC)
                continue
            if ele_num2 < 0:
                print(bcolors.BOLD + bcolors.FAIL + 'something went wrong!,'
                                                    ' seems like you have entered an unusual number!' + bcolors.ENDC)
                continue
        except:
            print(bcolors.BOLD + bcolors.FAIL + '\'Please Just Enter an Integer Number\'' + bcolors.ENDC)
            continue
        break

    for i in range(0, ele_num2):
        while True:
            try:
                num2 = i + 1
                ele2 = float(input(bcolors.OKBLUE + 'Enter lesson number ' + str(num2) +
                                   ' mark from two modular lessons: ' + bcolors.ENDC))
                if ele2 > 20:
                    print(bcolors.FAIL + bcolors.BOLD + "Your lesson mark must be between 0-20."
                                                        " Try again!" + bcolors.ENDC)
                    continue
                if ele2 < 0:
                    print(bcolors.FAIL + bcolors.BOLD + "Your lesson mark must be between 0-20."
                                                        " Try again!" + bcolors.ENDC)
                    continue
            except:
                print(bcolors.FAIL + '\'you Can Only Enter Numbers\'' + bcolors.ENDC)
                continue
            break
        two_modular.append(ele2)

    two_modular = list(map(lambda x: x * 2, two_modular))


def one_modular_lessons():
    global one_modular
    global ele_num1
    global ele1
    while True:
        try:
            ele_num1 = int(
                input(bcolors.BOLD + 'Enter number of your lessons for ONE modular lessons: ' + bcolors.ENDC))
            if ele_num1 > 10:
                print(bcolors.BOLD + bcolors.FAIL + 'something went wrong!,'
                                                    ' seems like you have entered an unusual number!' + bcolors.ENDC)
                continue
            if ele_num1 < 0:
                print(bcolors.BOLD + bcolors.FAIL + 'something went wrong!,'
                                                    ' seems like you have entered an unusual number!' + bcolors.ENDC)
                continue
        except:
            print(bcolors.BOLD + bcolors.FAIL + '\'Please Just Enter an Integer Number\'' + bcolors.ENDC)
            continue
        break

    for i in range(0, ele_num1):
        while True:
            try:
                num1 = i + 1
                ele1 = float(input(bcolors.OKBLUE + 'Enter lesson number ' + str(num1) +
                                   ' mark from one modular lessons: ' + bcolors.ENDC))
                if ele1 > 20:
                    print(bcolors.FAIL + bcolors.BOLD + "Your lesson mark must be between 0-20."
                                                        " Try again!" + bcolors.ENDC)
                    continue
                if ele1 < 0:
                    print(bcolors.FAIL + bcolors.BOLD + "Your lesson mark must be between 0-20."
                                                        " Try again!" + bcolors.ENDC)
                    continue
            except:
                print(bcolors.FAIL + '\'you Can Only Enter Numbers\'' + bcolors.ENDC)
                continue
            break
        one_modular.append(ele1)


def half_modular_lessons():
    global half_modular
    global ele_num_half
    global ele_half
    while True:
        try:
            ele_num_half = int(
                input(bcolors.BOLD + 'Enter number of your lessons for HALF modular lessons: ' + bcolors.ENDC))
            if ele_num_half > 20:
                print(bcolors.BOLD + bcolors.FAIL + 'something went wrong!,'
                                                    ' seems like you have entered an unusual number!' + bcolors.ENDC)
                continue
            if ele_num_half < 0:
                print(bcolors.BOLD + bcolors.FAIL + 'something went wrong!,'
                                                    ' seems like you have entered an unusual number!' + bcolors.ENDC)
                continue
        except:
            print(bcolors.BOLD + bcolors.FAIL + '\'Please Just Enter an Integer Number\'' + bcolors.ENDC)
            continue
        break

    for i in range(0, ele_num_half):
        while True:
            try:
                num = i + 1
                ele_half = float(input(bcolors.OKBLUE + 'Enter lesson number ' + str(num) +
                                       ' mark from half modular lessons: ' + bcolors.ENDC))
                if ele_half > 20:
                    print(bcolors.FAIL + bcolors.BOLD + "Your lesson mark must be between 0-20."
                                                        " Try again!" + bcolors.ENDC)
                    continue
                if ele_half < 0:
                    print(bcolors.FAIL + bcolors.BOLD + "Your lesson mark must be between 0-20."
                                                        " Try again!" + bcolors.ENDC)
                    continue
            except:
                print(bcolors.FAIL + '\'you Can Only Enter Numbers\'' + bcolors.ENDC)
                continue
            break
        half_modular.append(ele_half)

    half_modular = list(map(lambda x: x * 0.5, half_modular))


# Last function will do the main calculation part and will print the result with conditional operators.
def calculate():
    # By using this block of codes, all values of the list been added (final_marks) together.
    final_marks, sum_num = four_modular + three_modular + two_modular + one_modular + half_modular, 0
    for i in final_marks:
        sum_num += i

    sum_ele = ele_num4 * 4 + ele_num3 * 3 + ele_num2 * 2 + ele_num1 * 1 + ele_num_half * 0.5

    # If user kept entering zero, in order to avoid ZeroDivisionError we use sys.exit() method.
    if sum_ele == 0:
        print(
            bcolors.FAIL + bcolors.BOLD + 'Oops! Your final mark is 0 obviously. You\'re beyond saving.' + bcolors.ENDC)
        sys.exit()

    if sum_num / sum_ele > 17.0:
        print(bcolors.OKGREEN + 'Your final mark is: ', str(sum_num / sum_ele) + bcolors.ENDC)
    elif sum_num / sum_ele < 12.0:
        print(bcolors.FAIL + 'Your final mark is: ', str(sum_num / sum_ele) + bcolors.ENDC)
    else:
        print(bcolors.OKBLUE + 'Your final mark is: ', str(sum_num / sum_ele) + bcolors.ENDC)
