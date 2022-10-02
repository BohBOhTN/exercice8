import random
random_Number= random.randint(0,100)
num_utilisateur = int(input('Donner un nombre'))
nb_essai = 0
print(random_Number)
if(num_utilisateur == random_Number):
    print('Bravo vous avez trouver la bonne repense')
    print(f'le programme a génerer la valeur {num_utilisateur}')
    print('')
else:
    while (num_utilisateur != random_Number and nb_essai <= 5):
        if(num_utilisateur > random_Number):
            print(f'La valeur entrer {num_utilisateur} est trop grand voulez vous ressaier')
            num_utilisateur = int(input('Donner un nombre'))
            nb_essai += 1
        else:
            print(f'La valeur entrer {num_utilisateur} est trop petit voulez vous ressaier')
            num_utilisateur = int(input('Donner un nombre'))
            nb_essai += 1
if(num_utilisateur == random_Number ):
    print(f'bravo !! vous avez trouver la bonne repense apres {nb_essai} essai ')
    print(f'le script a generer le nombre {random_Number}')
else:
    print(f'Désole vous avez depasser {nb_essai - 1} essai pour trouver la repense ')
    print(f'la bonne repense est {random_Number}')
