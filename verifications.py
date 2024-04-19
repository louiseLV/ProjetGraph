from fichier import lire_contraintes, creation_graphe, afficher_graphe
def detecter_circuit(graphe):
    
    # Création d'une copie du graphe
    graphe_copie = [[val for val in ligne] for ligne in graphe]
    
    # Recherche des points d'entrée
    points_entree = [True] * len(graphe_copie)
    for ligne in graphe_copie:
        for tache in range(len(ligne)):
            if ligne[tache] != -999:
                points_entree[tache] = False
    
    
    # Liste pour stocker les sommets à traiter
    sommets_a_traiter = [i for i, est_entree in enumerate(points_entree) if est_entree]
    # Méthode d'élimination des points d'entrée
    while sommets_a_traiter:
        point = sommets_a_traiter.pop()
        suivants = [i for i, val in enumerate(graphe_copie[point]) if val != -999]
        for suivant in suivants:
            graphe_copie[point][suivant] = -999
            # Si le sommet suivant n'a plus de prédécesseur
            if all(graphe_copie[i][suivant] == -999 for i in range(len(graphe_copie))):
                sommets_a_traiter.append(suivant)
        
    # Vérification s'il reste des arcs dans le graphe
    pas_de_circuit = not any(val != -999 for ligne in graphe_copie for val in ligne)
    if pas_de_circuit:
        print("")
        print("-> Il n'y a pas de circuit")
    else:
        print("")
        print("-> Il y a un circuit")
    
    return pas_de_circuit



def arcs_negatifs(graphe):
        for ligne in graphe:
            for val in ligne:
                if val < 0 and val != -999:
                    return False
        print("-> Il n'y a pas d'arcs négatifs")
        return True

def calculer_rangs_graphe(graphe):
    def recherche_en_profondeur(sommet, rang):
        rangs[sommet] = rang
        for voisin in range(len(graphe)):
            if graphe[sommet][voisin] != -999:
                if rangs[voisin] < rang + 1:
                    recherche_en_profondeur(voisin, rang + 1)

    rangs = [0] * len(graphe)
    for sommet in range(len(graphe)):
        if not any(graphe[i][sommet] != -999 for i in range(len(graphe))):
            recherche_en_profondeur(sommet, 0)
        print("Rang du sommet", sommet, ":", rangs[sommet])

    
    return rangs


def calculer_calendriers(graphe,contraintes, rangs):
    nombre_taches = len(graphe)
    calendrier_plus_tot = [0] * nombre_taches
    calendrier_plus_tard = [0] * nombre_taches
    marges = [0] * nombre_taches
    durees= []
    durees.append(0)
    for contrainte in contraintes:
        durees.append(contrainte[1])
    for i in range(2):
        durees.append(0)
    
    
    sommets_tries = sorted(range(nombre_taches), key=lambda sommet: rangs[sommet])
    # Calcul des calendriers au plus tôt
    for sommet in sommets_tries:
        max_calendrier_precedent = 0
        for voisin in range(nombre_taches):
            if graphe[voisin][sommet] != -999:
                max_calendrier_precedent = max(max_calendrier_precedent, calendrier_plus_tot[voisin] + durees[voisin])  
        calendrier_plus_tot[sommet] = max_calendrier_precedent
    # Initialisation du calendrier au plus tard avec le calendrier au plus tôt du dernier sommet
    calendrier_plus_tard[-1] = calendrier_plus_tot[-1]
    
    # Calcul des calendriers au plus tard
   
    for sommet in reversed(sommets_tries):
        min_calendrier_suivant = calendrier_plus_tard[-1]
        for voisin in range(nombre_taches):
            if graphe[sommet][voisin] != -999:
                min_calendrier_suivant = min(min_calendrier_suivant, calendrier_plus_tard[voisin] - durees[sommet])
        calendrier_plus_tard[sommet] = min_calendrier_suivant
        calendrier_plus_tard[0]=0
    
    # Calcul des marges en soustrayant les calendriers au plus tard des calendriers au plus tôt
    marges = [calendrier_plus_tard[i] - calendrier_plus_tot[i] for i in range(nombre_taches)]

    return calendrier_plus_tot, calendrier_plus_tard, marges

def calculer_chemins_critiques(graphe, marges):
    chemins_critiques = []
    for sommet in range(len(graphe)):
        for voisin in range(len(graphe)):
            if graphe[sommet][voisin] != -999:
                if marges[sommet]==0 :
                    chemins_critiques.append((sommet, voisin))
    return chemins_critiques

def calculer_sommets_critiques(graphe, marges):
    sommets_critiques = set()
    for sommet_depart in range(len(graphe)):
        for sommet_arrivee in range(len(graphe)):
            if graphe[sommet_depart][sommet_arrivee] != -999:
                if marges[sommet_depart] == 0 and marges[sommet_arrivee] == 0:
                    sommets_critiques.add(sommet_depart)
                    sommets_critiques.add(sommet_arrivee)
    return list(sommets_critiques)

