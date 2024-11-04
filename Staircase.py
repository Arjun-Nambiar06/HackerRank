def staircase(n):
    for i in range(1,n+1):
        print(' '*(n-i) + '#'*i)

n=int(input("Enter a number for the staircase: "))
staircase(n)