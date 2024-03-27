def lire_contraintes(fichier='/Users/louiselavergne/Documents/ProjetGraph/contraintes.txt'):
    contraintes = []
    with open(fichier, 'r') as file:
        for line in file:
            contraintes.append(list(map(int, line.strip().split())))
    return contraintes

liste_contraintes = lire_contraintes()
print(liste_contraintes)

def afficher_graphe(liste_contraintes):
    nombre_taches = len(liste_contraintes)
    graphe = [[0] * (nombre_taches + 2) for _ in range(nombre_taches + 2)]
    for contrainte in liste_contraintes:
        tache = contrainte[0]
        duree = contrainte[1]
        predecesseurs = contrainte[2:]
        for predecesseur in predecesseurs:
            graphe[predecesseur][tache] = duree
    print("Matrice des valeurs :")
    print(" ", end="\t")
    for i in range(len(graphe[0])):
        print(i, end="\t")
    print()
    for i in range(len(graphe)):
        print(i, end="\t")
        for j in range(len(graphe[0])):
            if graphe[i][j] == 0:
                print("*", end="\t")
            else:
                print(graphe[i][j], end="\t")
        print()


