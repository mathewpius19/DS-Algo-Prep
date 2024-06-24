def generateDocument(characters, document):
    # Write your code here.
    characterDict = {}
    docDict = {}
    for ele in characters:
        if ele in characterDict:
            characterDict[ele] += 1
        else:
            characterDict[ele] = 1

    for ele in document:
        if ele in docDict:
            docDict[ele] += 1
        else:
            docDict[ele] = 1
    genDoc = False
    print(characterDict)
    print(docDict)
    for char in document:
        if char not in characters:
            return False
        if characterDict[char] >= docDict[char]:
            genDoc = True
        else:
            return False
    if genDoc:
        return True
    else:
        return False
print(generateDocument("aheaolabbhb", "hello"))