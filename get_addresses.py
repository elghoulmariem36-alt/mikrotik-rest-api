import requests
from config import BASE_URL, AUTH

resp = requests.get(f"{BASE_URL}/ip/address", auth=AUTH, verify=False, timeout=5)
resp.raise_for_status()

for item in resp.json():
    print(item[".id"], item["address"], item["interface"])
