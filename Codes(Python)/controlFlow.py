# -------------lect7---------

# # comparison operators same as c++
# # logical operators
# # use the words or/and:
# print(True and False)
# print(True or False)
#
# #indentations
# # use ":" to start a new code block and indent the new code block:
# if 1>2:
#     print("one is greater than two")
# elif 'a'=='a':
#     print("the elif is different from else if ")
# else:
#     print("one is indeed less than two!!")


#loops

# # for loops
# seq=[1,2,3,4,5]
# for item in seq:
#     print(item,end="") #end="" is for preventing to print in newline everytime
#
#
# mypairs=[(1,2),(3,4)]
# for item in mypairs:
#     print(item)
#
# # tuple unpacking
# for i1,i2 in mypairs:
#     print(i1,i2)


# # while loops
# i=1
# while i<5:
#     print(i)
#     i=i+1
#
#
# #range function
# #if third paramter is missing it is taken as 1
# var=list(range(0,10,2)) # makes a list: [0,2,4,6,8]
# print(var)
#
# # list comprehension:
# newvar=[num**2 for num in var]
# print(newvar)


# functions
# use def keyword to define a funciton
def my_func(param1='default'):
    print("my first python function! {}".format(param1))
my_func("its nice")



# using docstring
def func_with_doc():
    """
    this is the doc string
    """
#to check the type of datatype in python: use type()
variable=True
print(type(variable))


# # filter
# myList=[1,2,3,4,5,6]
# def evens(num):
#     return num%2==0
#
# newList=list(filter(evens,myList))
# print(myList)
# print(newList)


# using lambda expression for above funciton
myList=[1,2,3,4,5,6]
newList=list(filter(lambda num: num%2==0,myList))
print(newList)
