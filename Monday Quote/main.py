import smtplib
import datetime as dt
import random

now=dt.datetime.now()
current_day=now.weekday()

with open('quotes.txt', mode='r') as file:
    list_of_quotes=file.readlines()
if current_day==0:
    my_email='my_email@gmail.com'
    password='my_app_password'
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,to_addrs='random@yahoo.com',msg=random.choice(list_of_quotes))
