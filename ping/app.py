from flask import Flask, jsonify
import os, requests

app = Flask(__name__)

@app.get("/ping")
def ping():
    url = f"http://pong:{os.getenv('PONG_PORT', '8001')}/info"
    try:
        r = requests.get(url, timeout=3)
        r.raise_for_status()
        return jsonify({"ping": "ok", "pong_data": r.json()})
    except Exception as e:
        return jsonify({"ping": "fail", "error": str(e)}), 502

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PING_PORT", "8000")))
