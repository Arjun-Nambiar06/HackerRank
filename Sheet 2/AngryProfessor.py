def angryProfessor(k, a):
    on_time = 0
    for i in a:
        if i<=0:
            on_time += 1
    if on_time < k:
        return "YES"
    else:
        return "NO"

total = int(input("Enter total number of students: "))
threshold = int(input("Enter minimum number of students rquired for class to not be cancelled: "))
arrival_time=[]
for i in range(total):
    time = int(input("Enter arrival time of student: "))
    arrival_time.append(time)

print("Is the class cancelled? ", angryProfessor(threshold,arrival_time))