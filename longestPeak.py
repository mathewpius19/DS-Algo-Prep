def longestPeak(array):
    longestPeakLength = 0
    for i in range(1, len(array) - 1):
        isPeak = array[i] > array[i - 1] and array[i] > array[i + 1]
        if not isPeak:
            i += 1
            continue
        leftIndex = i - 2
        while leftIndex >= 0 and array[leftIndex] < array[leftIndex + 1]:
            leftIndex -= 1
        rightIndex = i + 2
        while rightIndex < len(array) and array[rightIndex] < array[rightIndex - 1]:
            rightIndex += 1

        currentPeak = rightIndex - leftIndex - 1
        maxPeak = max(longestPeakLength, currentPeak)
    return maxPeak


print(longestPeak([1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]))
