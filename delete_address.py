import requests
from config import BASE_URL, AUTH

TARGET = "192.168.20.1/24"

resp = requests.get(f"{BASE_URL}/ip/address", params={"address": TARGET},
                    auth=AUTH, verify=False, timeout=5)
resp.raise_for_status()
items = resp.json()
if not items:
    raise SystemExit(f"{TARGET} introuvable")
addr_id = items[0][".id"]

resp = requests.delete(f"{BASE_URL}/ip/address/{addr_id}",
                       auth=AUTH, verify=False, timeout=5)
print(resp.status_code)
resp.raise_for_status()
