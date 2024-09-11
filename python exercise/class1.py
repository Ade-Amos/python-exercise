class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)
        return f"Added grade {grade}. Current grades: {self.grades}"

    def average_grade(self):
        if not self.grades:
            return "No grades available."
        return f"Average grade: {sum(self.grades) / len(self.grades):.2f}"

# Create an instance and run the methods
student1 = Student("Charlie", "S12345")
print(student1.add_grade(90))
print(student1.add_grade(85))
print(student1.average_grade())