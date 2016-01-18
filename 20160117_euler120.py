# -*- coding: utf-8 -*-
'''Consider the remainder when (a−1)n+(a+1)n is divided by ae.

For example, if a=7, e=2 and n=3, then 63+83=728≡42(mod49), so the remainder is 42. And as n varies, so too will the remainder, but for a=7 and e=2 it turns out that the maximum remainder is 42.

Let R(a,e) be the largest remainder when (a−1)n+(a+1)n is divided by ae, among all n≥0.

Given A and e, find
∑a=1AR(a,e)
Since this value can be very large, output it modulo 109+7.

Input Format

The first line of input contains T, the number of test cases.

Each test case consists of a single line containing two integers, A and e.

Constraints

1≤T≤10000 
e∈{2,3} 
A≥1

For test cases worth 1/3 of the total score, A≤103. 
For test cases worth 2/3 of the total score, A≤106. 
For test cases worth 3/3 of the total score, A≤109.

Output Format

For each test case, output a single line containing the requested sum modulo 109+7.'''
T = int(raw_input(''))
Ae = raw_input('')
AeArr = Ae.split(' ')
A = int(AeArr[0])
e = int(AeArr[1])
a = 1
while a <= A:
    sumval = (pow(a - 1,
    a = a + 1