'''
Date and Time

---------------------------

> Python provides the built in date time module to work with dates and time

import datetime
----------------------



import datetime
today = datetime.date.today()
now = datetime.datetime.now()
print(now)
print(today)



import datetime
now = datetime.datetime.now()

print(f"year is {now.year}")
print(f"Month is {now.month}")
print(f"Day is {now.day}")
print(f"Hour is {now.hour}")
print(f"Minute is {now.minute}")
print(f"Seconds is {now.second}")



Formatting date and time
---------------------------
> strftime() is used to formate date and time
%d --> day
%m --> month
%Y --> Year
%H --> Hour
%M --> min
%S --> sec

import datetime
now = datetime.datetime.now()
print(now.strftime("%d-%m-%y"))
print(now.strftime("%H-%M-%S"))

'''
'''
import datetime
date1 = datetime.date(2026,6,1)
date2 = datetime.date(2026,6,15)
diff = date2 -date1
print(f"difference is: {diff}")


import datetime
today = datetime.date.today()
future = today + datetime.timedelta(days = 7)
print(f"future is : {future}")



import datetime
days = datetime.date.today()
print(days.ctime())



import calendar
import datetime

today = datetime.date.today()
year = today.year
month = today.month
print(calendar.month(year,month))

'''
'''
import calendar
year = 2025
month = 12
print(calendar.month(year,month))

'''

'''
import calendar
year = 2026
print(calendar.calendar(year))

'''
'''
import calendar
year = 2026
print(calendar.calendar(2016))

'''

'''
import datetime
import time
import smtplib
from email.message import EmailMessage
while True:
    now = datetime.now().strftime("%H:%M")
    if now == "10:15":
        sender = "nandigambadrinadh4@gmail.com"
        password = "qrdz ulie ylfd zivk"
        msg = EmailMessage()
        msg = EmailMessage()
        msg["Subject"] = "Test mail"
        msg["From"] = sender
        msg["To"] = "nadhbadri2@gmail.com"
        msg.set_content("Hi this is test message")
        server = smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        server.login(sender,password)
        server.send_message(msg)
        server.quit()
        print("Email Sent")
        break
    time.sleep(30)

    '''

from datetime import datetime
import time
import smtplib
from email.message import EmailMessage
while True:
    now = datetime.now().strftime("%H:%M")
    if now == "10:24":
        sender = "nandigambadrinadh4@gmail.com"
        password = "qrdz ulie ylfd zivk"
        msg = EmailMessage()
        msg["Subject"] = "Test Mail"
        msg["From"] = sender
        msg["To"] = "nadhbadri2@gmail.com"
        msg.set_content("Dear Sir/Madam,\n\n" "This is a test email to verify sucessful email delivery.\n\n""Thank you.")
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender, password)
        server.send_message(msg)
        server.quit()
        print("Email Sent")
        break
    time.sleep(30)
