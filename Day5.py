'''
sets
----------

> A set is a collection of  unuique and unordered elements
> Duplicate values are not allowed
> items are not stored in index order
> represented with {}

'''

'''
a = {1,2,2,3,4}
print(a)

'''
'''
Methods
------------
1. union : it will give values from 2 sets together in once
2. Intersection : to get common elemnts from both sets
3. difference : to get different values or elements from set
'''
'''
a = {12,9,2,45}
b = {43,99}
print(a|b)
print(a.union(b))

'''

'''
a = {78,54,19,46,12,80}
b = {45,21,19,46,50}
print(a.intersection(b))


a = {78,54,19,46,12,80}
b = {45,21,19,46,50}
print(a.difference(b))

'''

'''
symmetric difference

'''
'''
functions in sets

1. add() : To add new elements into set
2. update() : To add multiple items into set
3. remove() : used to remove values from the set. but it through error (key error) if element not in the set
4. descard() : used to remove element from the set. but it never through error
'''

'''
a = {78,54,19,46,12,80}
a.add(42)
print()
'''

'''
a = {78,54,19,46,12,80}
a.update([45,1])
print()
'''

a = {234,249,21,909}
a.discard(21)
print(a)

