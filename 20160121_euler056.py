# -*- coding: utf-8 -*-
'''This problem is a programming version of Problem 56 from projecteuler.net

A googol (10100) is a massive number: one followed by one-hundred zeros. 100100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, ab, where a,b<N, what is the maximum digital sum?

Input Format 
Input contains an integer N

Output Format 
Print the answer corresponding to the test case.

Constraints 
5≤N≤200'''
N = int(raw_input(''))
maxval = 0
for a in range(1,N):
    for b in range(1,N):
        val = pow(a,b)
        valstr = str(val)
        total = 0
        for i in valstr:
            total += int(i)
            if (total > maxval):
                maxval = total
print maxval