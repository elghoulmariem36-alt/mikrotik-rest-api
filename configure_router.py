import requests
from config import BASE_URL, AUTH

ROUTES = [
    {"dst-address": "10.10.10.0/24", "gateway": "192.168.174.1"},
    {"dst-address": "10.20.20.0/24", "gateway": "192.168.174.1"},
    {"dst-address": "172.16.0.0/16", "gateway": "192.168.174.1"},
]


def get_existing_routes():
    """Retourne l'ensemble des routes déjà présentes sur le routeur."""
    resp = requests.get(f"{BASE_URL}/ip/route", auth=AUTH, verify=False, timeout=5)
    resp.raise_for_status()
    return {(r.get("dst-address"), r.get("gateway")) for r in resp.json()}


def main():
    existing = get_existing_routes()
    for route in ROUTES:
        key = (route["dst-address"], route["gateway"])
        if key in existing:
            print(f"= déjà présente : {key[0]} via {key[1]}")
            continue
        resp = requests.put(f"{BASE_URL}/ip/route", json=route,
                            auth=AUTH, verify=False, timeout=5)
        if not resp.ok:
            print(f"! erreur {resp.status_code} : {resp.text}")
            resp.raise_for_status()
        print(f"+ créée : {key[0]} via {key[1]}")


if __name__ == "__main__":
    main()
