def compareTriplets(a, b):
    Alice=Bob=0
    for i in range(3):
        if a[i]>b[i]:
            Alice+=1
        elif a[i]<b[i]:
            Bob+=1
    return [Alice,Bob]

A_score=[]
B_score=[]
Cat=["problem clarity","originality","difficulty"]
for i in range(3):
    a=int(input("Enter Alice's score for "+Cat[i]+": "))
    b=int(input("Enter Bob's score for "+Cat[i]+": "))
    A_score.append(a)
    B_score.append(b)

Comp_Score=compareTriplets(A_score,B_score)
print("Alice's comparison score: ", Comp_Score[0], "\nBob's comparison score: ", Comp_Score[1])