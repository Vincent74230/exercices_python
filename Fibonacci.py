i=0
s=0

liste = [1,1]

print("Bienvenue dans ce petit programme qui calcule la suite de Fibonacci\n")
print("Combien de nombres voulez-vous faire apparaitre à l'écran?")
print ("Veuillez entrer un nombre entier positif")

while True:
    max = input()
    try: 
        max = int(max)
    
    except ValueError :
        print("Veuillez taper un nombre compris entre 2 et 500")
        continue
    if max<2:
        print("Tapez un nombre supérieur à 2")
    elif max>500:
        print ("Tapez un nombre inférieur à 500")
    else:
        break

while i<max-2:
    s = liste[i]+liste[i+1]
    liste.append(s)
    i+=1


print(liste)