'''

File Handling



> File Handler is a object of a file to maintain serveral functions of file
such as creating, reading, update and deleteing the file.


open a file
--------------

1. open()
2. with open()

Modes
------------

'r' --> is used to reading  the file, error if file does not exist
'a' --> is used to add the text into file, if file does not exit
'w' --> is used to add the txtx into file but it will override of all txt inside file
        if the file does not exists it will create with that name.
'x' --> is used to create the file...but eill throw error if we are used
'r' mode to create.




file = open("C:/Users/VIJAYALAKSHMI/OneDrive/Desktop/Ts_codes.txt", "r")
content = file.read()
print(content)
file.close()



with open("demo.txt", "r") as file:
    content = file.read()
    print(content)

    '''

'''
methods
---------

write()
read()
------------
> This method can read entire file chunk by chunk 


readline()
------------------
> can read only one line at a time in a file

readlines()
--------------------
>it will read entire file and gives in a list where each line is each index
 in the list

'''

'''
with open('demo.txt', 'r') as an:
    print(an.read())
'''
'''
file = open("demo.txt", "r")
'''
'''
file = open("demo.txt", "a")
file.write("Hello")
'''
'''
with open("demo.txt", "r") as file:
    print(file.read())
    '''
'''
with open("demo.txt", "w") as file:
    file.write("Python")
'''

'''
with open("demo.txt", "a") as file:
    file.write("\nPython")
'''
'''
any_ = open('demo.txt','r')
print(any_.readlines())
any_.close()

'''

with open("demo.txt", "r") as file:
    print(file.read())
