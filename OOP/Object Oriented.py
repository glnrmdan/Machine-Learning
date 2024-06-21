class exam_results:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    
    def display(self):
        print(f"Name\t: {self.name}\nScore\t: {self.score}")
        
student1 = exam_results("John", 90)
student2 = exam_results("Jane", 85)

results = [student1, student2]

i = 1
for result in results:
    print("Student Number", i)
    result.display()
    i += 1
    print("\n")