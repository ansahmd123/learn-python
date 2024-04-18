
# class Students:
#     def set_details(self):
#         self.name = input("Enter your name:")
#         self.age = input("Enter your age:")
#         self.branch = input("Enter your engineering branch:")

#     def get_details(self):
#         print(f"Your name is {self.name}, you are {self.age} years old, and your engineering branch is {self.branch}")


# stud1 = Students()

# stud1.set_details()
# stud1.get_details()

#getters/setters decorators
class Employee:
    def __init__(self,firstName,lastName):
        self.firstName = firstName
        self.lastName = lastName

    def email(self):
        pass
    
    def details(self):
        print(f"The name of the employee is {self.firstName} {self.lastName}")

anas = Employee("Anas","Ahmad")
musaib = Employee("Musaib","Qureshi")

anas.details()
musaib.details()