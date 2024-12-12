def majorityElement(nums):
    checked = set()
    for i in nums:
        if i not in checked:
            if nums.count(i) > len(nums)/2:
                return i
            checked.add(i)
    return -1


length = int(input("Enter length of list: "))
nums = []
for i in range(length):
    a = int(input("Enter element: "))
    nums.append(a)
print("Majority element is: ",majorityElement(nums))