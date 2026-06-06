'''
Polymorpshism

--------------------

> This means 'many forms' it allows the same function, method, or operator to behave differently depending on object

1. Method Overloading
----------------------

> Method overloading means defining multiple methods with same name but different parameters

class calc:
    def add(self,a,b,v=0):
        return a + b+ v
    def add(self,a,b,v=0):
        return a+b+v
An = calc()
print(An.add(23,6))
print(An.add(23,6,34))

class calc:
    def add(self,a,b):
        return a + b
    def add(self,a,b,c):
        return a + b+ c
an = calc()
print(an.add(23,6))
print(an.add(23,4,34))

2. Method Overrinding
-------------------------
> This occurs when a child class provides its own implementstion of a method already defined in the parent class


class animal:
    def sound(self):
        print("Animal makes sound")
class dog(animal):
    def sound(self):
        super().sound()
        print("Dog barks")
ntg = dog()
ntg.sound()

3. Operator Overloading
---------------------------

> This allows operators such as +,-,*, etc, to perform different actions for user defined objects
> Note : operator inside the method will overload a special method or operator given in the call

class stu:
    def __init__(self,marks):
        self.marks = marks
    def __add__(self,b):
        return self.marks + other.marks
so_l = stu(4)
so = stu_(78)
print(so_l + so)


class Area:
    def find_area(self, length, breadth=0):
        if breadth == 0:
            return length * length
        else:
            return length * breadth
obj = Area()
print("Area of Square:", obj.find_area(5))
print("Area of Rectangle:", obj.find_area(5, 10))


class Stu:
    def __init__(self, marks):
        self.marks = marks

    def __add__(self, other):
        return self.marks + other.marks

    def __sub__(self, other):
        return self.marks - other.marks

    def __mul__(self, other):
        return self.marks * other.marks
s1 = Stu(80)
s2 = Stu(20)
print("Addition:", s1 + s2)
print("Subtraction:", s1 - s2)
print("Multiplication:", s1 * s2)

4. Abstraction
-------------------
This is the process of hiding internal implementation details and showing only essential features to the user
> It focuses on what an object does rather than how it does it
'''

from abc import ABC, abstractmethod
class Vechicle(ABC):

    @abstractmethod
    def area(self):
        pass
    def perimenter(self):
        pass
class rec(shape):
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def area(self):
        return self.a * self.b
    def perimenter(self):
        return 2*(self.a * self.b)
an = rec(10,5)
print(an.area())
    
