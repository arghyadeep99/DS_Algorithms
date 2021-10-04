'''
Given a rod of length n inches and an array of prices that includes prices 
of all pieces of size smaller than n. Determine the maximum value obtainable 
by cutting up the rod and selling the pieces.
'''

def cutRod(price, n):
    if n <= 0:
        return 0
    max_price = float('-inf')

    for i in range(n):
        max_price = max(max_price, price[i] + cutRod(price, n - i - 1))

    return max_price


unit_prices = [3,5,8,9,10,17,17,20]
print("Maximum price obtainable for cutting thr rod is: ", cutRod(unit_prices, len(unit_prices)))
