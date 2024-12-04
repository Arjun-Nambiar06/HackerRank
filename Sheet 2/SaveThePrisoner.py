def saveThePrisoner(n, m, s):
    m -= (n-(s-1))
    m %= n
    if m == 0:
        return n
    return m

n = int(input("Enter number of prisoners: "))
m = int(input("Enter number of treats: "))
s = int(input("Enter the starting position: "))

print("The prisoner getting the bad candy is sitting at position: ", saveThePrisoner(n,m,s))