# *args
# def add(*nums):
#     sum = 0
#     for i in nums:
#         sum += i
#     return sum
# print(add(4,5,35,2))




# **kwargs
# def intro(**data):
#     print("\nData type of argument:", type(data))
#     for key, value in data.items():
#         print("{} is {}".format(key, value))
# intro(FirstName="Anas", LastName="Ahmad", age=21, phone=7620116383)
# intro(FirstName="Ammar", LastName="Ahmad", email="amrahmd123@gmail.com")




# def donobhi(*args,**kwargs):
#     sum = 0
#     for i in args:
#         sum = sum + i
#     print("Sum=",sum)
#     for key, value in kwargs.items():
#         print("{} is {}".format(key, value))
# donobhi(4,6,7,Name = "Anas Ahmad",Age = 21,Email = "ahmedanas8032@gmail.com")


