from Classes.Colors.color import bcolors


# Instantiating Input class.
class Input:
    def __init__(self):
        self.run = True
        self.current = 1
        self.count_input, self.mark_input = 0, 0
        self.one_modular, self.two_modular, self.three_modular, self.four_modular = [], [], [], []
        self.division_values, self.final_marks = [], []

    # Defining a method (get_input(self)) to get counts of each X modular lessons count from user.
    def get_input(self):
        while self.run:
            if self.current == 5:
                self.run = False
            else:
                # using try except method give us the ensurance that entering a wrong input won't crash our program.
                while True:
                    try:
                        self.count_input = int(input(bcolors.OKGREEN + 'Enter ' + str(self.current) +
                                                     ' modular lessons count: ' + bcolors.ENDC))
                        if self.count_input < 0:
                            print(bcolors.BOLD + bcolors.FAIL + 'something went wrong!, seems like you have entered'
                                                                ' an unusual number!' + bcolors.ENDC)
                            continue
                        if self.current == 1:
                            if self.count_input > 10:
                                print(bcolors.FAIL + bcolors.BOLD + 'something went wrong!, seems like you have entered'
                                                                    ' an unusual number!' + bcolors.ENDC)
                                continue
                        if self.current == 2:
                            if self.count_input > 8:
                                print(bcolors.FAIL + bcolors.BOLD + 'something went wrong!, seems like you have entered'
                                                                    ' an unusual number!' + bcolors.ENDC)
                                continue
                        if self.current == 3:
                            if self.count_input > 6:
                                print(bcolors.FAIL + bcolors.BOLD + 'something went wrong!, seems like you have entered'
                                                                    ' an unusual number!' + bcolors.ENDC)
                                continue
                        if self.current == 4:
                            if self.count_input > 4:
                                print(bcolors.FAIL + bcolors.BOLD + 'something went wrong!, seems like you have entered'
                                                                    ' an unusual number!' + bcolors.ENDC)
                                continue
                        self.division_values.append(self.count_input)
                    except:
                        print(bcolors.FAIL + '\'Please Just Enter an Integer Number\'' + bcolors.ENDC)
                        continue
                    break

                # Then by using for statement we take each count as end of our range() in order to get
                # X modular lessons marks from user.
                for items in range(0, self.count_input):
                    # using try except method give us the ensurance that entering a wrong input won't crash our program.
                    while True:
                        try:
                            counter = items + 1
                            self.mark_input = float(input(bcolors.OKBLUE + 'Enter lesson number ' + str(counter) +
                                                          ' mark from ' + str(self.current) + ' modular lessons: '
                                                          + bcolors.ENDC))

                            if self.mark_input > 20:
                                print(bcolors.FAIL + bcolors.BOLD + "Your lesson mark must be between 0-20."
                                                                    " Try again!" + bcolors.ENDC)
                                continue
                            if self.mark_input < 0:
                                print(bcolors.FAIL + bcolors.BOLD + "Your lesson mark must be between 0-20."
                                                                    " Try again!" + bcolors.ENDC)
                                continue
                        except:
                            print(bcolors.FAIL + '\'you Can Only Enter Numbers\'' + bcolors.ENDC)
                            continue
                        break

                    if self.current == 1:
                        self.one_modular.append(self.mark_input)
                    if self.current == 2:
                        self.two_modular.append(self.mark_input)
                    if self.current == 3:
                        self.three_modular.append(self.mark_input)
                    if self.current == 4:
                        self.four_modular.append(self.mark_input)

                self.current += 1
