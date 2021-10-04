'''
Given two natural number n and m. The task is to find the number of ways in 
which the numbers that are greater than or equal to m can be added to get the sum n.
'''

def sumNUsingM(n,m):

    dp_table = [[0 for i in range(n+2)] for j in range(n+2)]

    dp_table[0][n+1] = 1

    for i in range(n, m-1, -1):
        for j in range(n+1):
            dp_table[j][i] = dp_table[j][i+1]

            if j-i >= 0:
                dp_table[j][i] = dp_table[j][i] + dp_table[j-i][i]

    return dp_table[n][m]

n,m = 5,2
print(sumNUsingM(n,m))
