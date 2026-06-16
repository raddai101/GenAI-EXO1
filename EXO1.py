import random



def nombre_mystere():
    
    print("Bienvenue dans le jeu du nombre mystère !")
    
    nombre_mystere = random.randint(1, 100)
    essais = 0
    score = 100
    while True:
        try:
            essais += 1
            nombre_utilisateur = int(input("Entrez un nombre entre 1 et 100 : "))
            print("choississez une option : 1. Continuer à jouer 2. Quitter le jeu")
            
            if nombre_utilisateur < nombre_mystere:
                print("Le nombre mystère est plus grand.")
            elif nombre_utilisateur > nombre_mystere:
                print("Le nombre mystère est plus petit.")
            elif nombre_utilisateur < 1 or nombre_utilisateur > 100:
                print("Veuillez entrer un nombre valide entre 1 et 100.")
            elif nombre_utilisateur == nombre_mystere:
                print(f"Bravo ! Vous avez trouvé le nombre mystère en {essais} essais.")
                score -= essais 
                print(f"Votre score est de {score}.")
                choi_utilisateur = input("Voulez-vous continuer de jouer ? (o/n) ")
                if choi_utilisateur.lower() != "o":
                    print("Merci d'avoir joué ! À bientôt.")
                    break
        except ValueError:
            print("Veuillez entrer un nombre valide.")   
        
nombre_mystere()
# if "___name__" == "__main__":
#     nombre_mystere()