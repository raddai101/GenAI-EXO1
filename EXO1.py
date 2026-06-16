import random



def nombre_mystere():
    
    print("Bienvenue dans le jeu du nombre mystère !")
    n = 100
    nombre_mystere = random.randint(1, n)
    essais = 0
    score = 100
    while True:
        try:
            options = int(input("Voulez-vous jouer ? (1 pour oui, 2 pour non) "))
            if options == 1:
                essais += 1
                nombre_utilisateur = int(input("Entrez un nombre entre 1 et 100 : "))
            else:
                print("Au revoir !")
                break
            personnage = input("Voulez-vous créer de personnage ? (o/n)  ") or input("Voulez-vous continuer de jouer ? (o/n) ")
            if personnage.lower() != "o":
                print("passons au jeu.")
                continue
            else:
                nom = input("Entrez le nom de votre personnage : ")
                print(f"Bienvenue, {nom} ! amusez-vous bien.")
            
            
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
                choi_utilisateur = input(f"Voulez-vous continuer de jouer {nom} ? (o/n) ")
                if choi_utilisateur.lower() != "o":
                    print(f"Merci d'avoir joué {nom} ! À bientôt.")
                    break
        except ValueError:
            print("Veuillez entrer un nombre valide.")   
        
nombre_mystere()
# if "___name__" == "__main__":