from fichier import lire_contraintes

contraintes = lire_contraintes()

def verifier_contraintes(contraintes):
    nombre_taches = len(contraintes)
    graphe = [[0] * (nombre_taches + 2) for _ in range(nombre_taches + 2)]
    for contrainte in contraintes:
        tache = contrainte[0]
        duree = contrainte[1]
        predecesseurs = contrainte[2:]
        for predecesseur in predecesseurs:
            graphe[predecesseur][tache] = duree
    
    # Vérification des circuits
    def detecter_circuit(graphe):
        entrees = [True] * len(graphe)
        for ligne in graphe:
            for tache in range(len(ligne)):
                if ligne[tache] != 0:
                    entrees[tache] = False
        points_entree = [i for i, val in enumerate(entrees) if val]
        while points_entree:
            point = points_entree.pop()
            suivants = [i for i, val in enumerate(graphe[point]) if val != 0]
            for suivant in suivants:
                graphe[point][suivant] = 0
                if all(graphe[i][suivant] == 0 for i in range(len(graphe))):
                    points_entree.append(suivant)
        return not any(any(ligne) for ligne in graphe)

    if detecter_circuit(graphe)==False:
        print("Il y a un circuit dans le graphe.")
        
    
    # Vérification arcs négatifs
    def arcs_negatifs(graphe):
        for ligne in graphe:
            for val in ligne:
                if val < 0:
                    print("Il y a un arc négatif dans le graphe.")
                    return False
        return True
    
    if (detecter_circuit(graphe) and arcs_negatifs(graphe)):
        print("Les propriétés sont valides.")
        return 

verifier_contraintes(contraintes)

def calculer_rangs_graphe(graphe):
    def recherche_en_profondeur(sommet, rang):
        rangs[sommet] = rang
        for voisin in range(len(graphe)):
            if graphe[sommet][voisin] != 0:
                if rangs[voisin] < rang + 1:
                    recherche_en_profondeur(voisin, rang + 1)

    rangs = [0] * len(graphe)
    for sommet in range(len(graphe)):
        if not any(graphe[i][sommet] != 0 for i in range(len(graphe))):
            recherche_en_profondeur(sommet, 1)
    return rangs





