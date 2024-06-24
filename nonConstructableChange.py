# O(Nlog(N)) Time | O(1) Space
def nonConstructibleChange(coins):
	if len(coins)<1:
		return 1
	coinsSorted = sorted(coins)
	currentChange = 0
	for i in range(len(coinsSorted)):
		if coinsSorted[i]<=currentChange+1:
			currentChange+=coinsSorted[i]
		else:
			return currentChange+1
	return currentChange+1
	
		
print(nonConstructibleChange([5, 7, 1, 1, 2, 3, 22]))