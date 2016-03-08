# -*- coding: utf-8 -*-
'''By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 2323. The path is denoted by numbers in bold.

33 
7474 
246246 
85938593

That is, 3+7+4+9=233+7+4+9=23.

Find the maximum total from top to bottom of the triangle given in input.

Input Format 
First line contains TT, the number of testcases. For each testcase: 
First line contains NN, the number of rows in the triangle. 
For next NN lines, ii'th line contains ii numbers.

Output Format 
Print the required answer for each testcase on a new line.

Constraints 
1≤T≤101≤T≤10 
1≤N≤1001≤N≤100 
Each element of triangle lies between 00 and 100100(both inclusive).

1
2 3
4 5 6

'''
T = int(raw_input('')) # Test cases
for i in range(T):
    N = int(raw_input('')) # Number of lines in the test case
    matrix = [[0 for x in range(N)] for x in range(N)]
    for j in range(N):
        numbers = raw_input('').split(' ') # On each line specify the input numbers
        count = 0
        for k in numbers:
            matrix[j][count] = int(k)
            count += 1
    for i in range(N-2,-1,-1):# bottom up parsing
        for j in range(i+1):
            matrix[i][j] += max(matrix[i+1][j], matrix[i+1][j+1]);
    print max(max(matrix))