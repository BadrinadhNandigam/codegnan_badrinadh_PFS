
'''
age = 21
assert age >= 18, "Age must be greater than 18"
print("Eligible")
'''

'''
Functions
-------------------
> a function is block of code which only execute when it is called
> you can pass data, known as paramenters into a fucntion
> to avoid repeated lines in code

def function_name():
 -----
 -----

function_name(Arguments)

'''

'''
num = 9
def even(num):
    if num%2==0:
        print("Even")
    else:
        print(f"{num}odd")
even(num)
even(109)

'''

'''
Ways to pass arguments
----------------------------
1. Required arguments

> A function must be called with the same no of arguments

def even(num,num_2,num_3):
    if num%2==0:
        print(f"{num}Even")
    else:
        print(f"{num}odd")
even(109,90)
even(num)
'''
'''
2. Default Arguments

> Default values is defined at parameters even though it will take from arugments
 -------------------------------------------------
def even(name = "Badri", age = 90, sal=26000):
    print(name)
    print(age)
    print(sal)
even("Nandigam", 34, 94332)

'''

'''
3. Keyword length arguments

> We can send arguments with keyvalue syntax. By this the order of arguments does not matter

def even(name,age,sal):
    print(name)
    print(age)
    print(sal)
even(name="Badri",age=24,sal=23456)

'''
'''
4. variable lenght arguments

> Adding a star(*) before the paramenter name in the function, recevie a tuple of arguments and can access items with indexes
'''

'''
name = 'badri'
def even(any):
    print(any)
even(name)
'''
'''
for i in range(2,100):
    for j in range(2,1):
        if i%j == 0:
            break
    else:
        print(i)
'''

'''
def prime(n):
    count = 0
    for i in range(1,n+1):
        if n%i == 0:
            count += 1
    if count == 2:
        print("Prime")
    else:
        print("Not prime")
num = int(input("Enter number: "))
prime(num)

'''

'''
def armstrong(num):
    power = len(str(num))
    tot = 0
    for i in str(num):
        tot += int(i)**power
    if num == tot:
        print("Armstrong")
    else:
        print("Not Armstrong")
n = int(input("Enter a number: "))
armstrong(n)

'''

'''
def palin(text):
    rev = ""
    for i in text:
        rev = i + rev
    if text == rev:
        print("Palindrome")
    else:
        print("Not palindrome")
text = input("Enter sreing: ")
palin(text)
'''

'''
def perfect(n):
    tot = 0
    for i in range(1,n):
        if n%i == 0:
            tot += i
    if n == tot:
        print("perfect")
    else:
        print("Not perfect")
num = int(input("Enter Number: "))
perfect(num)
'''

'''
def even_odd(n):
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")
num = int(input("Enter number: "))
even_odd(num)
'''

def factorial(n):

    fact = 1

    for i in range(1, n + 1):

        fact = fact * i

    print(fact)


num = int(input("Enter number: "))

factorial(num)
