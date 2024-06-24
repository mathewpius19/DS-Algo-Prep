# def isPalindrome(string):
#     # Write your code here.
#     palCheck = string.lower()
#     if(palCheck==palCheck[::-1]):
#         return True
#     else:
#         return False

# O(N) Time | o(1) Space
def isPalindrome(string):
    left = 0
    right = len(string)-1
    for i in range(len(string)):
        if(string[left]!=string[right]):
            return False
        else:
            left+=1
            right-=1
    return True

print(isPalindrome("malayalam"))
