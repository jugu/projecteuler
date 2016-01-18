'''The sum of the primes below 10 is 2+3+5+7=17.

Find the sum of all the primes not greater than given N.'''
import math
def isPrime(N):
    x = 3  
    sqrtval = int(math.sqrt(N)) 
    while x <= sqrtval:
        if (N%x == 0):
            return False
        else:
            x = x + 2
    return True   
 
Ts = raw_input('')
T = int(Ts) 
caseN = list()
for i in range(T):
    caseN.append(long(raw_input('')))    
maxN = max(caseN)
plist = list()
plist.append(2)
plist.append(5)
candidate = 5
d = dict()  
d[1]=0
d[2]=2
d[3]=5
d[4]=5
while candidate <= maxN:
    d[candidate] = d[candidate - 1]        
    if isPrime(candidate):
        d[candidate] = d[candidate] + candidate
    d[candidate + 1] = d[candidate]        
    candidate = candidate + 2        
arr = range(len(plist) - 1)
for N in caseN:
    print d[N]
        

    