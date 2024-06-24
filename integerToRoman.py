def intToRoman(num):
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
    result = []
    for key, value in lookupDict.items():
        while num > 0:
            if value <= num:
                result.append(key)
                num = num - value
            else:
                break
    return "".join(result)


print(intToRoman(1994))
