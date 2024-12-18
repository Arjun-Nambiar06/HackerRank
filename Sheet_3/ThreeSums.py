def threeSum(nums):
    zero,N,P = [],[],[]
    final = set()

    for i in nums:
        if i < 0:
            N.append(i)
        elif i > 0:
            P.append(i)
        else:
            zero.append(i)
        
    neg,pos = set(N),set(P)
    if zero:
        for i in pos:
            if (-1)*i in neg:
                final.add(tuple([(-1)*i,0,i]))
        
    for i in range(len(N)):
        for j in range(i+1,len(N)):
            target = (-1)*(N[i]+N[j])
            if target in pos:
                final.add(tuple(sorted([N[i],N[j],target])))

    for i in range(len(P)):
        for j in range(i+1,len(P)):
            target = (-1)*(P[i]+P[j])
            if target in neg:
                final.add(tuple(sorted([P[i],P[j],target])))

        
    if len(zero) >= 3:
        final.add(tuple([0,0,0]))
            
    return [list(x) for x in final]

    '''length = len(nums)
    output=[]
    for i in range(length):
        for j in range(i+1,length):
            for k in range(j+1,length):
                if nums[i]+nums[j]+nums[k] == 0 :
                    trio = sorted([nums[i],nums[j],nums[k]])
                    if trio not in output:
                        output.append(trio) 
    return output'''
length = int(input("Enter length of list: "))
nums = []
for i in range(length):
    a = int(input("Enter element: "))
    nums.append(a)
print(threeSum(nums))