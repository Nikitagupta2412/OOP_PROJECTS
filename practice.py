#hiding the unnecessary codes = Abstraction
#having two functions with same name but different implementations = Polymorphism
#combining data and methods that operate on that data = Encapsulation
#when functions with diff implementation have same name the lat one overrides the another = Overriding
#nheritance is when a class inherits the properties and methods of another class = Inheritance

# from abc import ABC, abstractmethod

# class enforce(ABC):
#     @abstractmethod
#     def enginestart(self):
#         print("Bike engine started")

# class bike(enforce):
#     def enginestart(self):
#         print("Bike engine started")

# obj=bike()
# obj.enginestart()
# class numbers:
#     def __init__ (self,a):
#         self.a=a
#     def __add__(self,other):
#         return self.a + other.a

# num1=numbers(5)
# num2=numbers(10)
# result=num1+num2
# print(result)
# def extragreeting(func):
#     def wrapper():
#         print("Helloooo bitchhh")
#         func()
#         print("Yyyayy cllooockkkk iittt bitchhh")
#     return wrapper


# @extragreeting
# def greeting():
#     print("Youuuuuuuuuuuuuuuuuuuuuuuu are the best")

# greeting()
# def addition(*args):
#     sum=0
#     for i in args:
#         sum+=i
#     return sum

# print(addition(1,2,3,4,5,6,7,8,9,10))
# def info(**kwargs):
#     return kwargs

# print(info(name="nikita",age="22",city="delhi",country="india"))

# m=[1,2,3,4,5]
# passed_list=list(filter(lambda x:x**2,m))
# print(passed_list)

# name=["nikita","nikhil","nisha","nidhi","nishant"]
# marks=[90,80,70,60,92]
# result= zip(name,marks)

# print(list(result))
