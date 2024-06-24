# #Time Complexity = O(nlog(n))
# #Space Complexity = O(1)


def twoNumberSum(arr, targetSum):
    if(len(arr)==0):
        return []
    arr.sort()
    potentialSum = 0
    left = 0
    right = len(arr)-1
    while(left<right):
        potentialSum = arr[left] + arr[right]
        if(potentialSum==targetSum):
            return [arr[left], arr[right]]
        elif (potentialSum<targetSum):
            left+=1
        elif (potentialSum>targetSum):
            right-=1
	return []


print(twoNumberSum([1,2,3,4,5,6],10))
def twoSum(nums, target):
    resultDict = {}
    for i in range(len(nums)):
        potentialMatch = target - nums[i]
        if potentialMatch in resultDict:
            num1, num2 = i, resultDict[potentialMatch]
        else:
            resultDict[nums[i]] = i
    return [num1, num2]


print(twoSum([2, 7, 11, 15], 9))
print(twoSum([3, 2, 4], 6))
print(twoSum([3, 3], 6))
