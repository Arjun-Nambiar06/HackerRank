def threeSum(nums):
    zero,N,P = [],[],[]
    final = []

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
                if [(-1)*i,0,i] not in final:
                    final.append([(-1)*i,0,i])
        
    for i in range(len(N)):
        for j in range(i+1,len(N)):
            target = (-1)*(N[i]+N[j])
            if target in pos and sorted([N[i],N[j],target]) not in final:
                final.append(sorted([N[i],N[j],target]))

    for i in range(len(P)):
        for j in range(i+1,len(P)):
            target = (-1)*(P[i]+P[j])
            if target in neg and sorted([P[i],P[j],target]) not in final:
                final.append(sorted([P[i],P[j],target]))

        
    if len(zero) >= 3 and [0,0,0] not in final:
        final.append([0,0,0])
            
    return final

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