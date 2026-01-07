import os
from dotenv import load_dotenv

# 1. On charge les variables du fichier .env
load_dotenv()

# 2. On récupère l'IP du .env au lieu de l'écrire en dur
# Si GATEWAY_IP n'existe pas, il prendra "127.0.0.1" par défaut
ip_box = os.getenv("GATEWAY_IP", "127.0.0.1")

test_ip = input("Quelle IP voulez-vous tester ? ")

# On définit l'adresse IP de votre Box (Gateway)
# Remplacez X.X par les chiffres que vous avez trouvés tout à l'heure
# ip_box = "172.X.X.X"

print(f"--- Vérification de la connexion vers {ip_box} ---")

# On lance la commande ping : -c 1 signifie "envoyer 1 seul paquet"
# On utilise l'IP que TU tapes au début du programme
reponse = os.system(f"ping -c 1 {test_ip}")

# En informatique, une commande réussie renvoie souvent le code 0
if reponse == 0:
    print("Succès : La Box répond, le réseau est opérationnel !")
else:
    print("Échec : La Box ne répond pas. Vérifiez vos couches 1 et 2.")