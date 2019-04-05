print("Entrez un flottant:")

nb = input()

while True:
    try:
        nb = float(nb)
        break
    except:
        print("Veuillez entrer un nombre a virgule")
        continue


nb = str(nb)

entier,flottant = nb.split(".")

print(",".join([entier,flottant[:3]]))
print ("C'est plus joli..")

