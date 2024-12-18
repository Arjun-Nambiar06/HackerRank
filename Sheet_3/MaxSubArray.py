def maxSubArray(nums):
    sum,curr = nums[0],nums[0]
    for i in nums[1:]:
        curr = max(curr+i,i)
        sum = max(sum,curr)
    return sum

length = int(input("Enter length of list: "))
nums = []
for i in range(length):
    a = int(input("Enter element: "))
    nums.append(a)
print(maxSubArray(nums))