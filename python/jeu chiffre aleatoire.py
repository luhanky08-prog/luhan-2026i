#===================================
#Luhan.K / 2025
#===================================
import random

# Liste de mots
mots = ["python", "ordinateur", "fromage", "soleil", "voiture",
    "montagne", "chocolat", "musique", "jardin", "papillon",
    "volcan", "diamant", "cascade", "astronaute", "pyramide"]

# Choisir un mot au hasard
mot_secret = random.choice(mots)
lettres_trouvees = []
erreurs = 0
max_erreurs = 6

print("🎮 Bienvenue au jeu du pendu !")

while erreurs < max_erreurs:
    affichage = ""
    for lettre in mot_secret:
        if lettre in lettres_trouvees:
            affichage += lettre + " "
        else:
            affichage += "_ "

    print("\nMot :", affichage)

    if "_" not in affichage:
        print("🎉 Bravo ! Vous avez gagné !")
        break

    proposition = input("Proposez une lettre : ").lower()

    if proposition in mot_secret:
        print("✅ Bonne lettre !")
        lettres_trouvees.append(proposition)
    else:
        print("❌ Mauvaise lettre !")
        erreurs += 1
        print("Erreurs :", erreurs, "/", max_erreurs)

if erreurs == max_erreurs:
    print("💀 Vous avez perdu ! Le mot était :", mot_secret)
