def minimumBribes(q):
    bribe = 0
    for i in range(len(q)-1,-1,-1):
        if q[i] - (i + 1) > 2:
            print("Too chaotic")
            return
        for j in range(max(0, q[i] - 2), i):
            if q[j] > q[i]:
                bribe += 1
    print(bribe)

l = int(input("Enter length of list: "))
queue = []
for i in range(l):
    element = int(input("Enter an element in from 1 to 'length' (no repitions): "))
    queue.append(element)
minimumBribes(queue)