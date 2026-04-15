#Inheritance Practica
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def display_info(self):
        return f"User: {self.name}, Email: {self.email}"
    
class Student(User):
    def __init__(self, name, email, balance, student_id):
        super().__init__(name, email)  # Call the parent class constructor
        self.student_id = student_id
        self.balance = balance
    
    def display_info(self):
        return f"Student: {self.name}, Email: {self.email}, Student ID: {self.student_id}, Balance: {self.balance}"
    
class Teacher(User):
    def __init__(self, name, email, subject):
        super().__init__(name, email)
        self.subject = subject
    
    def display_info(self):
        return f"Teacher: {self.name}, Email: {self.email}, Subject: {self.subject}"
    
class Administrator(User):
    def __init__(self, name, email, role):
        super().__init__(name, email)
        self.role = role
    
    def display_info(self):
        return f"Administrator: {self.name}, Email: {self.email}, Role: {self.role}"
    
student = Student("Cherki", "cherki@example.com", -200.00, "S74238914")
teacher = Teacher("Mr. Gurgenidze", "agurgenidze@example.com", "Mathematics")
administrator = Administrator("Ms. Boje", "boje@example.com", "Principal")

print(student.display_info())
print(teacher.display_info())
print(administrator.display_info())
