"""
    Program: Calculating Average Mark
    Author: sina vahabi
    Copyright: 2023/02
    'Version 1.0'
"""

from Classes.Colors.color import bcolors
import sys


print(bcolors.BOLD + bcolors.OKBLUE + "let's start calculating your mark. ['Version 1.0']" + bcolors.ENDC + '\n')

run = True
current = 1
division_values, one_modular, two_modular, three_modular, four_modular, final_marks = [], [], [], [], [], []

while run:
    if current == 5:
        run = False
    else:
        # using try except method give us the ensurance that entering a wrong input won't crash or stop our program.
        while True:
            global count_input
            try:
                # Here we take counts of each X modular lessons count from user.
                count_input = int(input(bcolors.OKGREEN + 'Enter ' + str(current) + ' modular lessons count: '
                                        + bcolors.ENDC))
                if count_input < 0:
                    print(bcolors.BOLD + bcolors.FAIL + 'something went wrong!, seems like you have entered'
                                                        ' an unusual number!' + bcolors.ENDC)
                    continue
                if current == 1:
                    if count_input > 10:
                        print(bcolors.FAIL + bcolors.BOLD + 'something went wrong!, seems like you have entered'
                                                            ' an unusual number!' + bcolors.ENDC)
                        continue
                if current == 2:
                    if count_input > 8:
                        print(bcolors.FAIL + bcolors.BOLD + 'something went wrong!, seems like you have entered'
                                                            ' an unusual number!' + bcolors.ENDC)
                        continue
                if current == 3:
                    if count_input > 6:
                        print(bcolors.FAIL + bcolors.BOLD + 'something went wrong!, seems like you have entered'
                                                            ' an unusual number!' + bcolors.ENDC)
                        continue
                if current == 4:
                    if count_input > 4:
                        print(bcolors.FAIL + bcolors.BOLD + 'something went wrong!, seems like you have entered'
                                                            ' an unusual number!' + bcolors.ENDC)
                        continue
                division_values.append(count_input)
            except:
                print(bcolors.FAIL + '\'Please Just Enter an Integer Number\'' + bcolors.ENDC)
                continue
            break
        # Then by using for statement we take each count as end of our range() in order to get
        # X modular lessons marks from user.
        for items in range(0, count_input):
            # using try except method give us the ensurance that entering a wrong input won't crash or stop our program.
            while True:
                global mark_input
                try:
                    counter = items + 1
                    mark_input = float(input(bcolors.OKBLUE + 'Enter lesson number ' + str(counter) + ' mark from '
                                             + str(current) + ' modular lessons: ' + bcolors.ENDC))

                    if mark_input > 20:
                        print(bcolors.FAIL + bcolors.BOLD + "Your lesson mark must be between 0-20."
                                                            " Try again!" + bcolors.ENDC)
                        continue
                    if mark_input < 0:
                        print(bcolors.FAIL + bcolors.BOLD + "Your lesson mark must be between 0-20."
                                                            " Try again!" + bcolors.ENDC)
                        continue
                except:
                    print(bcolors.FAIL + '\'you Can Only Enter Numbers\'' + bcolors.ENDC)
                    continue
                break

            if current == 1:
                one_modular.append(mark_input)
            if current == 2:
                two_modular.append(mark_input)
            if current == 3:
                three_modular.append(mark_input)
            if current == 4:
                four_modular.append(mark_input)

        current += 1

# Calculating each X modular lessons marks by multiplying them.
one_modular = list(map(lambda x: x * 1, one_modular))
two_modular = list(map(lambda x: x * 2, two_modular))
three_modular = list(map(lambda x: x * 3, three_modular))
four_modular = list(map(lambda x: x * 4, four_modular))
final_marks = four_modular + three_modular + two_modular + one_modular
sum_divisions = division_values[0]*1 + division_values[1]*2 + division_values[2]*3 + division_values[3]*4


# By Defining this function we have a list (final_marks) which has sum of all X modular lessons Mark's in it.
# Also, this function will print the result with conditional operators.
def calculation():
    numbers_sum = 0
    for i in final_marks:
        numbers_sum += i

    # If user kept entering zero, in order to avoid ZeroDivisionError we use sys.exit() method.
    if sum_divisions == 0:
        print(bcolors.FAIL + bcolors.BOLD + 'Oops! Your final mark is 0 obviously.'
                                            ' You\'re beyond saving.' + bcolors.ENDC)
        sys.exit()

    calculated_mark = numbers_sum / sum_divisions

    if calculated_mark > 17.0:
        print(bcolors.OKGREEN + 'Your final mark is: ', str(calculated_mark) + bcolors.ENDC)
    elif calculated_mark < 12.0:
        print(bcolors.FAIL + 'Your final mark is: ', str(calculated_mark) + bcolors.ENDC)
    else:
        print(bcolors.OKBLUE + 'Your final mark is: ', str(calculated_mark) + bcolors.ENDC)


# Calling the function to do the last action of our program.
calculation()
