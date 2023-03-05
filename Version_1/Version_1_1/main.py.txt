"""
    Program: Calculating Average Mark (OOP)
    Author: sina vahabi
    Copyright: 2023/02
    'Version 1.1'
"""

from AverageMiniProject.Version_1.Version_1_1.calculation import Calculation


print("Time to calculate your semester average. ['Version 1.1']")
# After creating an object from calculation class, we access class's methods, and we use them to run our program.
average = Calculation()
average.four_modular_input()
average.get_four_modular_mark()
average.three_modular_input()
average.get_three_modular_mark()
average.two_modular_input()
average.get_two_modular_mark()
average.one_modular_input()
average.get_one_modular_mark()
average.half_modular_input()
average.get_half_modular_mark()
average.final_calculate()
