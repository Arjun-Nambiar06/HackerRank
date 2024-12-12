def strStr(haystack,needle):
    if needle not in haystack:
        return -1
    else:
        return haystack.find(needle)

haystack = input("Enter text: ")
needle = input("Enter string to be searched: ")

val = strStr(haystack,needle)
if val == -1:
    print('\"'+needle+'\" not found in \"'+haystack+'\".')
else:
    print('\"'+needle+'\" found in \"'+haystack+'\" at index: ',val,'.')