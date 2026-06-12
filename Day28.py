'''

  Regular Expression

--------------------------------

> RegEx is a sequence of char that form a searching pattern
> This can be used to check if a string contain the specified search pattern
> Python has a built in package called 're' which can be used to work with RegEx

Functions in re
-------------------------

1. Findall
2. search
3. fullmatch

Metachar
----------------
[] --> a-z,A-Z,0-9
. --> here each dot is one char
^ --> This look for the, string is starting with specified squence or not
$ --> This look for the, string is ending with specified squence or not.
* --> Zero or more
? --> Zero or one
+ --> one or more
{} -->

Special Sequence
------------------
\S ---> No space
\s ---> only space
\D ---> non-digits
\d ---> only-digits
\w ---> matches any word char (letters, digits, underscore)
\W ---> Non-words

import re
aa = " c is a foundational, general purpose"
print(re.findall('[pu....e]',aa))


import re
aa = "python is a foundational, 7general-purpose"
print(re.findall('P.*thon',aa))

'''

'''
import re
aa = "python is a foundational, 7general-purpose"
print(re.findall('P.?thon',aa))
'''

'''
import re
aa = "Python is a foundational"
print(re.findall('P.{7}',aa))


import re
aa = "Pyhton is a foundational"
print(re.findall('\S',aa))


import re
mob = input("enter mob number: ")
pattern = re.fullmatch('[6-9][0-9]{9}',mob)
if pattern:
    print(f"{mob} is indian number")
else:
    print(f"{mob} is not indian number")

'''


import re
landline = input("Enter landline number: ")
pattern = re.fullmatch(r"0[0-9]{2,4}-[0-9]{6,8}", landline)
if pattern:
    print("Valid landline number")
else:
    print("Invalid landline number")
