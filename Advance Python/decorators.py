# def decorator_func(func):
#     def wrapper_func():
#         print('inside wrapper_func')
#         return func()
#     print("inside decorator_func")
#     return wrapper_func

#method 1
# def show():
#     print("inside show")
# variab = decorator_func(show)
# variab()

# method 2
# @decorator_func
# def show():
#     print("inside show")
# show()

def dec_func(func):
    def squ(num):
        
        return func(num)
    
    return squ 

@dec_func
def fact(num):
    if num == 0 or num == 1:
        return 1
    result = fact(num-1)*num
    return result

print(fact(5))