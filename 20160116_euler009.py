# -*- coding: utf-8 -*-
'''Given N, Check if there exists any Pythagorean triplet for which a+b+c=N 
Find maximum possible value of abc among all such Pythagorean triplets, If there is no such Pythagorean triplet print −1. '''
Ts = raw_input('')
T = int(Ts) 
caseN = list()
for i in range(T):
    caseN.append(long(raw_input('')))    
for N in caseN:
    maxval = -1
    for a in range(1, N/3):
        b = (N*N/2 - a*N)/float(N - a)                
        if b <= 0 or b != int(b):
            continue
        c = N - a - b        
        if a*a + b*b == c*c and a*b*c > maxval:
            maxval = a*b*c
    print int(maxval)
                