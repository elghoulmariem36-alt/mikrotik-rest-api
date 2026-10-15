import requests
from config import BASE_URL, AUTH

TARGET = "192.168.20.1/24"

# 1. GET filtré pour retrouver le .id de cette adresse uniquement
resp = requests.get(f"{BASE_URL}/ip/address", params={"address": TARGET},
                    auth=AUTH, verify=False, timeout=5)
resp.raise_for_status()
items = resp.json()
if not items:
    raise SystemExit(f"{TARGET} introuvable")
addr_id = items[0][".id"]
print("id trouvé :", addr_id)

# 2. PATCH : modifier le commentaire
resp = requests.patch(f"{BASE_URL}/ip/address/{addr_id}",
                      json={"comment": "modifié via l'API"},
                      auth=AUTH, verify=False, timeout=5)
print(resp.status_code)
print(resp.text)
resp.raise_for_status()
