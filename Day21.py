'''

Inheritance
--------------------
> This allows one class to aquire the properties and methods of another class

Types

1. Single Inheritance
> A class inherts from a single parent class

class father:
    def Land(self):
        print("my father hace 5A")
class Badri(father):
    def my_own(self):
        print(" I have 2A")
fam = badri()
fam.Land()

  Father
     |
     |
     |
     |
   child

2. Multiple Inheritance
---------------------------
> class father:
    def Land(self):
        print("my father has 5A")
  class mother:
      def gold(self):
          print("my mother have 1 kg G")
  class son(father,mother):
      def mine(self):
          print("i have ntg")
 all_ = son()
 all_.Land()
 all_.gold()
 
3. Multi level inheritance
--------------------------------
> A class ibherits from a parent class another class inherit from that child class
class grandfather:
    def land(self):
        print("my grandfather have 5A of land")
class father(grandfather):
    def flat(self):
        print("have flat at chennai")
class son(father):
    def ntg(self):
        print("I own both of their")
all_ = son()
all_.land()
all_.flat()
4. Hierarichal inheritance
5. Hybrid Inheritance
-----------------------------
> this is the combination of two or more types of inhertance

'''
'''
class animal:
    def eat(self):
        print("animal is eating")
class dog(animal):
    def bark(self):
        print("dog is barking")
d = dog()
d.eat()
d.bark()
'''

'''

class Camera:
    def take_photo(self):
        print("Photo captured")

class Phone:
    def call(self):
        print("Calling...")

class Smartphone(Camera, Phone):
    def browse(self):
        print("Browsing internet")

mobile = Smartphone()

mobile.take_photo()
mobile.call()
mobile.browse()
'''

'''
class Device:
    def power_on(self):
        print("Device powered on")

class Computer(Device):
    def process(self):
        print("Processing data")

class Laptop(Computer):
    def battery(self):
        print("Running on battery")

lap = Laptop()

lap.power_on()
lap.process()
lap.battery()
'''
'''
class father:
    def Land(self):
        print("10A")
class badri(father):
    def mine(self):
        print("job")
class radha (father):
    def sis(self):
        print("jobless")
radh = radha()
radh.Land()
r = badri()
r = land()
'''

'''
class A:
    def some(self):
        print("class A')
class B(A):
    def any(self):
        print("class B")
class C(A):
    def so (self):
        print("Class C")
class D(B,c):
    def all_(self):
        print("class D")
how = D()
how.so()
'''

'''
super() method
--------------------
> used to access methods and constructor of the parent class from the child class

'''

'''
class parent:
    def display(self):
        print('method')
class child(parent):
    def display(self):
        super().display()
        print('Method child')
any_ = child()
any_.display()
'''

class person:
    def __init__(self,name):
        self.name = name
class stu_(person):
    def __init__(self,roll):
        super().__init__(name)
        self.roll = roll
    def show(self):
        print(f"Name : (self.name)")
        print(f"Roll no : (self.roll)")
any_ = stu_('badri',101)
any_.show()
