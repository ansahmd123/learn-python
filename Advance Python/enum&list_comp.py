#enumerate function

list = [34,14,'a',False,"anas",3.3]

# index = 0
# for item in list:
#     print(item,index)
#     index += 1

#shortcut for above task
for index,item in enumerate(list):
    print(item,index)


# list comprehension
# a = [4,37,17,786,3,21,2,64]

# b = []
# for item in a:
#     if item%2==0: 
#         b.append(item)
# print(b)

#shortcut using list comprehension
# b = [item for item in a if item%2==0]
# print(b)
