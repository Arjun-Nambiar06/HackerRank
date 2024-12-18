from collections import defaultdict
def subarraySum(nums,k):
    dct = defaultdict(int)
    dct[0] = 1
    sum,ans = 0,0
    for i in range(len(nums)):
        sum += nums[i]
        ans += dct[sum - k]
        dct[sum] += 1
    return ans

target = int(input("Enter target: "))
length = int(input("Enter length of list: "))
nums = []
for i in range(length):
    a = int(input("Enter element: "))
    nums.append(a)
print('All combinations that sum to target are: \n',subarraySum(nums,target))