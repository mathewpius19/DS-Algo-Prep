def isValidSubsequence(array, sequence):
	if len(array)==1:
		return True
	ptr = 0
	for ele in array:
		if ele==sequence[ptr]:
			ptr+=1
		if ptr== len(sequence):
			return True
	return False

print(isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10]))