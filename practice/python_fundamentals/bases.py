# Ceci est commentaire (le # dit à Python d'ignorer cette ligne)
prenom = "Tehe"     # Une chaîne de caractères (du texte)
age = 29            # Un nombre entier
taille = 1.85       # Un nombre à virgule (on utilise un point en Python)
age_annee = "ans"   # Une chaîne de caractères (du texte)

#print(prenom)

annee_actuelle = 2026
anne_naissance = 1996

# Python fait le calcul et range le résultat dans une nouvelle variable
age_calcule = annee_actuelle - anne_naissance

print("Tehe, tu as ou tu vas avoir :")
print(age_calcule,"ans")        #En mettant une virgule entre les éléments dans print(), Python ajoute automatiquement un espace et gère le mélange des types pour toi.

print(f"{age_calcule} ans")     #C'est la méthode recommandée aujourd'hui. On place un f avant les guillemets et on met la variable entre accolades {}.

print(str(age_calcule) + " ans") #Si tu veux absolument utiliser le signe +, tu dois transformer le nombre en texte manuellement.

print(f"Tehe tu vas avoir ou tu à déja {age_calcule} ans ?")