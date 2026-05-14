'''
Operators

1. Arthemetic operators

'''

'''
print (2*3)
print (4%5 == 0)
print (10**2)
print(10/2)
print (35.24//5)

'''

'''

2. Assignment Operator
--------------------

=, +=, -=, %=, *=
'''

'''
count = 0
for j in range(1,10):
    count += 1
print(count)

'''

'''

3. Comparison operator
------------------------------
== --> both values are equal or not

==, !=,  >=, <=,
'''
'''
a = 5
b = 2
print(a==b)
'''

'''

4. Identity Operator
------------------------
is,is not

is -> This operator looks fo the object is same or not

'''

'''
a = [1,2]
b = [1,2]
c=a
print(a == b)
print(id(a))
print(id(b))
print(id(c))
print(a is c)
print( a is not b)
'''

'''

5. Logical
--------------------

and --> to check both should be true
or
not
'''

'''
a = 5
if a % 3 == 0 and a % 5 == 0:
    print("Success")
else:
    print("fail")

'''

'''
a = 5
if a % 3 == 0 or a % 5 == 0:
    print("Success")
else:
    print("fail")

'''

'''
6. Membership

-------------------

in,not in
'''

'''

7. Biteise operator
---------------------

&, |, <<, >>

'''


'''

                  Strings

--> String is a sequence of characters that are enclosed in ''."", and string is immutable

'''

'''
String Methods

-----------------
replace() --> used to replace with new substring
syntax --> var_name.replace("old string","new string")
'''

'''
a = "python program"
print (a.replace("python","java"))
print(a)
'''
'''
split() --> used to separate into parts, and split based on the substring where before substring is one index and after is another index in the list

syntax --> var_name.split("substring")

a = "python program"
print (a.split())

'''

'''
a = "python program"
print(len(a))
'''

'''
slicing()
------------
--> can give the access of to get particular index from string.
'''

'''
a = "python program"
print(a[3:8])
'''

'''
indexing
-----------
--> used to get substring present  in that index pos
'''

'''
a = "python program"
print(a[4])
print(a.index("ram"))
'''
