from AverageMiniProject.Version_1.Version_1_1.input import Input, bcolors
import sys


# After Calculate class inheritance from Input class we define our methods.
class Calculate(Input):
    numbers_sum = 0
    sum_divisions = 0
    calculated_mark = 0

    # Calculating each X modular lessons marks by multiplying them.
    def do_math(self):
        self.one_modular = list(map(lambda x: x * 1, self.one_modular))
        self.two_modular = list(map(lambda x: x * 2, self.two_modular))
        self.three_modular = list(map(lambda x: x * 3, self.three_modular))
        self.four_modular = list(map(lambda x: x * 4, self.four_modular))
        self.final_marks = self.four_modular + self.three_modular + self.two_modular + self.one_modular
        self.sum_divisions = (self.division_values[0] * 1 + self.division_values[1] * 2 + self.division_values[2] * 3 +
                              self.division_values[3] * 4)

    # By Defining this method we have a list (final_marks) which has sum of all X modular lessons Mark's in it.
    def final_math(self):
        for i in self.final_marks:
            self.numbers_sum += i

        # If user kept entering zero, in order to avoid ZeroDivisionError we use sys.exit() method.
        if self.sum_divisions == 0:
            print(bcolors.FAIL + bcolors.BOLD + 'Oops! Your final mark is 0 obviously.'
                                                ' You\'re beyond saving.' + bcolors.ENDC)
            sys.exit()

        self.calculated_mark = self.numbers_sum / self.sum_divisions
        return self.calculated_mark
