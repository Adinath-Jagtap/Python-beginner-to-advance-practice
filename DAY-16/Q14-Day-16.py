#14. Create Student and Course classes where a student can enroll in multiple courses

class Course:
    def __init__(self, code, title):
        self.code = code
        self.title = title
        self.students = []

    def enroll(self, student):
        if student not in self.students:
            self.students.append(student)
            student.courses.append(self)

class Student:
    def __init__(self, sid, name):
        self.sid = sid
        self.name = name
        self.courses = []

    def enroll(self, course):
        course.enroll(self)

# Demo:
s1 = Student(1, "Alice")
s2 = Student(2, "Bob")
c1 = Course("CS101", "Intro CS")
c2 = Course("DS201", "Data Science Basics")

s1.enroll(c1)
s1.enroll(c2)
s2.enroll(c1)

print(s1.courses)  # [Course(CS101), Course(DS201)]
print(c1.students) # [Student(1, 'Alice'), Student(2, 'Bob')]