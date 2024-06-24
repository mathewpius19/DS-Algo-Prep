def uniqueIntegers(num):
    arr = [x for x in str(num)]
    countInt = {}
    for value in arr:
        if value not in countInt:
            countInt[value] = 1
        else:
            countInt[value] += 1

    count = 0
    for value in countInt.values():
        if value > 1:
            count += 1
    return count


print(uniqueIntegers(578378923))
