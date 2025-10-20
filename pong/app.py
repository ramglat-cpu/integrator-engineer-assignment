from flask import Flask, jsonify
import os, socket

app = Flask(__name__)

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 80))
        return s.getsockname()[0]
    finally:
        s.close()

@app.get("/info")
def info():
    return jsonify({
        "service": "pong",
        "hostname": socket.gethostname(),
        "ip": get_ip(),
        "env": os.getenv("APP_ENV", "dev")
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PONG_PORT", "8001")))
