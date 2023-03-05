"""
    Program: Calculating Average Mark
    Author: sina vahabi
    Copyright: 2023/02
    'Version 1.0'
"""

# First we import functions from average module.
from average import (four_modular_lesson, three_modular_lessons, two_modular_lessons,
                     one_modular_lessons, half_modular_lessons, calculate)
from Classes.Colors import bcolors


print(bcolors.UNDERLINE + bcolors.OKGREEN + "let's start calculating your mark. ['Version 1.0']" + bcolors.ENDC)
# Calling our functions
four_modular_lesson()
three_modular_lessons()
two_modular_lessons()
one_modular_lessons()
half_modular_lessons()
calculate()
