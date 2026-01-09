import requests # Si erreur : tape 'pip install requests' dans le terminal

url = "https://www.google.com"

print(f"--- Requête HTTP (Couche 7) vers {url} ---")

try:
    # On effectue la requête
    reponse = requests.get(url)

    # Le status_code 200 est le code universel pour "Succès"
    print(f"Statut de la réponse : {reponse.status_code}")

    # On affiche les en-têtes (Headers) : c'est la "carte d'identité" du serveur
    print(f"Serveur détecté : {reponse.headers.get('Server', 'Inconnu')}")

    # On affiche un extrait du code HTML (ce que voit le navigateur)
    print(f"\nExtrait du contenu HTML : ")
    print(reponse.text[:150] + "...")

except Exception as e:
    print(f"Erreur lors de la requête : {e}")