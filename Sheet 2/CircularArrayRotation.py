def circularArrayRotation(a, k, queries):
    k %= len(a)
    q = []
    for i in queries:
        q.append(a[i-k])
    return q

size = int(input("Enter size of list: "))
a = []
for i in range(size):
    element = int(input("Enter a value: "))
    a.append(element)

k = int(input("\nEnter the number of rotations on the list: "))

n = int(input("\nEnter the number of queries: "))
queries = []
for i in range(n):
    query = int(input("Enter the index to be checked: "))
    queries.append(query)

print()
q = circularArrayRotation(a,k,queries)
for i in range(n):
    print("The value at index ",queries[i]," is ",q[i],".")