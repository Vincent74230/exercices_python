import random
import math

rejoue = True # Booléen pour la boucle principale du jeu
capital = 1000 # capital de depart


print ("\n")
print ("€€€€€€€   Bienvenue au casino!   €€€€€€€\n")
print ("Vous êtes ici pour jouer à la roulette.\n")
print ("Vous avez au départ 1000 € en poche, eh oui vous etes riche")
print ("Les règles sont les suivantes : Choisissez votre numéro entre 0 et 49")
print ("Puis misez dessus la somme que vous voulez, \nsi le numéro gagnant est celui que vous aurez choisi: vous triplez votre mise.")
print ("Si le numéro gagnant est de la meme couleur (pair ou impair) que le votre, vous récupérez la moitié de votre mise\n")
print ("Sinon vous perdez votre mise, Bonne chance")



# fonction de sécurité de saisie du numéro choisi par l'utilisateur, l'utilisateur
# ne peux pas taper autre chose qu'un chiffre, dans l'intervalle 0-->49
def number():
    while True :
        user_number = input()
        try:
            user_number = int(user_number)
                    
        except ValueError:
            print("Veuillez entrer un chiffre pour votre numéro puis tapez entree")
            continue
        if user_number<0 or user_number>49:
            print ("Veuillez entrer en chiffre entre 0 et 49.")
        else:
            break
    return user_number

#test des != possibilites
while (rejoue):
    rand_number = random.randint(0,49)
    print ("Choisissez quel numero jouer (entre 0 et 49):")
    user_number = number()
    print ("Combien misez vous sur le",user_number,"?")
    print ("Vous disposez de",capital,"€")

    while True : #boucle de securite de saisie de la mise
        mise = input()
        try:
            mise = int(mise)     
        except ValueError:
            print("Veuillez entrer un nombre pour votre mise")
            continue
        if mise < 0:
            print ("Vous devez miser au minimum 1€ pour pouvoir jouer")
        elif mise > capital:
            print("Ne misez pas plus que ce que vous avez en banque..")
        else:
            break

    if user_number == rand_number: #si user gagne == 3 fois sa mise :)
        print ("Gagné! Vous remportez 3 fois votre mise!\n")
        capital += 3*mise
        

    elif user_number != rand_number and user_number%2 == rand_number%2: # si meme couleur
        print ("Vous remportez la moitie de votre mise\n")
        mise = math.ceil(mise/2)
        capital += mise

    else:#si rien du tout
        print ("Vous perdez votre mise..\n")
        capital -= mise


    if capital > 0: #si le capital arrive à 0: fin de la partie

        print ("Continuer à jouer? Vous disposez de",capital,"\n""€ Si oui tapez 1 sinon tapez 0 puis entree:")
        i = int(input())
        if i == 0:
            rejoue = False
    else:
        rejoue = False



if capital > 0:
    print("Vous décidez de vous retirer avec",capital,"€, trés bonne décision")
else:
    print("Perdu ! Le meilleur moyen de gagner est de ne pas jouer!")

