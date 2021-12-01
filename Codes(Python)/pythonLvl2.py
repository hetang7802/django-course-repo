# scope: order:local->enclosing funciton locals->global->built-in

# OOP in python
# class Sample():
#     pass
# x=Sample()
# print(type(x))

# attributes in a class
# class Dog():
#     def __init__(self,breed):
#         self.breed=breed
#
# mydog=Dog(breed="some breed")
# print(mydog.breed)

# methods in a class
class Circle():
    pi=3.14
    def __init__(self,radius=1):
        self.radius=radius

    def find_area(self):
        return Circle.pi*self.radius*self.radius

newCircle=Circle(10)
print(newCircle.find_area())

# inheritance

# class Animal():
#
# 	def __init__(self):
# 		print("Animal Initial Method")
#
# 	def who_am_i(self):
# 		print("Animal")
#
# 	def eat(self):
# 		print("Eating")
#
# # Create a Dog class
# # here we inherit the class Animal in the class Dog
# class Dog(Animal):
#
# 	def __init__(self):
# 		# Animal.__init__(self)
# 		print("Dog Initial Method")
#
# 	def bark(self):
# 		print("WOOF")
#
# mydog = Dog()
# mydog.who_am_i()
# mydog.eat()
# mydog.bark()

# # special methods
# class Book():
#
# 	def __init__(self, title, author, pages):
# 		self.title = title
# 		self.author = author
# 		self.pages = pages
#   #print() will search for this method in the class
# 	def __str__(self):
# 		return "Title: {}, Author: {}, Pages: {}".format(self.title, self.author, self.pages)
#   #len funciton when called uses this part of the class
# 	def __len__(self):
# 		return self.pages
#   # __del__ will be called when instace of a class is deleted
# 	def __del__(self):
# 		print("A book was deleted")
#
# b = Book("Python", "Vadym", 250)
# print(b)
# print(len(b))
# del b
