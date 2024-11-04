def MinMaxSum(arr):
    arr.sort()
    print("Minimum sum is: ", sum(arr)-arr[-1], "\nMaximum sum is: ", sum(arr)-arr[0])

n=int(input("Enter no. of elements: "))
arr=[]
for i in range(n):
    a=int(input("Enter an integer element: "))
    arr.append(a)
MinMaxSum(arr)    