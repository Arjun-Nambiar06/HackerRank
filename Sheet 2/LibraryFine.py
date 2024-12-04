def libraryFine(d1, m1, y1, d2, m2, y2):
    if y1 == y2:
        if m1 <= m2: 
            if d1 <= d2 or m1 < m2:
                return 0
            else: #m1=m2, y1=y2, d1> d2
                return 15 * (d1-d2)
        else: #m1>m2
            return 500 * (m1-m2)
    elif y1 < y2:
        return 0
    else:
        return 10000 

d1 = int(input("Enter return date: "))
m1 = int(input("Enter return month: "))
y1 = int(input("Enter return year: "))

d2 = int(input("\nEnter due date: "))
m2 = int(input("Enter due month: "))
y2 = int(input("Enter due year: "))

print("\nThe fine applicable is: ",libraryFine(d1,m1,y1,d2,m2,y2))