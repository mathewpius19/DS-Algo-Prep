def romanToInt(roman):
    arr = [x for x in roman]
    lookupDict = {
        "M": 1000,
        "CM": 900,
        "D": 500,
        "CD": 400,
        "C": 100,
        "XC": 90,
        "L": 50,
        "XL": 40,
        "X": 10,
        "IX": 9,
        "V": 5,
        "IV": 4,
        "I": 1,
    }
    result = 0
    i = 0
    while i < len(arr) - 1:
        value = arr[i] + arr[i + 1]
        if value in lookupDict:
            result += lookupDict[value]
            i += 2
            continue
        if arr[i] in lookupDict:
            result += lookupDict[arr[i]]
            i += 1
    result += lookupDict[arr[i]]
    return result


print(romanToInt("XXXVI"))
