from collections import defaultdict
def subarraysDivByK(nums,k):
    dct = defaultdict(int)
    dct[0] = 1
    sum,count = 0,0
    for i in range(len(nums)):
        sum += nums[i]
        remainder = sum % k
        if remainder in dct:
            count += dct[remainder]
        dct[remainder] += 1
    return count

divisor = int(input("Enter divisor: "))
length = int(input("Enter length of list: "))
nums = []
for i in range(length):
    a = int(input("Enter element: "))
    nums.append(a)
print(subarraysDivByK(nums,divisor),'sums of combinations of elements are divisible by',divisor)