'''What is the N'th prime number?'''
import math
def isPrime(N):
    x = 3    
    while x <= int(math.sqrt(N)):
        if (N%x == 0):
            N = int(N/x)
            return False
        else:
            x = x + 2
    return True            
    
Ts = raw_input('')
T = int(Ts) 
caseN = list()
for i in range(T):
    caseN.append(long(raw_input('')))
primeNumbers = list()
maxN = max(caseN)
primeNumbers.append(2)
primeNumbers.append(3)
count = 2
candidate = 3
while True:        
    if count == maxN:
        break
    candidate = candidate + 2   
    if (isPrime(candidate)):
        primeNumbers.append(candidate)
        count = count + 1   
for i in caseN:
    print primeNumbers[i-1] 


    