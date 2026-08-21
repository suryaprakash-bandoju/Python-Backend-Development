class Student:
    def __init__(self, name, age, gpa = 0.0, branch="Computer Science"):
        if not name or not isinstance(name, str):
            raise ValueError("Student name must be a non-empty string")
        if age < 16 or age > 100:
            raise ValueError("Student age must be between 16 to 100")

        self.name = name
        self.age = age
        self.branch = branch
        self.gpa = gpa
        self.courses = []

    def enroll(self, course):
        # Add course to self.courses if not already enrolled
        if course not in self.courses:
            self.courses.append(course)
        else:
            raise ValueError(f"Already enrolled in {course}")

    def get_gpa(self):
        # Return current GPA
        return self.gpa

    def update_gpa(self, new_gpa):
        # Validate: new_gpa must be between 0.0 and 10.0
        if new_gpa >= 0.0 and new_gpa <= 10.0:
            self.gpa = new_gpa
        else:
            raise ValueError("GPA must be between 0.0 to 10.0")

    def get_info(self):
        # Return formatted string with name, age, branch, gpa, courses
        return (f"Name: {self.name}, Age: {self.age}, Branch: {self.branch}, GPA: {self.gpa}, Courses: {self.courses}")


s1 = Student("Surya", 21)
s1.enroll("Python")
s1.enroll("Data Structures")
s1.update_gpa(8.5)
print(s1.get_info())
# Expected: Name: Surya, Age: 21, Branch: Computer Science, GPA: 8.5, Courses: ['Python', 'Data Structures']

# These should raise errors:
s2 = Student("", 21)  # Empty name
s3 = Student("Priya", 15)  # Age too young
s4 = Student("Rahul", 20)
s1.update_gpa(11.0)  # Invalid GPA
