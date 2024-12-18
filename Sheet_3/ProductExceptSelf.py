def productExceptSelf(nums): 
    size = len(nums)
    products = [1]*size
    prod_f,prod_b = 1,1
    for i in range(size):
        products[i] *= prod_f
        products[size-1-i] *= prod_b
        prod_f = prod_f*nums[i]
        prod_b = prod_b*nums[size-1-i]
    return products
            

    '''
    import math
    final = []
    for i in range(len(nums)):
        final.append(math.prod(nums[:i])*math.prod(nums[i+1:]))
    return final
    '''

length = int(input("Enter length of list: "))
nums = []
for i in range(length):
    a = int(input("Enter element: "))
    nums.append(a)
print(productExceptSelf(nums))