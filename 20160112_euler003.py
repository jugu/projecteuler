'''The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of a given number N?'''

''' number of test cases '''
import math
Ts = raw_input('')
T = int(Ts) 
caseN = list()
for i in range(T):
    caseN.append(long(raw_input('')))
for N in caseN:
    x = 2  
    while N%x == 0:
        N = int(N/x)
    max = N
    x = 3
    while x <= int(math.sqrt(N)):
        if (N%x == 0):
            N = int(N/x)
            max = N
        else:
            x = x + 2
    print max