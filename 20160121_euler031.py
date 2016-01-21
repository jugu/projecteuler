# -*- coding: utf-8 -*-
'''In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:
1×£1+1×50p+2×20p+1×5p+1×2p+3×1p
How many different ways can N p be made using any number of coins? As the result can be large print answer mod (109+7)
Input Format 
The first line contains an integer T , i.e., number of test cases. 
Next T lines will contain an integer N.

Note: N is given as p and not £'''
T = int(raw_input(''))
caseN = list()
for i in range(T):
    caseN.append(int(raw_input('')))
coinvalues = [1,2,5,10,20,50,100,200]
for N in caseN:
    ways = [1]+[0]*N  
    for i in range(len(coinvalues)):
        j = coinvalues[i]
        while j <= N:
            ways[j] = ways[j]+ ways[j - coinvalues[i]]      
            j = j + 1
    print ways[N]
