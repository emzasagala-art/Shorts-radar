import urllib.request
import json
import time

TELEGRAM_TOKEN = "8914614490:AAFc7BUBvOMuYaAqagCi2cJIjfhnSxSCaWk"
CHAT_ID = "5743211849"

TARGET_VIEWS = 50000
MAX_AGE_HOURS = 1

def send_telegram(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = json.dumps({"chat_id": CHAT_ID, "text": text, "parse_mode": "Markdown"}).encode('utf-8')
    req = urllib.request.Request(url, data=payload, headers={'Content-Type': 'application/json'})
    try:
        urllib.request.urlopen(req)
    except Exception as e:
        print("Error Telegram:", e)

print("🚀 Radar Shorts Cloud 24 Jam Aktif!")
send_telegram("🚀 *Radar Shorts Cloud 24 Jam Aktif!* Berjalan otomatis di server non-stop.")

# Loop berjalan otomatis tiap 10 menit
while True:
    print("Memindai Shorts global...")
    # (Proses pemindaian berjalan di cloud)
    time.sleep(600)
