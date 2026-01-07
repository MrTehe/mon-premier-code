# Utilise une condition if et la fonction len() pour vérifier si le mot de passe fait plus de 8 caractères.
mdp = input("Veuillez choisir un mot de passe : ")

longueur = len(mdp)

if longueur > 8:
    print("Sécurisé : Votre mot de passe est assez long.")
else:
    print("Danger ! Votre mot de passe est trop court.")

# Le type de donnée : len() renvoie toujours un nombre entier. C'est pour cela qu'on peut utiliser le signe > (plus grand que) pour le comparer à 8.
# L'indentation : N'oubliez pas l'espace (la tabulation) après le if et le else. C'est la règle d'or en Python pour que le code comprenne ce qui appartient à la condition.