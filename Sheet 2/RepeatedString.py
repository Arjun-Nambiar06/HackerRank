def repeatedString(s, n):
    length=len(s)
    rem=n%length
    c1=s.count('a')
    c2=s[:rem].count('a')
    return c1*(n//length)+c2    

string=input("Enter a string: ")
n=int(input("Enter the number of characters to consider: "))
print("\nThe number of times 'a' occurs within ",n," characters is: ",repeatedString(string,n))