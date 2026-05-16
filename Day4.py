'''
concatination
------------------
> The (+) for int and can, but for the other data types it will act as concatinating the datatype


a = 90
b = 8
print(a+b)
aa = "py"
so = "lang"
print(aa + so)

am = [2,4]
an = [6,7]
print(an + am)

'''

'''
Tuple
---------------
> collection of different data types separated by commas, represented in () and immutable

> Methods

1. count() : used to count particular item in the tuple
2. index() : used to find index positon of the item and only gives the first occurence


'''

'''
example = (1,"pthon", [1,2],(3,4))
print(example.index((3,4)))


example = (1,"pthon", [1,2],(3,4))
print(example.count((3,4)))
'''

'''
a = (1, 'python', [1, 2, [34, 'this is python 3rd class', 78], 'python is a language', 89], 34, [3, 4])

print(a[2][2][2])

'''

'''
Dictionary
--------------
> key : value pair separated by ':' represented in {}

> values() : used to get all values from the dict

> items() : used to get key and value together
'''

'''
badri = {"Name" : "Badrinadh", 1 : 2, (1,2) : [3,4]}
print(badri)
'''
'''
d = {
    "name": "Badrinadh",
    "age": 22,
    "course": "Python"
}

print(d[input("Enter key: ")])
'''

'''
update()
--------------
> used to add new key value pair into dict
'''

d = {
    "name": "Badrinadh",
    "age": 22,
    "course": "Python"
}

d.update({"pan" : "QWEOP23O"})
print(d[input("Enter key: ")])
