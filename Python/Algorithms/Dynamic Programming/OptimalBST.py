def optCost(freq, i, j): 
	if j < i:	 # no elements in this subarray 
		return 0
	if j == i:	 # one element in this subarray 
		return freq[i] 
	fsum = Sum(freq, i, j) 
	
	# Initialize minimum value 
	Min = float('inf')
	
	# One by one consider all elements as root and recursively find cost of the BST, compare the cost with min and update min if needed 
	for r in range(i, j + 1): 
		cost = (optCost(freq, i, r - 1) +
				optCost(freq, r + 1, j)) 
		if cost < Min: 
			Min = cost 
	# Return minimum value 
	return Min + fsum 

def optimalSearchTree(keys, freq, n): 

	return optCost(freq, 0, n - 1) 

# A utility function to get sum of array elements freq[i] to freq[j] 
def Sum(freq, i, j): 
	s = 0
	for k in range(i, j + 1): 
		s += freq[k] 
	return s 

# Driver Code 
if __name__ == '__main__': 
	keys = [12, 10, 2] 
	freq = [8, 34, 40] 
	pair=zip(keys,freq)
	freq=[y for _,y in sorted(pair)]
	keys.sort()
	print(keys,freq)
	n = len(keys) 
	print("Cost of Optimal BST is", 
		optimalSearchTree(keys,freq, n)) 


