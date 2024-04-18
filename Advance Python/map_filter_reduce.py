# map,filter,reduce
# map
# def square(num):
#     return num*num

# square = lambda num: num * num
# numbers = [3, 4, 6, 2, 1, 7, 3, 5]

# method1
# result = []
# for item in list:
#     result.append(square(item))
# print(result)

# method2
# result = map(square, numbers)
# print(list(result))

# filter
# numbers = [3, 24, 36, 2, 1, 7, 35, 5]
# def gt5(num):
#     if num>5:
#         return True

# gt10 = lambda num: num>10

# result = filter(gt5,numbers)
# result2 = filter(gt10,numbers)
# print(list(result))
# print(list(result2))

#reduce
# from functools import reduce

# numbers = [1,2,3,4]

# add = lambda a,b:a+b
# def mul(a,b):
#     return a*b

# result = reduce(add,numbers)
# result2 = reduce(mul,numbers)
# print(result)
# print(result2)