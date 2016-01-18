'''Find the difference between the sum of the squares of the first N natural numbers and the square of the sum.'''
Ts = raw_input('')
T = int(Ts) 
caseN = list()
for i in range(T):
    caseN.append(long(raw_input('')))
for N in caseN:
    sumOfSquare = N*(N+1)*(2*N+1)/6
    squareSum = N*(N+1)/2    
    print squareSum*squareSum - sumOfSquare