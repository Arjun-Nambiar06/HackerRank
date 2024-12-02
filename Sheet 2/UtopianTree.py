def utopianTree(n):
    h = 1
    for i in range(1,n+1):
        if i%2 == 0:
            h += 1
        else:
            h *= 2
    return h

N = int(input("Enter the total number of entries: "))

for i in range(N):
    cycle = int(input("Enter the number of growth cycles at which the height is to be calculated: "))
    print("The height at this growth cycle is ", utopianTree(cycle),".\n")