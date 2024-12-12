def twoSum(nums, target):
    prev = {}
    for i in range(len(nums)):
        minus = target - nums[i]
        if minus in prev:
            return[prev[minus],i]
        else:
            prev[nums[i]] = i

length = int(input("Enter length of list: "))
nums = []
for i in range(length):
    a = int(input("Enter element: "))
    nums.append(a)
target = int(input("Enter target amount: "))

print("The two numbers which add up to form target amount are at index positions: ",twoSum(nums,target))