# Parent Class Exam Result
class StudentName:
    def __init__ (self, name):
        self.name = name
        

# Child Class Exam Result
class Result(StudentName):
    def __init__ (self, name, score, grade):
        super().__init__(name)
        self.score = score
        self.grade = grade
        
    def display(self):
        print(f"Name\t: ", self.name, "\nScore\t: ", self.score, "\nGrade\t: ", self.grade, "\n")
        
def grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

student1 = Result("Hari", 90, grade(90))
student2 = Result("Budi", 85, grade(85))
student3 = Result("Joko", 70, grade(70))
student4 = Result("Rudi", 55, grade(55))

results = [student1, student2, student3, student4]
i = 1

for result in results:
    print("Student Number ", i)
    result.display()
    i += 1