#!/bin/bash

# Automatisation : La mission identity_manager.sh
# Création de mon premier script Bash.
# Dans la VM, crée un fichier : nano identity_manager.sh.

# Script d'automatisation : Création d'utilisateur
echo "--- Début de la création de l'utilisateur stagiaire ---"

# 1. Création de l'utilisateur avec son dossier home et bash
useradd -m -s /bin/bash stagiaire

# 2. Création du groupe formation
groupadd formation

# 3. Ajout au groupe
usermod -aG formation stagiaire

echo "Utilisateur stagiaire créé et ajouté au groupe formation."
echo "Vérification des infos :"
id stagiaire

# Rendre script exécutable : chmod +x identity_manager.sh.
# Lancer le : ./identity_manager.sh.