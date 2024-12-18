def threeSumClosest(nums,target):
    nums.sort()
    closest = nums[0] + nums[1] + nums[2]
    for i in range(len(nums)-2):
        j,k = i+1,len(nums)-1
        while j<k:
            sum = nums[i] + nums[j] + nums[k]
            if abs(closest-target) > abs(sum-target):
                closest = sum
            if sum == target:
                return sum
            elif sum < target:
                j+=1
            else: k-=1
    return closest

target = int(input("Enter target: "))
length = int(input("Enter length of list: "))
nums = []
for i in range(length):
    a = int(input("Enter element: "))
    nums.append(a)
print('The closest sum to target is: ',threeSumClosest(nums,target))