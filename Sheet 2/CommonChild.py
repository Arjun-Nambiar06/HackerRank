def commonChild(s1, s2):
    m = n = len(s1)
    prev = [0]*(m+1)
    crnt = [0]*(m+1)
    
    for i in range(m):
        for j in range(n):
            if s1[i]==s2[j]:
                crnt[j+1] = prev[j]+1
            else:
                crnt[j+1] = max(crnt[j],prev[j+1])
        prev,crnt = crnt,prev
    return prev[m]
    
    
s1 = (input("Enter first string: ")).upper()
s2 = (input("Enter second string: ")).upper()
print("Length of common child is ",commonChild(s1,s2),'.')
 