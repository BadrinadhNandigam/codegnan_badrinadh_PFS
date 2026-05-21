'''

marks = int(input("Enter marks: "))
if marks >= 90 and marks <= 100:
    print("Grade A")
elif marks >= 75 and marks < 90:
    print("Grade B")
elif marks >= 60 and marks < 75:
    print("Grade C")
elif marks >= 35 and marks < 60:
    print("Grade D")
elif marks >= 0 and marks < 35:
    print("Fail")
else:
    print("Invalid marks")

'''

'''
a = int(input("Enter the number 1: "))
b = int(input("Enter the number 2: "))
c = int(input("Enter the number 3: "))

if a>b and a>c:
    print("max number is: ", a)
elif b>a and b>c:
    print("max number is: ", b)
else:
    print("max number is: ", c)
'''

'''
password = input("Enter your passcode: ")
if password == "admin":
    if len(password) >= 5:
        print("Correct password")
else:
    print("Incorrect password")

'''

'''
sbi = {"PIN" : 6600"}
pin = int(input("enter 4 digit pin: "))
if len(pin) == 4:
       if pin in sbi['PIN']:
           print("welconme")
       else:
           print("invalid")
else:
    print("pls enter 4 digit pin")

'''

'''
for
---------
> used to iterate over a sequence

a = "pyhton"
b = [1,2,3,4]
c = (5,6,7,8)
for how in a:
    print(how)

'''

'''
range() > is a built in function used to generate numbers in sequence manner
---------
syntax : range(start,end,step)

> else in for:
----------------------
> once iterations completed this else will be
'''

'''
for i in range(1,10):
    print(i)
else:
    print("ended")
    
'''

'''
break : used to exit from the loop when condition is met

for i in range(1,10):
    print(i)
    if i == 5:
        break
'''

'''
continue : used to skip the current iteration base on the condition



for i in range(1,10):
    print(i)
    if i == 5:
        continue
    print(i)

'''

'''
pass : space holder to avoid error after error

'''

'''
for i in range(1,10):
    if i == 3:
        pass

'''

i = 1
while i<5:
    print(i)
    i += 1
