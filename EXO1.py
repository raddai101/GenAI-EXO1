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
            print("choississez une option : 1. Continuer à jouer 2. Quitter le jeu 3. Afficher le score 4.Modifier  intervalle")
            options = int(input("Entrez votre choix : "))
            
            if options == 1:
                continue
            elif options == 2:
                print("Merci d'avoir joué ! À bientôt.")
                break
            elif options == 3:
                print(f"Votre score est de {score}.")
                continue
            elif options == 4:
                print("Veuillez entrer un intervalle de 1 a 100")
                intervalle = int(input("Entrez votre choix : "))
                if intervalle < 1 or intervalle > 100:
                    print("Veuillez entrer un intervalle valide entre 1 et 100.")
                    continue    

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