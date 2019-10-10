# Directories

friend_ages = {"Ralf": 24, "Adam": 20, "Anne": 30}
friend_ages["Ralf"] = 20

print(friend_ages)

# List of dictionaries

friends = [
    {"name": "Rolf Smith", "age": 24},
    {"name": "Adam Wool", "age": 30},
    {"name": "Anne Pun", "age": 27},
]

print(friends)

# -- Iteration --

student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}

for student in student_attendance:
    print(f"{student}: {student_attendance[student]}")

# Better

for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}")

# -- Using the `in` keyword --

if "Tona" in student_attendance:
    print(f"Tona: {student_attendance[student]}")
else:
    print("Tona isn't a student in this class!")

# -- Calculate an average with `.values()` --

attendace_values = student_attendance.values()
print(sum(attendace_values) / len(attendace_values))