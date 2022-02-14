#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getFinalOrder' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY amount
#

def getFinalOrder(k, amount):
    # Write your code here
    result = []
    cur_per_order= [] 
    #to store amt,balance,index using which we can sort the balance 
    #ex[1,1,0] is [amt,balance(k-amt),index]
    
    for i in range(len(amount)):
        cur_per_order.append([amount[i],math.ceil(amount[i]/k),i])  
        #using ceil to find remainder(balance)
    cur_per_order.sort(key=lambda x: x[1]) 
    #usig balance as parameter to sort
    #print(cur_per_order)
    for per in cur_per_order:
        result.append(per[2]+1) #since indexing starts at 0 we add 1 to the index values stored in current person order list
    return result

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    k = 2 #int(input().strip())

    amount_count = 3 #int(input().strip())

    amount = [2,5,1]

    # for _ in range(amount_count):
    #     amount_item = int(input().strip())
    #     amount.append(amount_item)

    result = getFinalOrder(k, amount)
    print(result)

    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
