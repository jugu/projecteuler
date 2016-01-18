'''Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634=14+64+34+448208=84+24+04+849474=94+44+74+44
As 1 = 1^4 is not a sum it is not included. 
The sum of these numbers is 1634+8208+9474=19316.

Find the sum of all the numbers that can be written as the sum of Nth powers of their digits.

Input Format 
Input contains an integer N

Output Format 
Print the answer corresponding to the test case.'''
N = int(raw_input(''))
maxSum = 0
i = 100
d = dict()
d[0] = 0
d[1] = 1
d[2] = pow(2,N)
d[3] = pow(3,N)
d[4] = pow(4,N)
d[5] = pow(5,N)
d[6] = pow(6,N)
d[7] = pow(7,N)
d[8] = pow(8,N)
d[9] = pow(9,N)
maxRange = 600000
possRange =pow(9,N)*N
if (maxRange > possRange):
    maxRange = possRange
while i <= maxRange:
    s = str(i)
    sumx = 0
    for x in s:
        sumx = sumx + d[int(x)]    
    if sumx == i:
        maxSum = maxSum + i
    i = i+1
print maxSum
    

