import socket

target = "127.0.0.1"
# On va tester une liste de ports courants
ports = [22,80,443,631]

print(f"--- Scan de ports sur {target} ---")

for port in ports:
    # On crée une "prise" (socket) réseau
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # On définit un temps d'attente court (0.5 seconde)
    s.settimeout(0.5)

    # On tente de se connecter au port
    resultat = s.connect_ex((target, port))

    if resultat == 0:
        print(f"Port {port} : Ouvert")
    else:
        print(f"Port {port} : Fermé")

    s.close()