def diagonalSum(mat):
    sum = 0
    for i in range(len(mat)):
        sum += mat[i][i] + mat[i][len(mat)-1-i]
    if len(mat) %2 != 0:
        sum -= mat[len(mat)//2][len(mat)//2]
    return sum

size = int(input("Enter size of square matrix: "))
mat=[]
for i in range(size):
    row = []
    for j in range(size):
        elem = int(input("Enter element ("+str(i)+','+str(j)+"): "))
        row.append(elem)
    mat.append(row)

print("Sum of diagonals is: ",diagonalSum(mat))