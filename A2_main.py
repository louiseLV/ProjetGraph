from A2_fichier import lire_contraintes, afficher_graphe, creation_graphe, afficherGraphSousLaFormeDeTriplet
from A2_verifications import detecter_circuit, arcs_negatifs, calculer_rangs_graphe, calculer_calendriers, calculer_sommets_critiques, calculer_chemins_critiques


def main():
    menue = True
    
    while menue:
        # Choix du tableau de contraintes à traiter
        print("Choix du tableau de contraintes à traiter :")
        print("1-14")
        fichier = input("Entrez le numéro du tableau de contraintes à traiter : ")
        fichier = "Fichiers/table "+fichier+".txt"

        # Lecture du tableau de contraintes sur fichier et stockage en mémoire
        contraintes = lire_contraintes(fichier)
        
        # Création de la matrice correspondant au graphe représentant ce tableau de contraintes et affichage
        graphe = creation_graphe(contraintes)

        afficherGraphSousLaFormeDeTriplet(graphe)
        afficher_graphe(graphe)
    
        #Vérification des propriétés nécessaires pour que ce graphe soit un graphe d'ordonnancement
        if not detecter_circuit(graphe):
            menue = input("Voulez-vous continuer avec un autre tableau de contraintes ? (oui/non) ") == "oui"
            continue
        print("")
        if not arcs_negatifs(graphe):
            print("Il y a un arc négatif dans le graphe.")
            menue = input("Voulez-vous continuer avec un autre tableau de contraintes ? (oui/non) ") == "oui"
            continue
 
        print("")
        print("-> c'est un graphe d'ordonnancement")
        print("")
        # Calcul des rangs des sommets et affichage
        rangs = calculer_rangs_graphe(graphe)
        print("")
        # Calcul des calendriers au plus tôt et au plus tard et affichage
        calendrier_plus_tot, calendrier_plus_tard, marges = calculer_calendriers(graphe,contraintes, rangs)
        print("Calendriers au plus tôt :", calendrier_plus_tot)
        print("")
        print("Calendriers au plus tard :", calendrier_plus_tard)
        print("")
        print("Marges :", marges)

        print("")
        
        # Calcul des chemins critiques et affichage
        sommets_critiques = calculer_sommets_critiques(graphe, marges)
        print("Chemins critiques :", calculer_chemins_critiques(graphe, marges))
        print("")
        print("Sommets des chemins critiques :", sommets_critiques)
        print("")
        menue = input("Voulez-vous continuer avec un autre tableau de contraintes ? (oui/non) ") == "oui"

if __name__ == "__main__":
    main()
