'''2^9=512 and the sum of its digits is 5+1+2=8.

What is the sum of the digits of the number 2^N ?

Input Format 
The first line contains an integer T , i.e., number of test cases. 
Next T lines will contain an integer N.

Output Format 
Print the values corresponding to each test case.'''
T = int(raw_input(''))
caseN = list()
for i in range(T):
    caseN.append(int(raw_input('')))    
for N in caseN:
    val = pow(2,N)
    valstr = str(long(val))
    sumT = 0
    for i in valstr:
        sumT = sumT + int(i)
    print sumT
