# On demande à partir de quel nombre on veut commencer
depart = int(input("On commence le décollage à combien ? "))

print("Lancement imminent...")

# La boucle 'while' : TANT QUE le nombre est plus grand que 0
while depart > 0:
    print(f"{depart}...")
    depart = depart - 1

print()