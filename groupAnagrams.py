def groupAnagrams(words):
    somedict = {}
    for word in words:
        chars = "".join(sorted(word))
        if chars in somedict:
            somedict[chars].append(word)
        else:
            somedict[chars] = [word]
    resultant = [group for group in somedict.values()]
    return resultant, somedict


print(groupAnagrams(["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]))
