from fichier import lire_contraintes, creation_graphe, afficher_graphe
    # Vérification arcs négatifs
def detecter_circuit(graphe):
    graphe_copie = [ligne[:] for ligne in graphe]
    
    entrees = [True] * len(graphe_copie)
    for ligne in graphe_copie:
        for tache in range(len(ligne)):
            if ligne[tache] != 0:
                entrees[tache] = False
    points_entree = [i for i, val in enumerate(entrees) if val]
    
    while points_entree:
        point = points_entree.pop()
        suivants = [i for i, val in enumerate(graphe_copie[point]) if val != 0]
        for suivant in suivants:
            graphe_copie[point][suivant] = 0
            if all(graphe_copie[i][suivant] == 0 for i in range(len(graphe_copie))):
                points_entree.append(suivant)
    
    return not any(any(ligne) for ligne in graphe_copie)


def arcs_negatifs(graphe):
        for ligne in graphe:
            for val in ligne:
                if val < 0:
                    return False
        return True
    
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


def calculer_calendriers(graphe, rangs):
    durees = [max(ligne) for ligne in graphe]
    calendrier_plus_tot = [0] * len(graphe)
    calendrier_plus_tard = [rangs[i] for i in range(len(graphe))]
    marges = [0] * len(graphe)

    for sommet in range(len(graphe)):
        for voisin in range(len(graphe)):
            if graphe[sommet][voisin] != 0:
                if calendrier_plus_tot[voisin] < calendrier_plus_tot[sommet] + durees[sommet]:
                    calendrier_plus_tot[voisin] = calendrier_plus_tot[sommet] + durees[sommet]
    
    for sommet in reversed(range(len(graphe))):
        for voisin in range(len(graphe)):
            if graphe[sommet][voisin] != 0:
                if calendrier_plus_tard[sommet] > calendrier_plus_tard[voisin] - durees[sommet]:
                    calendrier_plus_tard[sommet] = calendrier_plus_tard[voisin] - durees[sommet]
    
    marges = [calendrier_plus_tard[i] - calendrier_plus_tot[i] for i in range(len(graphe))]
    return calendrier_plus_tot, calendrier_plus_tard, marges

def calculer_chemins_critiques(graphe, calendrier_plus_tot, calendrier_plus_tard, marges):
    chemins_critiques = []
    for sommet in range(len(graphe)):
        for voisin in range(len(graphe)):
            if graphe[sommet][voisin] != 0:
                if calendrier_plus_tard[sommet] == calendrier_plus_tot[sommet] or marges[sommet]==0 :
                    chemins_critiques.append((sommet, voisin))
    return chemins_critiques



