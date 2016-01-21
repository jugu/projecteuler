# -*- coding: utf-8 -*-
'''The 5−digit number, 16807=75, is also a fifth power. Similarly, the 9-digit number, 134217728=89, is a ninth power.

Given N, print the N−digit positive integers which are also an Nth power?

Input Format 
Input contains an integer N

Output Format 
Print the answer corresponding to the test case.

Constraints 
1≤N≤19'''
import math
N = int(raw_input(''))
i = 1
while i < 12: 
    test = i**N
    val = int(math.log10(test))
    if val == N - 1:
        print test
    i = i + 1