class Student:
    def __init__(self, name, branch):
        self.name = name
        self.branch = branch

    def show_details(self):
        print("Name:", self.name)
        print("Branch:", self.branch)

s1 = Student("Tejasri", "CSE")
s1.show_details()
