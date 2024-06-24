# Time O(mn) | Space O(m)
def canSum(targetSum, array, memo={}):
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return True
    if targetSum < 0:
        return False
    for num in array:
        diff = targetSum - num
        if canSum(diff, array, memo) == True:
            memo[targetSum] = True
            return True
    memo[targetSum] = False
    return False


print(canSum(7, [5, 3, 4, 7]))
print(canSum(300, [7, 14]))
