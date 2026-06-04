'''
Object Oriented Programming Systems (OOPS)

1. Class : A class is blueprint or a template used to create object

2. Object : It is an instance of a class

class stu:
    name = 'badri'
s1 = stu()
print(s1.name)

3. Attribute : Attributes are the variables that belongs to a class or an object
4. Methods : The functions defined inside the class is methods
5. Constructor : A constructor is a special type of method that is automatically callled when an object is created from a class.

class student:
    name = 'badri'
    age = 22
s1 = student()
print(s1.name)
print(s1.age)


class PFS_DA:
    def python(self):
        PFS_DA = 'Batch_003'
        print('This is PFS & DA Batch - 003')
    def Flask(self):
        PFS = 'Batch_003'
        print('This is PFS Batch - 003')
all_ = PFS_DA()
all_.python()
all_.Flask()


'''

'''
class ATM:
    def __init__(self, balance, name):
        self.balance = balance
        self.name = name
    def bal_check(self):
        print(f"{self.name}, your total balance is {self.balance + 700}")
    def show_name(self):
        print(self.name)

card = ATM(balance=5000, name='badri')
card.bal_check()
card.show_name()

'''

'''
6. Access Modifiers

> public : This can be accessed from anywhere in the program
> Protected : This is represented using a single underscore _
> private : This is represented using double underscore __

'''

'''

7. Encapsulation  : wrapping up methods and data into single unit is called encapsulation

'''

class bank:
    def 
