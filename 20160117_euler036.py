'''The decimal number, 585=10010010012 (binary), is palindromic in both bases.

Find the sum of all natural numbers, less than N, which are palindromic in base 10 and base K.

(Please note that the palindromic number, in either base, may not include leading zeros.)

Input Format 
Input contains two integers N and K.

Output Format 
Print the answer corresponding to the test case.'''
NKs = raw_input('')
NKArr = NKs.split(' ')
N = int(NKArr[0])
K = int(NKArr[1])
NRev = ''
arr = range(1, N)
allsum = 0
for val in arr:
    N = val
    NRev=''
    while N > 0:
        NRev = NRev + str(N%10)
        N = N/10        
    if NRev != str(val):
        continue
    else:
        N = int(val)
        NRev=''
        NProp = ''
        while N > 0:
            NProp = str(N%K) + NProp
            NRev = NRev + str(N%K)
            N = N/K
        if (NProp == NRev):
            allsum = allsum + val
print allsum