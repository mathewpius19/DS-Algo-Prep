# O(N) Time | O(1) Space
def hasSingleCycle(array):
    visited = 1
    current = 0 + array[0]
    # initial check for the current value to find the index  of the next value in the array
    if current >= len(array):
        current = current % len(array)
    if current < 0:
        if abs(current) > len(array):
            value = current % len(array)
            current = value
        else:
            current = len(array) + current
    # while loop to determine whether theres a single cycle or not
    while current != 0:
        if visited > len(array):
            return False
        visited += 1  # count the number of values visited
        nextCurrent = current + array[current]
        print("nextCurrent", nextCurrent)
        if nextCurrent < 0:
            if abs(nextCurrent) > len(array):
                print("nextCurrent", nextCurrent)
                value = nextCurrent % len(array)
                print("value", value)
                current = value
                print("current value", current)
                continue
            else:
                current = len(array) + nextCurrent
                continue
        elif nextCurrent >= len(array):
            current = nextCurrent % len(array)
            continue
        current = nextCurrent

    if visited == len(array):
        return True
    else:
        return False


print(hasSingleCycle([10, 11, -6, -23, -2, 3, 88, 908, -26]))
