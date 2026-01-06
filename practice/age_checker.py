age = int(input("Quel est ton âge ? "))

if age >= 18:   # À noter : > * >= signifie "supérieur ou égal".
    print("Accès autorisé : Tu es majeur.")
    print("Bienvenue dans le système.")

elif age >= 13:
    print("Accès restreint : Tu es un ado.")
    
else:           # L'indentation (le décalage) : Remarque que les print sont décalés vers la droite après les :. En Python, c'est ce décalage qui indique quelles lignes appartiennent au "Si". Si tu ne décales pas, ça ne marchera pas !
    print("Accès refusé : Tu es trop jeune.")