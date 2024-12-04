def is_palindrome(s, l, r):
    while l < right:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True

def palindromeIndex(s):
    l, r = 0, len(s) - 1
    
    while l < r:
        if s[l] != s[r]:
            if is_palindrome(s, l + 1, r):
                return l
            elif is_palindrome(s, l, r - 1):
                return r
            else:
                return -1
        l += 1
        r -= 1
    return -1

str = input("Enter a string: ")
res = palindromeIndex(str)
if res == -1 :
    print("String cannot be converted to a palindrome by removing one letter.")
else:
    print("String can be converted to a palindrome by removing the letter at index position '",res,"':")
    print(str[:res]+str[res+1:])
    