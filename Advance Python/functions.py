# class computer:
#     def __init__(self,cpu,ram):         #constructor:call automatically for every object
#         self.cpu = cpu
#         self.ram = ram

#     def config(self):
#         print("Config is",self.cpu+" with "+str(self.ram)+"gb ram")

#     def total_ram(self,gpu_mem=0):
#         print("Total ram = ", int(self.ram)+int(gpu_mem),"gb")

# # create or instantiate an object
# comp1 = computer("Intel i5",8)
# comp2 = computer("Ryzen 7",16)

# # computer.config(comp1)
# # computer.config(comp2)

# # calls methods of the object
# comp1.config()
# comp1.total_ram(2)

# comp2.config()
# comp2.total_ram()


class Students:

    #school and total_marks are class variable
    school = "Shri Shivaji College of Arts,Commerce and Scinence, Akola"
    total_marks = 300

    #physics,chemistry,biology,mathematics are instance or object variable and will only be accessible using object names.
    def __init__(self,physics,chemistry,biology,mathematics):
        self.physics = physics
        self.chemistry = chemistry
        self.biology = biology
        self.mathematics = mathematics

    def pcm_percentage(self):
        return (((self.physics+self.chemistry+self.mathematics)/self.total_marks)*100)

    def pcb_percentage(self):
        return (((self.physics+self.chemistry+self.biology)/self.total_marks)*100)

    #classmethod is a decorator used for accessing class function.
    @classmethod
    def get_school(cls):
        return cls.school

    @staticmethod
    def info():
        print("This is student class...and this method is static method and has nothing to do with instance or class variable")

    @staticmethod
    def message():
        print("Hi Students")


anas = Students(56,74,38,76)
musaib = Students(87,58,98,65)

# instance method calls
# print(anas.pcb_percentage())
# print(anas.pcm_percentage())
# print(anas.school)
#
# print(musaib.pcb_percentage())
# print(musaib.pcm_percentage())
# print(musaib.school)

# # class method calls
print(Students.get_school())
print(anas.get_school())

# static method calls
Students.info()
anas.info()

anas.message()
Students.message()


# class inside class


# class Students:
#     def __init__(self, name, age, batch) -> None:
#         self.name = name
#         self.age = age
#         self.batch = batch

#     def show(self):
#         print(self.name, self.age, self.batch)

#     class Laptop:
#         def __init__(self, name, cpu, ram):
#             self.name = name
#             self.cpu = cpu
#             self.ram = ram

#         def show(self):
#             print(self.name, self.cpu, self.ram)


# anas = Students("Anas", 21, "Computer")
# adnan = Students("Adnan", 24, "Electrical")

# # anas.show()
# # adnan.show()

# lap1 = Students.Laptop("HP", "i5", 8)
# lap1.show()
# lap2 = Students.Laptop("Dell", "i7", 16)
# lap2.show()

# inheritance


# class A:
#     def __init__(self):
#         print("in A init")
#
#     def method1(self):
#         print("In method 1")
#
#     def method2(self):
#         print("In method 2")
#
#
# class B:
#     def __init__(self):
#         print("In B init")
#
#     def method3(self):
#         print("In method 3")
#
#     def method4(self):
#         print("In method 4")
#
#
# class C(A, B):
#     def __init__(self):
#         print("In C init")
#
#     def method5(self):
#         print("In method 5")


# a = A()
# a.method1()
# a.method2()

# b = B()
# b.method3()
# b.method4()

# a = A()
# b = B()
# c = C()