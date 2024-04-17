def lire_contraintes(fichier):
    contraintes = []
    with open(fichier, 'r') as file:
        for line in file:
            contraintes.append(list(map(int, line.strip().split())))
    return contraintes

def creation_graphe(contraintes):
    nombre_taches = len(contraintes)
    listePredecesseurs=[]
    graphe = [[0] * (nombre_taches+2) for _ in range(nombre_taches+2)]
    
    for contrainte in contraintes:
        tache = contrainte[0]
        predecesseurs = contrainte[2:]
        for element in predecesseurs:
            listePredecesseurs.append(element)
        if len(predecesseurs)==0 :
            graphe[0][tache]= 0
        for predecesseur in predecesseurs:
            graphe[predecesseur][tache] = predecesseur

    for contrainte in contraintes:
        tache=contrainte[0]
        if tache not in listePredecesseurs:
            graphe[tache][nombre_taches+1] = tache
    
    return graphe



def afficher_graphe(graphe):
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


def afficherGraphSousLaFormeDeTriplet(graphe):
    NombreDarc=0
    ListOfArcs=[]
    print("* Création du graphe d'ordonnancement :")
#Afficher le nombre de sommet 
    print("Nombre de sommet :", len(graphe))
#Afficher le nombre d'arc
    for i in range(len(graphe)):
        for j in range(len(graphe[0])):
            if graphe[i][j]!= 0:
                NombreDarc+=1
                newArc=str(i)+" -> "+str(j)+" = "+str(graphe[i][j])
                ListOfArcs.append(newArc)
    print("Nombre d'arc :",NombreDarc)
    for arc in ListOfArcs:
        print(arc)