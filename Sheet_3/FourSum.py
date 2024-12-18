def fourSum(nums, target):
    size = len(nums)
    nums.sort()
    final = []

    for i in range(size):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        for j in range(i+1, size):
            if j > i+1 and nums[j] == nums[j-1]:
                continue
            l, r = j+1, size-1
            while l < r:
                total = nums[i] + nums[j] + nums[l] + nums[r]
                if total > target:
                    r -= 1
                elif total < target:
                    l += 1
                else:
                    quad = [nums[i], nums[j], nums[l], nums[r]]
                    final.append(quad)
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1                        
    return final

target = int(input("Enter target: "))
length = int(input("Enter length of list: "))
nums = []
for i in range(length):
    a = int(input("Enter element: "))
    nums.append(a)
print('All combinations of four that sum to target are: \n',fourSum(nums,target))