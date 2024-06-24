# O(N) Time | O(1) Space, constant space because our dictionary will only have a max of 26 characters.
def firstNonRepeatingCharacter(string):
    # Write your code here.
    array = [ele for ele in string]
    charDict = {}
    for ele in array:
        if ele in charDict:
            charDict[ele] += 1
        else:
            charDict[ele] = 1
    smallIdx = float("inf")
    Nonrepeated = False
    for i in range(len(array)):
        if charDict[array[i]] < 2 and smallIdx > i:
            smallIdx = i
            Nonrepeated = True
    if Nonrepeated is False:
        return -1
    else:
        return smallIdx


print(firstNonRepeatingCharacter("abcdcaf"))
