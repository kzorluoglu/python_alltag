students = [
    ("Max", 1),
    ("Necmettin", 5),
    ("Temel", 4),
    ("Erik", 1)
]

def students_key(student):
    return student[1]

# standart way
students.sort(key=students_key, reverse=True)
print(students)

# with lambda

students.sort(key=lambda student: student[1])
print(students)

f = lambda student: student[1]
f(("Max", 1))