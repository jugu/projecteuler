Ts = raw_input('')
T = int(Ts)
caseN = list()
for i in range(T):
    caseN.append(int(raw_input('')))
for N in caseN:
    tn3 = int((N-1)/3)
    tn5 = int((N-1)/5)
    tn15 = int((N-1)/15)
    s3 = (tn3)*(2*3 + (tn3-1)*3)/2
    s5 = (tn5)*(2*5 + (tn5-1)*5)/2
    s15 = (tn15)*(2*15 + (tn15-1)*15)/2
    sum = s3 + s5 - s15
    print sum