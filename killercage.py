# This is based on code contributed by ChitraNayal 
# Modified by Anna Vahtera 2020-2025

# Killer Sudoku Cage Solver

# The main function that prints all 
# combinations of size r in arr[] of 
# size n. This function mainly uses  
# combinationUtil() 

# Original code (by ChitraNayal) for:
# Program to print all combination  
# of size r in an array of size n 

# Logic for "Killer Sudoku" Rules by Anna Vahtera


import sys
arguments = len(sys.argv) - 1
    
if (arguments != 2):
    print()
    print("You must use two arguments: [Cage Size] [Sum of Cells].")
    sys.exit()

v = int(sys.argv[2])
r = int(sys.argv[1])
cageSize = r
cageSum = v

def checkError(cSize, cSum):
    sumError = bool(False)
    if (cSize == 2) and (17 < cSum or cSum < 3):
        sumError = bool(True)
    if (cSize == 3) and (24 < cSum or cSum < 6):
        sumError = bool(True)
    if (cSize == 4) and (30 < cSum or cSum < 10):
        sumError = bool(True)
    if (cSize == 5) and (35 < cSum or cSum < 15):
        sumError = bool(True)
    if (cSize == 6) and (39 < cSum or cSum < 21):
        sumError = bool(True)
    if (cSize == 7) and (42 < cSum or cSum < 27):
        sumError = bool(True)
    if (cSize == 8) and (45 < cSum or cSum < 34):
        sumError = bool(True)

    if (cSize == 1):
        print()
        print("Single-cell cages always contain the digit equal to the sum of the cage, which must be 1-9.")
        sys.exit()

    if (cSize == 9):
        print()
        print("In a normal Killer Sudoku, all size 9 cages must include all the numbers from 1 to 9.")
        sys.exit()

    if (cSize > 9):
        print()
        print("Please check input. Cages bigger than 9 are not possible in a normal Killer Sudoku.")
        sys.exit()
    
    if sumError:
        print()
        print("Impossible combination. A size " + str(cageSize) + " cage cannot contain a sum of " + str(cageSum) + ".")
        sys.exit()



def printCombination(arr, n, r): 
  
    # A temporary array to store  
    # all combination one by one 
    data = [0] * r 
  
    # Print all combination using 
    # temprary array 'data[]' 
    combinationUtil(arr, n, r, 0, data, 0) 
  
''' arr[] ---> Input Array 
n     ---> Size of input array 
r     ---> Size of a combination to be printed 
index ---> Current index in data[] 
data[] ---> Temporary array to store 
            current combination 
i     ---> index of current element in arr[]     '''

def combinationUtil(arr, n, r, index, data, i): 
    res = 0
    combi = ""
    combi2 = ""
    # Current cobination is ready,  
    # print it 
    if (index == r): 
        arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        
        for j in range(r): 
            for u in range(len(arr2)):
                if (data[j] == arr2[u - 1]):
                    del arr2[u -1]
                                
            res = res + data[j]
            combi = combi + str(data[j])
            
        
        for u in range(len(arr2)):
            combi2 = combi2 + str(arr2[u])
            
        if (res == v):
            rString = ""
            if (cageSize > 4):
                rString = '{:13}'.format("[" + combi + "]") + " + " + '{:10}'.format("[" + combi2 + "]")
            else:
                rString = "[" + combi + "]"
                            
            print(rString.rstrip())            
            
        return
    
    # When no more elements are  
    # there to put in data[] 
    if (i >= n): 
        return
  
    # current is included, put 
    # next at next location 
    data[index] = arr[i] 
    combinationUtil(arr, n, r, index + 1,  
                    data, i + 1) 
  
    # current is excluded, replace it  
    # with next (Note that i+1 is passed,  
    # but index is not changed) 
    combinationUtil(arr, n, r, index,  
                    data, i + 1) 


checkError(cageSize, cageSum)

 
# Driver Code 
if __name__ == "__main__": 
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9] 
    n = len(arr)
    val = 45 - v
    print()

    if (cageSize == 8):
        res = 0
        res = 45 - v
        print("Cage is missing a " + str(res))
        print()
        sys.exit()

    
    if (cageSize > 4):
        print("There are " + str(9 - cageSize) + " cells outside of cage, which sum to " + str(val) + ".")
        print()
        print("Possible number combinations for cells:")
        print("[Inside Cage] + [Outside Cage]:")
    else:
        print("Possible number combinations for cells:")
    
    printCombination(arr, n, r) 
    
    print()
 