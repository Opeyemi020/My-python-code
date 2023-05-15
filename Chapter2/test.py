course1 = int(input("Enter grade for course 1: "))
course2 = int(input("Enter grade for course 2: "))
course3 = int(input("Enter grade for course 3: "))

average = (course1 + course2 + course3) / 3

print("Average grade of three courses:", average)

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

age = int(input("Enter your age: "))
max_heart_rate = 220 - age
target_heart_rate_min = max_heart_rate * 0.5
target_heart_rate_max = max_heart_rate * 0.85

print(f"Your maximum heart rate is {max_heart_rate} beats per minute.")
print(f"Your target heart rate range is {target_heart_rate_min:.2f} to {target_heart_rate_max:.2f} beats per minute.")