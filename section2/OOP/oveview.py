""" student = {
    "name": "Rolf",
    "grades": (89, 90, 93, 78, 90)
}

def average(sequence):
    return sum(sequence) / len(sequence)

#passing data to function
print(average(student["grades"])) """

# dot(.) means inside e.g Student.average() means average function inside Student class
class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average(self):
        return sum(sequence) / len(sequence)
    def __str__(self):
        return f"Student {self.name}, {self.grades} years old."
    def __repr__(self):
        return f"Student"




# easier to pass json
studenta = Student("Bob", (89, 90, 93, 78, 90))
print(studenta.name)

# access directly in student object
print(studenta)











