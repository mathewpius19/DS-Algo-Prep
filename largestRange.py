# O(N) Time | O(N) Space
def largestRange(array):
    nums = {}
    longestRange = 0
    bestRange = []
    for num in array:
        nums[num] = True
    for num in array:
        if not nums[num]:
            continue
        nums[num] = False
        currentRange = 1
        left = num - 1
        right = num + 1
        while left in nums:
            nums[left] = False
            currentRange += 1
            left -= 1
        while right in nums:
            nums[right] = False
            currentRange += 1
            right += 1
        if longestRange < currentRange:
            longestRange = currentRange
            bestRange = [left + 1, right - 1]
    return bestRange


print(largestRange([1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]))
