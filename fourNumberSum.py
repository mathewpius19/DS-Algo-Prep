# O(n^3) Time | O(N^2) Space
def fourNumberSum(array, targetSum):
    array.sort()
    result = []
    for i in range(len(array) - 3):
        for j in range(i + 1, len(array) - 2):
            left = j + 1
            right = len(array) - 1
            while left < right:
                potentialSum = array[i] + array[j] + array[left] + array[right]
                if potentialSum == targetSum:
                    result.append([array[i], array[j], array[left], array[right]])
                    left += 1
                    right -= 1
                elif potentialSum < targetSum:
                    left += 1
                else:
                    right -= 1
    return result if len(result) != 0 else []


print(fourNumberSum([7, 6, 4, -1, 1, 2], 16))
