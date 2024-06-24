# O(N^2) Time | O(N)Space
def longestPalindromicSubstring(string):
    currentLongest = [0, 1]
    total = 0
    for i in range(1, len(string)):
        odd = getLongestPalindrome(string, i - 1, i + 1)
        even = getLongestPalindrome(string, i - 1, i)
        # longest = max(odd, even, key=lambda x: x[1] - x[0])
        # currentLongest = max(longest, currentLongest, key=lambda x: x[1] - x[0])
        total += odd + even
    return total + 1


def getLongestPalindrome(string, left, right):
    count = 0
    while left >= 0 and right < len(string):
        if string[left] != string[right]:
            break
        left -= 1
        right += 1
    count += (right - left) // 2
    print("right", right)
    print("left", left)
    print(count)
    return count


print(longestPalindromicSubstring("aaa"))


# def longestPalindromicSubstring1(string):
#     longest = ""
#     arr = [x for x in string]
#     for i in range(len(arr)):
#         for j in range(i, len(arr)):
#             substring = arr[i : j + 1]
#             if len(substring) > len(longest) and ifPalindrome(substring):
#                 longest = substring
#     return "".join(longest)


# def ifPalindrome(substring):
#     if substring == substring[::-1]:
#         return True
#     return False


# print(longestPalindromicSubstring("abaxyzzyxf"))
