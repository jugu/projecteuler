'''What is the smallest positive number that is evenly divisible(divisible with no remainder) by all of the numbers from 1 to N?
1 <= N <= 40'''
Ts = raw_input('')
T = int(Ts) 
caseN = list()
for i in range(T):
    caseN.append(long(raw_input('')))
arr = [1,2,3,2,5,1,7,2,3,1,11,1,13,1,1,2,17,1,19,1    ,1,1,23,1,5,1,1,1,29,1,31,2,1,1,1,1,37,1,1]
for N in caseN:
    num = 1
    for i in range(N):
        num = num*arr[i]                          
    print num
        
    