def palindromeIndex(s):
    for i in range(len(s)):
        l, r, skip = 0, len(s)-1, False
        while l<r:
            if l==i:
                l+=1
            if r==i:
                r-=1
            if s[l] != s[r]:
                skip = True
                break
            l+=1
            r-=1
        if skip == False:
            return i
    return -1

str = input("Enter a string: ")
res = palindromeIndex(str)
if res == -1 :
    print("String cannot be converted to a palindrome by removing one letter.")
else:
    print("String can be converted to a palindrome by removing the letter at index position '",res,"':")
    print(str[:res]+str[res+1:])
    