'''

validation
-----------------

1. Mobile Number
------------------
rules

> 10 digits number
-----------------------

2. Password
----------------------
> Capital, small. digit, special character, atleast 8

--------------------

3. gmail
----------------
> @gmail.com

'''

'''
import re
def mobile_validation():
    mob = input("enter mobile number: ")
    pattern = re.fullmatch(r"[6-9] [0-9]{9}",mob)
    if pattern:
        print(f"valid mobile number")
    else:
        print(f"invalid number")
mobile_validation()
    
'''

'''
import re
class Mobilevalidation:
    def validate(self):
        mob = input("enter mobile number: ")
        pattern = re.fullmatch(r"[6-9][0-9]{9}",mob)
        if pattern:
            print(f"valid")
        else:
            print(f"invalid")
obj = Mobilevalidation()
obj.validate()
'''

'''
import re
class passwordvalidation:
    def validate(self):
        password = input("Enter Password: ")
        pattern = re.fullmatch(r"(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%^&*!]).{8,}",password)
        if pattern:
            print(f"valid password")
        else:
            print(f"invalid")
obj = passwordvalidation()
obj.validate()
'''

'''
import re
class gmailvalidation:
    def validate(self):
        gmail = input("enter your gmail: ")
        pattern  = re.fullmatch(r"[a-zA-Z0-9._]+@gmail\.com",gmail)
        if pattern:
            print(f"valid email")
        else:
            print(f"invalid emial")
obj = gmailvalidation()
obj.validate()
'''

import re
class UserValidation:
    def validate(self):
        name = input("Enter Name: ")
        email = input("Enter Email: ")
        mobile = input("Enter Mobile Number: ")
        password = input("Enter Password: ")
        name_pattern = re.fullmatch(r"[A-Za-z ]{3,}", name)
        email_pattern = re.fullmatch(r"[a-zA-Z0-9._]+@gmail\.com", email)
        mobile_pattern = re.fullmatch(r"[6-9][0-9]{9}", mobile)
        password_pattern = re.fullmatch(
            r"(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%^&*!]).{8,}",password)
        if name_pattern:
            print(" Valid Name")
        else:
            print(" Invalid Name")

        if email_pattern:
            print(" Valid Email")
        else:
            print(" Invalid Email")

        if mobile_pattern:
            print(" Valid Mobile Number")
        else:
            print(" Invalid Mobile Number")

        if password_pattern:
            print(" Valid Password")
        else:
            print(" Invalid Password")
obj = UserValidation()
obj.validate()



