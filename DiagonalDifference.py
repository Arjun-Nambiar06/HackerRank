def diagonalDifference(arr):
    d1=d2=0
    for i in range(len(arr)):
        d1+=arr[i][i]
        d2+=arr[i][len(arr)-i-1]
    return abs(d1-d2)

n=int(input("Enter order of square matrix: "))
arr=[]
for i in range(n):
    arr_row=[]
    for j in range(n):
        a=int(input("Enter the ["+str(i)+"]["+str(j)+"] element: "))
        arr_row.append(a)
    arr.append(arr_row)

print("The absolute value of the diagonal difference is: ", diagonalDifference(arr))