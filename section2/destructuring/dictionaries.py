# destructuring: cut the collection to variables
# "="

student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}

# student is the key
# attendance is the value

for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}")


person = ("Bob", 42, "Mechanic")
name, _, profession = person
print(name, profession)


*head, tail = [1, 2, 3, 4, 5]
print(head)  # [1,2,3,4]
print(tail)


head, *tail = [1, 2, 3, 4, 5]
print(*head)  # 1 2 3 4
print(tail)
