# -*- coding: utf-8 -*-
'''A palindromic number reads the same both ways. The smallest 6 digit palindrome made from the product of two 3-digit numbers is 101101=143×707. 

Find the largest palindrome made from the product of two 3-digit numbers which is less than N.'''

''' number of test cases '''
def ispalindrome(number):
    orignumber = number
    palnumber = ''
    while number > 0:
        palnumber = palnumber+`(number%10)`;
        number = number/10;
    if int(palnumber) == orignumber:
        return True
    return False

Ts = raw_input('')
T = int(Ts) 
caseN = list()
for i in range(T):
    caseN.append(long(raw_input('')))    
elevenMult = range(90,9,-1)
for N in caseN:
    max = 0
    for i in elevenMult:
        found = False
        for j in range(999,99,-1):
            candidate = i*j*11
            if candidate > max and candidate/100000 > 0 and candidate < N:
                if (ispalindrome(candidate)): 
                    found = True
                    break
        if found and max < candidate:
            max = candidate            
    print max
                        


    