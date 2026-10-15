import os
import urllib3
from dotenv import load_dotenv

load_dotenv()
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

HOST = os.getenv("DEVICE_HOST")
USER = os.getenv("DEVICE_USER")
PASSWORD = os.getenv("DEVICE_PASSWORD")

if not all([HOST, USER, PASSWORD]):
    raise SystemExit("Variables manquantes dans .env")

BASE_URL = f"https://{HOST}/rest"
AUTH = (USER, PASSWORD)
