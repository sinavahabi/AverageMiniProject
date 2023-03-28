"""
    Program: Calculating Average Mark (OOP)
    Author: sina vahabi
    Copyright: 2023/02
    'Version 1.1'
"""

# After importing essential Classes we call the final class (Calculate()) to an object called result.
from AverageMiniProject.Version_1.Version_1_1.calculation import Calculate, bcolors

print("Time to calculate your semester average. ['Version 1.1'] \n")

result = Calculate()
# Accessing (get_input()) method from Input class which Calculate class had an inheritance from it.
result.get_input()
# Accessing (do_math()) method from Calculate class which we passed tp result object.
result.do_math()
# Accessing (final_math()) method from Calculate class which we passed tp result object.
result.final_math()

# By accessing to returned value from (final_math()) method from Calculate class we use our conditional operators.
if result.calculated_mark > 17.0:
    print(bcolors.OKGREEN + 'Your final mark is: ', str(result.calculated_mark) + bcolors.ENDC)
elif result.calculated_mark < 12.0:
    print(bcolors.FAIL + 'Your final mark is: ', str(result.calculated_mark) + bcolors.ENDC)
else:
    print(bcolors.OKBLUE + 'Your final mark is: ', str(result.calculated_mark) + bcolors.ENDC)
