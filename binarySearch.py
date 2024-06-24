# O(log(N)) Time | O(1) Space
def binarySearch(arr, target):
    array = sorted(arr)
    left = 0
    right = len(array)-1
    while left <= right:
        mid = int((left+right)/2)
        if(array[mid]==target):
            return mid
        elif array[mid]<target:
            left = mid+1
        elif array[mid]>target:
            right = mid-1
    return 0

print(binarySearch([1,3,2,4,6,5], 3))