🧩 Ping-Pong Microservices

Integrator Engineer Assignment Solution

📘 Overview

This project demonstrates a simple microservices setup using Python (Flask), Docker, and Docker Compose.
It contains two separate services – one that responds (pong) and one that requests (ping) – both running in isolated containers and communicating over Docker’s internal network.

⚙️ Project Structure
ping-pong/
├─ ping/
│  ├─ app.py
│  ├─ requirements.txt
│  └─ Dockerfile
├─ pong/
│  ├─ app.py
│  ├─ requirements.txt
│  └─ Dockerfile
├─ .env
├─ docker-compose.yml
└─ README.md

🧩 Services
🟢 PONG (server)

Flask app running on port 8001

Returns information about itself:

{
  "service": "pong",
  "hostname": "<container_name>",
  "ip": "<container_ip>",
  "env": "dev"
}

🔵 PING (client)

Flask app running on port 8000

Sends an HTTP GET request to http://pong:8001/info

Returns the received JSON from pong:

{
  "ping": "ok",
  "pong_data": { ... }
}

🐳 Docker Setup

Each service has its own Dockerfile based on python:3.11-slim.
docker-compose.yml builds and runs both containers together.

🌱 Environment Configuration (.env)
APP_ENV=dev
PING_PORT=8000
PONG_PORT=8001

🚀 How to Run
docker compose up --build


Then open your browser at:
👉 http://localhost:8000/ping

Expected output:

{
  "ping": "ok",
  "pong_data": {
    "service": "pong",
    "hostname": "pong-container",
    "ip": "172.18.0.x",
    "env": "dev"
  }
}

🧹 To Stop
Ctrl + C
docker compose down

✅ Result

✅ Both containers run successfully
✅ Service-to-service communication verified
✅ Environment management via .env
✅ Fully meets the assignment requirements
  ✅