'''
Built in function

----------------------------
input()
len()
type()
max()
min()

'''

'''
> Recursive Functions in Python

A recursive function is a function that calls itself again and again until a condition becomes false.


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)
print(factorial(5))


'''
 def palindrome(text):
     rev= ""
     for i in text:
         rev = i + rev
    if text == rev:
        print("palin")
    else:
        print("no")
text = input("Enter strig: ")
palindrome(text)
'''
'''

def perfect(n):
    tot = 0
    for i in range(1,n):
        if n%i ==0
        tot += i
    if n== tot:
        print("Perfect")
    else:
        print("Not perfect")
num = int(input("enter number: "))
perfect(num)

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
return
---------------------
this ends the function execution and sends a value back to the code that called the function

eg
-------
def add(a,b):
    return a + b
res = add(4,5)
print(res)
'''

'''
Lambda function
----------------------
> is small anonmous function
> can take n number of arguments, but only one expression
'''

add = lambda a, b : a + b
print(add(10, 20))

square = lambda n : n * n
print(square(5))

sub = lambda a,b : a - b
print(sub(5,2))

             
