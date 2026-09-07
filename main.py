from http.server import HTTPServer, BaseHTTPRequestHandler
import threading
import urllib.request
import json
import time

# Server dummy kecil agar Render mendeteksi sebagai Web Service aktif
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Radar Shorts 24/7 Active!")

def run_server():
    server = HTTPServer(('0.0.0.0', 10000), SimpleHTTPRequestHandler)
    server.serve_forever()

# Jalankan server dummy di latar belakang
threading.Thread(target=run_server, daemon=True).start()

# --- SCRIPT BOT RADAR KAMU DI BAWAH SINI ---
TELEGRAM_TOKEN = "8914614490:AAFc7BUBvOMuYaAqagCi2cJIjfhnSxSCaWk"
CHAT_ID = "5743211849"

TARGET_VIEWS = 50000
MAX_AGE_HOURS = 2

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
