import random

# List of random names
names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hannah", "Ian", "Jasmine"]

# List of subjects
subjects = ["Math", "Science", "History", "English", "Art"]

# Generate random grades for each student for each subject
students = [{
    "name": name,
    "grades": {subject: random.randint(60, 100) for subject in subjects}
} for name in names]

# Print the list of students and their grades
for student in students:
    print(f"Name: {student['name']}")
    print(f"Grades: {student['grades']}")
    print()  # Empty line for separation
