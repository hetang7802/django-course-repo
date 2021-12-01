# print("python's cool")
# var=19
# var1="string "
# var2=var1*var
# print(var2)

# # -----------lect 3(strings)------------
# #strings
# #use single/double quotes
# #indexing same as js (use negative to refer from the end of string )
# # slicing(similar to substring)
# # exmaple:
# mystring="abcdefg"
# print(mystring[1:4]) #prints from index 1 upto index 4 (excluding 4)
# print(mystring[1::2]) #prints every alternate character starting from index one
# mystring[::-1] can be used to reverse the string
# #strnig is immutable(any particular character cannot be changed)
# x=mystring.upper()#converts all letters to upper case
# print(x)
# y=mystring.capitalize()#converts first letter to capital
# print(y)
# x=mystring.split('c')#will split the string from all the places where there is c in the string
# print(x)
# #string interpolation
# x="Insert string here {} another here {k2} third one here {k1}".format("dog",k1="cat",k2="rabbit")
# print(x)
# use funciton endswith to find if a string ends with other string:
# example:
# print( "abcdefg".endswith("defg"))# will return True


# # -------------lect 4----------(lists)
# # lists in python (similar to js array), can hold mixed datatypes
# # how to create:
# myList=[1,2,3]
# print(myList)
# #to find the length
# length=len(myList)
# print(length)
# #indexing and splicing is similar to strings
# #lists are mutable unlike string
# #append can be used like push in c++
# #extend can be used to append multiple items:
# myList.extend([1,2])
# print(myList)

# #pop method will pop the index given to it as paramter without paramter,the last
# # index will be removed, the return value will be the element popped
# myList.pop(3)
# print(myList)
# #reverse method will reverse the list
# #.sort can be used to sort the list (refer heirarchy for mixed data types)
# # nested lists can be used
# matrix=[[1,2,3],[4,5,6],[7,8,9]]
# #list comprehension
# first_col=[row[0] for row in matrix]
# print(first_col)


# # ------------lect 5(dictionaries)------------
# # similar to unordered map in c++ but the data types can be varied for values
# # remember that it is unordered
# my_stuff={"key1":"string1","key2":123,"key3":[1,2,4]}
# print(my_stuff)
# #to grab any of the values
# print(my_stuff["key1"])
# #to modify particular value
# my_stuff["key1"]="new"
# #to add key-value pair
# my_stuff["new_key"]=12
# print(my_stuff)


# --------------lect6(tuples,sets,booleans)------

# # booleans: True,False, can also use 0,1(less common)
#
# # tuples: immutable sequences, can have mixed data types
# # for declaration use paranthesis instead of sq brackets in lists
# # slicing,indexing etc can be done same as lists
# t=(1,"hello",3)
# print(t[1])
#
# # sets
# x=set()
# # use add like push
# # sets do not have particular order
# x.add(1)
# x.add("hello")
# print(x)
# # sets can have only unique elements
# # new_set = set([1,1,1,2,3]) will give new_set={1,2,3}
