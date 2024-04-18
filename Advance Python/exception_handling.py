# while(True):
#     print("Enter q to quit:")
#     a = input("Enter a number:")
#     if a == 'q':
#         break
#     try:
#         a = int(a)
#         if a>6:
#             print("You entered a number greater than 6")
#         else:
#             print("You entered a number less than 6")
#     except Exception as e:
#         print(e)
# print("Thanks for playing")



# num1 = int(input("Enter a number:"))
# num2 = int(input("Enter a number:"))

# try:
#     result = num1/num2
#     print(f"result =",result)
# except Exception as e:
#     print(f"Error occured:",e)




# different types of exception

# try:
#     a = int(input("Enter a number:"))
#     c = 1/a
#     print(c)
# except ValueError as e:
#     print("Please enter a valid  value")
    
# except ZeroDivisionError as e:
#     print("Make sure you didn't enter zero")

# except Exception as e:
#     print("Another unknown exception")

# print("Thanks for using this code!")

# try except with else
# try:
#     i = int(input("Enter a number:"))
#     c = 1/i
# except Exception as e:
#     print(e)
# else:
#     print("Successfull")


#raise own exception

# def increment(num):
#     try:
#         return int(num)+1
#     except:
#         raise ValueError("The input is invalid")
    
# a = increment("anas")
# print(a)

