'''

List Comprehension
----------------------------------

> List Comprehension a shoetest syntax when we want to create a new list from existing list

'''

'''
old = [23,46,7,2]
new_ = ["even" if so % 2==0 else so for so in old]
print(new_)

'''

'''
Generators
--------------------
> Generators in python are a special type of iterables, allowing users to iterate over data efficicently without storing everything in memory
> they generate values lazily usinf yield keyword
> Generators does not store entire dataset in memory, they generate values on the fly
> Avoiding unnecessary storage of data speed up execution.

How it works
----------------------------------
>It looks like normal function but uses the yiel keyword instead of return
> When Function is called it does not execute immediately. Instead, it return a generator
object which can be iterated usind loop or next() function

def sample_gen():
    print("start")
    yield 1
    yield 2
    yield 3
    print("end")
gen = simple_gen()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

'''
'''
def any(num):
    for i in range(num):
        yield i*i
a = any(4)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
'''
'''
def any(num):
    return num * num
n = int(input("Enter a number: "))
print(any(n))
'''

'''
def sqr(num):
    res = []
    for i in range(1,num+1):
        res.append(i*i)
    return res
print(sqr(5))


def any(num):
    for i in range(1,num+1):
        yield i*i
a = any(5)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
'''
'''
def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        yield a
        c = a + b
        a = b
        b = c
f = fibonacci(5)
print(next(f))
print(next(f))
print(next(f))
'''

para = 'abfdsfv opfipovmpdf'
vow = ''
for j in para:
    if j not in "AEIOUaeiou":
        vow += j
print(vow)
