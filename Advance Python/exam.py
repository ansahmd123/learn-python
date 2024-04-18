# #1 question
# dict = {}
# dict[1] = 1
# dict['1'] = 2
# dict[1] += 1

# sum = 0
# for k in dict:
#     sum =sum + dict[k]
# print(sum)





# #2.
# counter = {}

# def addToCounter(country):
#     if country in counter:
#         counter[country] += 1
#     else:
#         counter[country] = 1
        
# addToCounter('China')
# addToCounter('Japan')
# addToCounter('china')
# print(len(counter))
# print(counter)



# # 3.
# class Acc:
#     def __init__(self, id):
#         self.id = id
#         id = 555
# acc = Acc(111)
# print(acc.id)

# # 4
# check1 = ['Learn', 'Quiz', 'Practice', 'Contribute']
# check2 = check1
# check3 = check1[:]
# check2[0] = 'Code'
# check3[1] = 'Mcq'
# print(check1)
# print(check2)
# print(check3)
# count = 0
# for c in (check1, check2, check3):
#     if c[0] == 'Code':
#         count += 1
#     if c[1] == 'Mcq':
#         count += 10
# print (count)

# # 5
# def addToList(listcontainer):
#     listcontainer += [10]
# mylistContainer = [10, 20, 30, 40]
# addToList(mylistContainer)
# print(len(mylistContainer))
# print(mylistContainer)

# # 6
# nameList = ['Harsh', 'Pratik', 'Bob', 'Dhruv']
# print(nameList[1][-1])

# # 7
# count = 1
# def doThis():
#     global count
#     for i in (1, 2, 3): 
#         count += 1
# doThis()
# print(count)

# 8
# a = True
# b = False
# c = False
# if not a or b:
#     print (1)
# elif not a or not b and c:
#     print (2)
# elif not a or b or not b and a:
#     print (3)
# else:
#     print (4)


# 9
# a = True
# b = False
# c = False
# if a or b and c:
#     print ("HELLO")
# else:
#     print ("hello")

# # 10
# r = lambda q: q * 2
# s = lambda q: q * 3
# x = 2
# x = r(x)
# x = s(x)
# x = r(x)
# print (x)

# # 11
# x = 1
# while True:
#     if x % 5 == 0:
#         break
#     print(x)
#     x += 1

# # 12
# print(all([2,4,6,0,5,6]))

# # 13
# print(pow(5,2,7))

# # 14
# print(round(4.576))

# # 15
# x y z p = 400,00
# print(xyzp)

# 16
# _x = 2
# print(_x)
# __x = 4
# print(__x)
# __xyz__ = 3
# print(__xyz__)

# 17
# class Name:
#     def __init__(javatpoint):
#         javajavatpoint = java
# name1=Name("ABC")
# name2=name1