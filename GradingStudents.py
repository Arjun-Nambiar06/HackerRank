def gradingStudents(grades):
    for i in range(len(grades)):
        if grades[i]>=38:
            if (grades[i]+1)%5==0:
                grades[i]+=1 
            elif (grades[i]+2)%5==0:
                grades[i]+=2
    return grades

grades_count = int(input("Enter the number of grades: "))
grades=[]
for i in range(grades_count):
    grade = int(input("Enter a grade: "))
    grades.append(grade)

print("\nFinal Grades are: ")
rounded_grades=gradingStudents(grades)
for i in range(grades_count):
    print(rounded_grades[i])