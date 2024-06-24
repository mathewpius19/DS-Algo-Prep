# O(N) Time | (O(N)) Space
def caesarCipherEncryptor(string, key):
    arr = list(string)
    result = []
    string = ""
    for char in arr:
        val = ord(char) + key
        if(char>='a' and char<='z'):
            num = ((val-97)%26) + 97
            result.append(chr(num))
        elif(char>="A" and char <="Z"):
            num = ((val-65)%26) +65
            result.append(chr(num))
    return string.join(result)

print(caesarCipherEncryptor("xyz", 0))