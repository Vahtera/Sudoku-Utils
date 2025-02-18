# Sandwich Sudoku size calculator
# By Anna Vahtera 2020-2025
#
# Calculates the Minimum and Maximum
# number of sells for a given sum.
#

import sys
import os

if (sys.platform == "win32"):
    os.system('color')
    
if (sys.platform == "linux" or sys.platform == "linux2"):
	print()
	    
if (sys.platform == "darwin"):
	print()
	
arguments = len(sys.argv) - 1

def checkErrors(tSum):
    if (tSum > 35):
        print("A sandwhich clue must be " + '\033[91m' + "35 or lower" + '\033[39m' + ", other sums are not possible in Sudoku.")
        sys.exit()
    if (35 - tSum == 1) or (tSum == 1):
        print("Impossible sum, you can't have a cell valued 1 outside or inside the sandwich.")
        print("The borders of the sandwich are made from 1 and 9 and those are not counted in the sum.")
        sys.exit()

if (arguments != 1):
    print()
    print("You must use exactly " + '\033[91m' + "one" + '\033[39m' + " argument as the sum of the sandwich.")
    #print('\033[39m') 
    sys.exit()

if (sys.argv[1].isnumeric()):
    cageSum = int(sys.argv[1])
else:
    print("Make sure you only enter numbers for the argument.")
    sys.exit()

maxDigits = 7
tempSum = 0
tempSum2 = 0
minSize = 1
maxSize = 7

for u in range(maxDigits):
    tempSum = tempSum + (u + 2)
    if (tempSum > cageSum):
        maxSize = u
        break

for u in range (maxDigits):
    tempSum2 = tempSum2 + (8 - u)
    if (tempSum2 >= cageSum):
        minSize = (u + 1)
        break

print()

checkErrors(cageSum)

if (maxSize != minSize):
    print('\033[92m' + "Minimun " + '\033[39m' + "size of sandwich is " + '\033[97m' + str(minSize) + '\033[39m' + ".")
    print('\033[91m' + "Maximum " + '\033[39m' + "size of sandwich is " + '\033[97m' + str(maxSize) + '\033[39m' + ".")
    print()
    print("There are " + str(maxDigits - maxSize) + " to " + str(maxDigits - minSize) + " cells outside of the sandwich.")
else:
    print("The sandwich must have exactly " + str(minSize) + " cell(s) in it, with a total of " + str(cageSum) + ".")
    print("There are exactly " + str(maxDigits - minSize) + " cell(s) outside of the sandwich.")
print("Sum of the cells outside of sandwich is " + '\033[97m' + str(35 - cageSum) + '\033[39m' + ".")