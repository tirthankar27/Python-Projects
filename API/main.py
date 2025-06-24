import requests
import datetime as dt
import smtplib

MY_LAT=22.572645
MY_LONG=88.363892
MY_POSITION=tuple((MY_LAT,MY_LONG))
MY_EMAIL='abc@gmail.com'
MY_PASSWORD='yxawekkajsccsaw'

parameters={
    "lat":MY_LAT,
    "lng":MY_LONG,
    "formatted":0
}

sun_response = requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)

sun_response.raise_for_status()
data=sun_response.json()

sunrise=int(data['results']['sunrise'].split('T')[1].replace("+00:00","").split(':')[0])
sunset=int(data['results']['sunset'].split('T')[1].replace("+00:00","").split(':')[0])
current_time=dt.datetime.now()
current_hour=current_time.hour

response = requests.get(url="http://api.open-notify.org/iss-now.json")

response.raise_for_status()
data=response.json()

longitude = data['iss_position']['longitude']
latitude = data['iss_position']['latitude']
curr_position = tuple((latitude,longitude))

if MY_POSITION==curr_position and (sunset<current_hour or current_hour<sunrise):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL,password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,to_addrs='random@yahoo.com',msg="Look at ISS now!")

