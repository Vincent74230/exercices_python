import random

ok=1

while (ok==1):

	i=9

	rand_number = random.randint(0,100)

	print("***Bienvenue dans le jeu du nombre mystere***")
	print("Le nombre mystere se situe entre 1 et 100, saurez-vous le trouver?")
	print("Tapez un nombre entre 1 et 100, vous avez 10 essais:")

	nombre_utilistaure = int(input())


	while i != 0:


		if (nombre_utilistaure<rand_number):
			print("C'est plus ! Il vous reste",i,"essais")
		elif (nombre_utilistaure>rand_number):
			print("C'est moins ! Il vous reste",i,"essais")
		else:
			print("Bravo vous avez trouvé, le nombre mystere était",rand_number)
			break
		
		nombre_utilistaure = int(input())

		i -= 1

		


	if (i==0):
		print  ("Vous avez lamentablement échoué..")
	print("Voulez-vous faire une autre partie? Si oui tapez 1 sinon 0")
	ok = int(input())