'''
nested loops

> loop inside loop
'''
'''
for i in range(1,10):
    for j in range(1,2):
        print(i)
        print(j)
        '''
'''
num =int(input("enter number: "))
for i in range (1,13):
    print(num, "x", i, "=", num * i)
'''

'''
text = input("Enter string: ")

rev = ""

for i in text:
    rev = i + rev

print(rev)
'''

'''
text = input("Enter string: ")

rev = ""

for i in text:
    rev = i + rev
if text == rev:
    print("palindrome")
else:
    print("Not palindrome")
'''

'''
num = int(input("Enter a number: "))
power = len(str(num))
sum = 0
for i in str(num):
    sum += int(i)**power
if num == sum:
    print("Armstrong Number")
else:
    print("Not a Armstrong Number")
'''

'''

n = int(input("enter number: "))
sum = 0
for i in range(1,n):
    if n % i == 0:
        sum += i
if n == sum:
    print("perfect")
else:
    print("not perfect")
'''

'''
num = int(input())
count = 0
for i in range(1,num+1):
    if num % i == 0:
        count += 1
if count == 2:
    print("Prime Number")
else:
    print("Not prime")

'''

'''
for i in range(1,6):
    for j in range(i):
        print(chr(65 + j),end = " ")
    print()
'''

'''
num = 1
for i in range(1,6):
    for j in range(i):
        print(num, end = " ")
        num += 1
    print()
'''

'''
for i in range(1,6):
    for j in range(i):
        print("*", end = " ")
    print()
'''

'''
rows = 5
for i in range(rows,0,-1):
    print("*" * i)

'''

rows = 5
for i in range(rows):
    for j in range(rows - i - 1):
        print(" ", end=" ")
    for k in range(2 * i + 1):
        print("*", end=" ")
    print()














