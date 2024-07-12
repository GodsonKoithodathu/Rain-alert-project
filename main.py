import requests
import smtplib
import os

my_email = "godson.koithodathu@gmail.com"
password = os.environ.get('PASSWORD')

WEATHER_FORCAST_URL = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = os.environ.get('API_KEY')
LAT = 19.832930
LONG = 75.891800

weather_parameters = {
    "lat": LAT,
    "lon": LONG,
    "appid": API_KEY,
    "cnt": 4,
}

response = requests.get(url=WEATHER_FORCAST_URL, params=weather_parameters)
# print(response.status_code)
weather_data = response.json()
# print(weather_data)

# this can be a logic:
# weather_list = []
# for num in range(4):
#     weather_list.append(weather_data["list"][num]["weather"][0]["id"])
# print(weather_list)
#
# for number in weather_list:
#     if number < 700:
#         print("It's rainy")


# this is the logic that will also work:
will_rain = False

for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True

if will_rain:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="godson.koithodathu@yahoo.com",
                            msg="Subject: Rain alert\n\n"
                                "It's going to rain today, carry your umbrella.")
