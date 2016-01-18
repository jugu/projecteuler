'''Work out the first ten digits of the sum of N 50-digit numbers.

Input Format 
First line contains N, next N lines contain a 50 digit number each.

Output Format 
Print only first 10 digit of the final sum'''
Ts = raw_input('')
T = int(Ts) 
caseN = list()
for i in range(T):
    caseN.append(raw_input(''))    
total = long(0)
for N in caseN:
    total = total + long(N)
totalstr = str(total)
print totalstr[0:10]