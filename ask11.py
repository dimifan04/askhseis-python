import numpy as np
import random
from itertools import chain

counter = 0
palindromos = 0
sum_of_counters = 0

for x in range(100):
    while (palindromos == 0):
        sum = 0
        #δημιουργώ μία αλυσίδα αριθμών από το 1-1000 εκτός 196 & 879
        for f in random.sample(list(chain(range(1,196), range(197,879),range(880,1001))),1):
            #print('1....FFFFF = ',f)
            temp = f
            while (f>0):
                ek = f%10
                sum = sum*10 + ek
                f = f//10
                #new_num = mon*100+dek*10+ek
            if (temp == sum):
                #print('2....',temp)
                #print('3....',sum)
                palindromos = 1
                #break
            else:
                counter = counter + 1
                #print('4....FFFFF = ',temp)
                #print('5....',sum)
                sum_1 = f + sum
                #print('sum = ', sum_1)
        sum_of_counters = sum_of_counters + counter
        #print(counter)
print('MO = ', sum_of_counters/100)