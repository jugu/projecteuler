# -*- coding: utf-8 -*-
'''The series,
1^1+2^2+3^3+⋯+10^10=10405071317
Find the last ten digits of the series,
1^1+2^2+3^3+⋯+N^N

Note You do not need to print leading zeros. See sample.

Input Format 
Input contains an integer N

Output Format 
Print the answer corresponding to the test case.'''
def modN(a, exp, mod):
    if (exp == 1):
        return a%mod
    if (exp%2 == 0):
        t = modN(a, exp/2, mod)
        return (t*t)%mod
    else:
        t = modN(a, exp/2, mod)
        return (a*t*t)%mod
        
N =int(raw_input(''))
total = 0
for i in range(1,N+1):
    total = total + modN(i, i, 10000000000)
print int(((str(total)[::-1])[0:10])[::-1])

