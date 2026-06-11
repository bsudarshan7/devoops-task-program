students = {
    "Rahul": 85,
    "Priya": 92,
    "Amit": 76,
    "Sneha": 89,
    "Karan": 95
}

highest_student = max(students, key=students.get)
lowest_student = min(students, key=students.get)

average_marks = sum(students.values()) / len(students)

print("===== Student Marks Report =====")
print()

for name, marks in students.items():
    print(f"{name}: {marks}")

print()
print(f"Top Scorer: {highest_student} ({students[highest_student]})")
print(f"Lowest Scorer: {lowest_student} ({students[lowest_student]})")
print(f"Average Marks: {average_marks:.2f}")
