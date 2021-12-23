import requests 
from twilio.rest import Client

MY_LAT = 17.3753
MY_LON = 78.4744
api_key = "146fbf15285254d06b9314f767a6a2f8"
account_sid = "AC5b0dc06e44b1bf72a68a003ae5b031a5"
auth_token = "882ba524719386b51c0302b3f1297c31"
parameter = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "appid": api_key,
    "exclude": "current, minutely, daily"
}
will_rain = False

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameter) 
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It is going rain, bring umbrella ☂️",
        from_= "+17153143894",
        to="+917989490464"
    )

    print(message.status)