def ArraySum(arr):
    return sum(arr)

arr=[]
arr_count = int(input("Enter number of elements: "))
for i in range(arr_count):
    a = int(input("Enter an element: "))
    arr.append(a)
print("Sum of elements of the array is: ", ArraySum(arr))
