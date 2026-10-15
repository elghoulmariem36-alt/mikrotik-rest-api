# mikrotik-rest-api

Scripts Python qui pilotent un routeur MikroTik CHR (RouterOS v7) via son API REST (TP 5).

## Prérequis

- Python 3
- Une VM MikroTik CHR v7 accessible, avec le service `www-ssl` activé et un utilisateur API dédié
- Les dépendances :

        python -m pip install requests python-dotenv

## Configuration

Créer à la racine un fichier `.env` (ignoré par Git, ne jamais le commiter) :

    DEVICE_HOST=192.168.174.10
    DEVICE_USER=api-user
    DEVICE_PASSWORD=votre_mot_de_passe

## Scripts

Les scripts se lancent depuis la racine du projet :

| Script | Rôle |
|---|---|
| `get_addresses.py` | Lit les adresses IP (GET) |
| `create_address.py` | Crée une adresse IP (PUT) |
| `update_address.py` | Modifie le commentaire d'une adresse (PATCH) |
| `delete_address.py` | Supprime une adresse (DELETE) |
| `configure_router.py` | Crée des routes statiques sans doublon (idempotent) |

Exemple :

    python get_addresses.py

## Remarques

- Avec l'API REST de RouterOS, la création d'un élément se fait avec `PUT`. `POST` sert à exécuter une commande précise (par exemple `/ip/address/add`).
- `verify=False` est utilisé car le certificat de la VM est auto-signé : acceptable en laboratoire, à éviter en production.
- `configure_router.py` est idempotent : relancé, il n'ajoute aucune route déjà présente.
