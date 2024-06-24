# O(N) Time | O(1) Space
def kadanesAlgorithm(array):
    # Write your code here.
    if len(array) == 0:
        return 0
    presentSum = float("-inf")
    maxSoFar = float("-inf")
    for num in array:
        presentSum = presentSum + num
        presentSum = max(num, presentSum)
        maxSoFar = max(maxSoFar, presentSum)
    return maxSoFar


print(kadanesAlgorithm([-90]))
