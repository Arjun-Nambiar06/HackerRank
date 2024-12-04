def jumpingOnClouds(c):
    i=jump=0
    while i < len(c)-1:
        if i+2 < len(c) and c[i+2]==0:
            i+=2
            jump+=1
        elif i+1 and c[i+1]==0:
            i+=1
            jump+=1
        else:
            print("Cannot reach end point.")
            break
    return jump

c=[]
length = int(input("Enter the size of array: "))
for i in range(length):
    b = int(input("Enter a value (0/1): "))
    c.append(b)
print("The array is: ",c)
print("The minimum number of jumps required is: ",jumpingOnClouds(c))