'''

time = input("Enter 24 hours format: ")

parts_ = time.split(":")

hour_ = int(parts_[0])
min_ = int(parts_[1])

print(f"{time} is converted into {hour_ - 12}:{min_} pm")

'''

'''

List
----------
> List is a collection of different data types represented in square brackets [] and separated by commas
>mutable
a = [1,"apple",[1,2]}
print (a)
'''

'''
a = [1, "python",[1,2,[34,"this is python 3rd class",78],"python is a language",89],34,[3,4]]


#print(a[2][2][1][8])
print(a[2][4])
'''

'''
Methods
----------
> append() : Used to add new item into list at last index position
> extend() : this method is used to add iterables inot list and it will in the last index position, each value or substring is each index in the list

'''

'''
a = [1,2,3]
a.append(9)
print(a)
a.append([20,90])
print(a)
'''
'''
a = [1,2,3]
a.extend([20,90])
print(a)
'''

'''
Immutable
--------------
> could not modify on that particular variable
eg: int,str

Mutable
-------------
> can able modify on that particular variable
eg: list
'''

'''
pop()
-------------
> used to remove the items from list, but will mention here index position in the pop method

a= [12,34,42]
a.pop(2)
print(a)
'''
