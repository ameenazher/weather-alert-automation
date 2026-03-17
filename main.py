import requests
import os
from twilio.rest import Client

# 🔐 Secrets
api_key = os.environ.get("OWM_API_KEY")
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")

# 📍 Baghdad
lat = 33.314690
lon = 44.376759

url = "https://api.openweathermap.org/data/2.5/weather"

params = {
    "lat": lat,
    "lon": lon,
    "appid": api_key,
    "units": "metric"
}

response = requests.get(url, params=params)

if response.status_code != 200:
    print("❌ API request failed")
    exit()

data = response.json()

if "main" in data:
    temp = data["main"]["temp"]
    weather = data["weather"][0]["description"]
    weather_id = data["weather"][0]["id"]
    rain = data.get("rain", {}).get("1h", 0)

    city = data["name"]

    message_text = f"""
🌧️ Weather Alert - {city}

🌡️ Temp: {temp}°C
🌥️ Condition: {weather}
🌧️ Rain: {rain} mm
"""

    print(message_text)

    # 🚨 Send only if rain detected
    if rain > 0 or (200 <= weather_id < 600):
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            from_="whatsapp:+14155238886",
            body=message_text,
            to="whatsapp:+964XXXXXXXXXX"
        )

        print("✅ WhatsApp Message Sent!")
    else:
        print("☀️ No rain → No message sent")

else:
    print("❌ API Error:", data)
