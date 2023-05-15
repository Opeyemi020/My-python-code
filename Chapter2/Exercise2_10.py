course1 = int(input("Enter grade for course1:\n"))
course2 = int(input("Enter grade for course2:\n"))
course3 = int(input("Enter grade for course3:\n"))

average = (course1 + course2 + course3) / 3
print("Average grade for three courses is", average)

if course1 > course2:
    if course1 > course3:
        print("Course with highest grade: Course 1")
    else:
        print("Course with highest grade: Course 3")
else:
    if course2 > course3:
        print("Course with highest grade: Course 2")
    else:
        print("Course with highest grade: Course 3")

if course1 < course2:
    if course1 < course3:
        print("Course with lowest grade: Course 1")
    else:
        print("Course with lowest grade: Course 3")
else:
    if course2 < course3:
        print("Course with lowest grade: Course 2")
    else:
        print("Course with lowest grade: Course 3")
