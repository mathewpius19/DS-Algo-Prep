# O(N^2) Time | O(1) Space
def selectionSort(array):
    currentIdx = 0
    while currentIdx < len(array)-1:
        smallIdx = currentIdx
        for i in range(currentIdx+1, len(array)):
            if(array[smallIdx] > array[i]):
                smallIdx = i
        swap(currentIdx, smallIdx, array)
        currentIdx+=1
    return array

def swap(i,j,array):
    array[i], array[j] = array[j], array[i]

print(selectionSort([8,5,2,9,5,6,3]))