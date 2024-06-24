# O(Nlog(N) + Mlog(M)) Time | O(1)Space
def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    arrayOne.sort()
    arrayTwo.sort()
    ptr1 = 0
    ptr2 = 0
    resultPtr1 = 0
    resultPtr2 = 0
    smallest = float("inf")
    while ptr1 < len(arrayOne) and ptr2 < len(arrayTwo):
        if abs(arrayOne[ptr1] - arrayTwo[ptr2]) < smallest:
            smallest = abs(arrayOne[ptr1] - arrayTwo[ptr2])
            result1, result2 = arrayOne[ptr1], arrayTwo[ptr2]
        elif arrayOne[ptr1] < arrayTwo[ptr2]:
            ptr1 += 1
        else:
            ptr2 += 1
    return [result1, result2]


print(smallestDifference([-1, 5, 10, 20, 28, 3], [-1, 5, 10, 20, 28, 3]))
