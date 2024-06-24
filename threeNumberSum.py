# O(N^2) Time | O(N) Space
def threeNumberSum(array, targetSum):
    # Write your code here.
    array.sort()
    result = []
    for i in range(len(array) - 2):
        left = i + 1
        right = len(array) - 1
        while left < right:
            potentialSum = array[i] + array[left] + array[right]
            if potentialSum == targetSum:
                result.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
            elif potentialSum < targetSum:
                left += 1
            elif potentialSum > targetSum:
                right -= 1
    return result


print(threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6], 0))
