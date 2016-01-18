'''Find the greatest product of K consecutive digits in the N digit number.

Input Format 
First line contains T that denotes the number of test cases. 
First line of each test case will contain two integers N & K.
Second line of each test case will contain a N digit integer. '''
Ts = raw_input('')
T = int(Ts)  
caseNK = list()
caseNum = list()
for i in range(T):
    caseNK.append((raw_input('')))
    caseNum.append((raw_input('')))
for i in range(len(caseNK)):
    input = caseNK[i]
    NK = input.split(' ')
    N = int(NK[0])
    K = int(NK[1])
    Num = caseNum[i]
    maxProduct = -1
    for p in range(len(Num)-K+1):
        product = 1
        for x in range(K):
            product = product*int(Num[p+x])         
        if product > maxProduct:
            maxProduct = product
    print maxProduct
        
    