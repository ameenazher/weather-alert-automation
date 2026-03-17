# 🌧️ Weather Alert Automation

An automated weather monitoring system that sends WhatsApp alerts when rain is detected.

---

## 🚀 Features
- ⏰ Automated execution via GitHub Actions
- 🌦️ Real-time weather data from OpenWeather API
- 📲 WhatsApp alerts using Twilio
- 🌧️ Smart rain detection logic
- 🔐 Secure environment variables handling

---

## 🛠️ Tech Stack
- Python 3
- GitHub Actions (CI/CD automation)
- OpenWeatherMap API
- Twilio API

---

## ⚙️ How It Works
1. GitHub Actions triggers the script on a schedule
2. The script fetches weather data for Baghdad
3. Rain conditions are analyzed:
   - Rain volume (mm)
   - Weather condition codes
4. If rain is detected → WhatsApp message is sent

---

## 🔐 Environment Variables
Set these in your GitHub repository secrets:

- `OWM_API_KEY` → OpenWeather API key
- `ACCOUNT_SID` → Twilio Account SID
- `AUTH_TOKEN` → Twilio Auth Token

---

## 📦 Installation (Local Run)

```bash
git clone https://github.com/your-username/weather-alert.git
cd weather-alert
pip install -r requirements.txt
python main.py
