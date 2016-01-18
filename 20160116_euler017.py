'''The numbers 1 to 5 written out in words are One, Two, Three, Four, Five

First character of each word will be capital letter for example: 
104382426112 is One Hundred Four Billion Three Hundred Eighty Two Million Four Hundred Twenty Six Thousand One Hundred Twelve

Given a number, you have to write it in words.

Input Format 
The first line contains an integer T , i.e., number of test cases. 
Next T lines will contain an integer N.
Output Format 
Print the values corresponding to each test case.'''
d= dict()
s = "One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen Twenty"
sArr = s.split(" ")
count = 1
for i in sArr:    
    if count < 21:
        d[count] = i
        count = count + 1
d[30] = 'Thirty'
d[40] = 'Forty'
d[50] = 'Fifty'
d[60] = 'Sixty'
d[70] = 'Seventy'
d[80] = 'Eighty'
d[90] = 'Ninety'
tx = [20,30,40,50,60,70,80,90]
for i in tx:
    for j in range(1,10):
        si = i+j
        d[si] = d[i]+" "+ d[j]
d[100] = 'Hundred'
d[1000] = 'Thousand'
d[1000000] = 'Million'
d[1000000000] = 'Billion'
T = int(raw_input(''))
caseN = list()
for i in range(T):
    caseN.append(int(raw_input('')))    
for N in caseN:
    word = ''
    t1 = N%100
    N = (N - t1)/100
    if t1 > 0:
        word = d[t1]
    hun1 = N%10
    N = (N-hun1)/10
    if hun1 > 0:
        word = d[hun1] +" " +d[100]+" " + word
    t2 = N%100
    N = (N - t2)/100
    if t2 > 0:
        word = d[t2] + " "+d[1000]+" " + word        
    hun3 = N%10
    N = (N-hun3)/10
    if hun3 > 0:
        word = d[hun3] +" " +d[100]+" " + word
    t4 = N%100
    N = (N - t4)/100
    if t4 > 0:
        word = d[t4] + " "+d[1000000]+" " + word    
    hun5 = N%10
    N = (N-hun5)/10
    if hun5 > 0:
        word = d[hun5] +" " +d[100]+" " + word
    t6 = N%100
    N = (N - t6)/100
    if t6 > 0:
            word = d[t6] + " "+d[1000000000]+" " + word
    hun7 = N%10
    N = (N-hun7)/10
    if hun7 > 0:
        word = d[hun7] +" " +d[100]+" " + word
    print word
        
        
        