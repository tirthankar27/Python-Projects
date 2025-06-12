import pandas as pd
import smtplib
import datetime as dt
import random

now=dt.datetime.now()
year=now.year
month=now.month
day=now.day
data_file=pd.read_csv('birthdays.csv').to_dict(orient='records')
letters=['letter_1.txt','letter_2.txt','letter_3.txt']

for data in data_file:
    if int(data['month'])==month and int(data['day'])==day:
        with open(f"letter_templates/{random.choice(letters)}") as file:
            letter=file.read()
            new_letter = letter.replace('[NAME]', data['name'])
        my_email='example@gmail.com'
        password='my_app_password'
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=my_email,password=password)
            connection.sendmail(from_addr=my_email,to_addrs=data['email'],msg=f"Subject:Happy Birthday!\n\n{new_letter}")
