def runLengthEncoding(string):
    # Write your code here.
    encodedCharacters = []
    length = 1
    for i in range(1, len(string)):
        currentChar = string[i]
        previousChar = string[i - 1]
        if currentChar != previousChar or length == 9:
            encodedCharacters.append(str(length))
            encodedCharacters.append(previousChar)
            length = 0
        length += 1

    encodedCharacters.append(str(length))
    encodedCharacters.append(string[len(string) - 1])
    return "".join(encodedCharacters)


print(runLengthEncoding("AAAAAAAAAAAAABBCCCCDD"))
