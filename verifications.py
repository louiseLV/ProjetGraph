from fichier import lire_contraintes, creation_graphe, afficher_graphe
    # Vérification arcs négatifs

# def detecter_circuit(graphe):
#     graphe_copie = [ligne[:] for ligne in graphe]
    
#     entrees = [True] * len(graphe_copie)
#     for ligne in graphe_copie:
#         for tache in range(len(ligne)):
#             if ligne[tache] != 0:
#                 entrees[tache] = False
#     points_entree = [i for i, val in enumerate(entrees) if val]
    
#     while points_entree:
#         point = points_entree.pop()
#         suivants = [i for i, val in enumerate(graphe_copie[point]) if val != 0]
#         for suivant in suivants:
#             graphe_copie[point][suivant] = 0
#             if all(graphe_copie[i][suivant] == 0 for i in range(len(graphe_copie))):
#                 points_entree.append(suivant)
    
#     return not any(any(ligne) for ligne in graphe_copie)
def detecter_circuit(graphe):
    print("Détection de circuit (Méthode de suppression des points d'entrée) :")
    
    # Création d'une copie du graphe
    graphe_copie = [[val for val in ligne] for ligne in graphe]
    
    # Recherche des points d'entrée
    points_entree = [True] * len(graphe_copie)
    for ligne in graphe_copie:
        for tache in range(len(ligne)):
            if ligne[tache] != -999:
                points_entree[tache] = False
    
    print("* Points d'entrée :", [i for i, est_entree in enumerate(points_entree) if est_entree])
    
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
        
        # Mise à jour des sommets restants
        sommets_restants = [i for i in range(len(graphe_copie)) if any(graphe_copie[i][j] != -999 for j in range(len(graphe_copie[i])))]
        print("* Suppression des points d'entrée")
        print("Sommets restants :", sommets_restants)
        print("* Points d'entrée :", [i for i in range(len(graphe_copie)) if all(graphe_copie[j][i] == -999 for j in range(len(graphe_copie)))])
    
    # Vérification s'il reste des arcs dans le graphe
    pas_de_circuit = not any(val != -999 for ligne in graphe_copie for val in ligne)
    if pas_de_circuit:
        print("-> Il n'y a pas de circuit")
    else:
        print("-> Il y a un circuit")
    
    print("Il n'y a pas d'arcs négatifs")
    print("-> C'est un graphe d'ordonnancement")
    
    return pas_de_circuit



def arcs_negatifs(graphe):
        for ligne in graphe:
            for val in ligne:
                if val < 0 and val != -999:
                    return False
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
    return rangs


def calculer_calendriers(graphe,contraintes, rangs):
    nombre_taches = len(graphe)
    calendrier_plus_tot = [0] * nombre_taches
    calendrier_plus_tard = [0] * nombre_taches
    marges = [0] * nombre_taches
    durees= []
    #truc moche mais à refaire mieux
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
            if graphe[voisin][sommet] != 0:
                max_calendrier_precedent = max(max_calendrier_precedent, calendrier_plus_tot[voisin] + durees[voisin])  
        calendrier_plus_tot[sommet] = max_calendrier_precedent
    # Initialisation du calendrier au plus tard avec le calendrier au plus tôt du dernier sommet
    calendrier_plus_tard[-1] = calendrier_plus_tot[-1]

    #Ca calcule le bon resultat 
    
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

#pour faire les tests (ça sert pas à grand chose)
# contraintes = lire_contraintes("contraintes.txt")
# graphe = creation_graphe(contraintes)
# rangs = calculer_rangs_graphe(graphe)
# calendrier_plus_tot, calendrier_plus_tard, marges = calculer_calendriers(graphe, contraintes, rangs)

def calculer_chemins_critiques(graphe, marges):
    chemins_critiques = []
    for sommet in range(len(graphe)):
        for voisin in range(len(graphe)):
            if graphe[sommet][voisin] != -999:
                if marges[sommet]==0 :
                    chemins_critiques.append((sommet, voisin))
    return chemins_critiques



