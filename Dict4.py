# A dictionary is given where the keys are student names and values are student grades we create a function 
# that returns a dictionary with names as keys and average grades as their values
students={
    "Alice":[75,82,90],
    "Bob":[83,88,92],
    "Charlie":[76,84,89]
}

def average_grades(students: dict) -> dict:
    avg={}
    for students,grades in students.items():
        avg[students]=sum(grades)/len(grades)
    return avg

print(average_grades(students))    

