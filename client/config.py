import os
import socket
from dotenv import load_dotenv

load_dotenv()

SERVER_IP = os.getenv("SERVER_IP", "127.0.0.1")
SERVER_PORT = os.getenv("SERVER_PORT", "5000")
SERVER_ENDPOINT = os.getenv("SERVER_ENDPOINT", "/metrics")
SAMPLING_INTERVAL = int(os.getenv("SAMPLING_INTERVAL_SECONDS", "10"))
DEVICE_ID = os.getenv("DEVICE_ID", f"PC-{socket.gethostname()}")

SERVER_URL = f"http://{SERVER_IP}:{SERVER_PORT}{SERVER_ENDPOINT}"