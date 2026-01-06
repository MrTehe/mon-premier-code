# On pose une question et on range la réponse dans une variable
user = input("Comment t'appelles-tu ? ")

print(f"Enchanté {user}, je suis ton premier programme sur Debian !")

# ATTENTION AU PIÈGE : input() renvoie TOUJOURS du texte.
# Si on veut faire un calcul, il faut transformer la réponse en nombre.
age_texte = input("Quel âge as-tu ? ")
age_nombre = int(age_texte) # On transforme le texte "25" en nombre 25

prochain_age = age_nombre + 1
print(f"Cette année, tu auras {prochain_age} ans !")