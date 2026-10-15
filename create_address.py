import requests
from config import BASE_URL, AUTH

payload = {"address": "192.168.20.1/24", "interface": "ether2", "comment": "TP5"}

resp = requests.put(f"{BASE_URL}/ip/address", json=payload, auth=AUTH, verify=False, timeout=5)
print(resp.status_code)
print(resp.text)
resp.raise_for_status()
