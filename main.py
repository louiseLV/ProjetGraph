from fichier import lire_contraintes, afficher_graphe, creation_graphe
from verifications import detecter_circuit, arcs_negatifs, calculer_rangs_graphe, calculer_calendriers, calculer_chemins_critiques


def main():
    menue = True
    
    while menue:
        # Choix du tableau de contraintes à traiter
        fichier = "/Users/louiselavergne/Documents/ProjetGraph1/contraintes.txt"
        
        # Lecture du tableau de contraintes sur fichier et stockage en mémoire
        contraintes = lire_contraintes(fichier)
        
        # Création de la matrice correspondant au graphe représentant ce tableau de contraintes et affichage
        graphe = creation_graphe(contraintes)
        afficher_graphe(contraintes)
        
        # Vérification des propriétés nécessaires pour que ce graphe soit un graphe d'ordonnancement
        if not detecter_circuit(graphe):
            print("Il y a un circuit dans le graphe.")
            menue = input("Voulez-vous continuer avec un autre tableau de contraintes ? (oui/non) ") == "oui"
            continue
        if not arcs_negatifs(graphe):
            print("Il y a un arc négatif dans le graphe.")
            menue = input("Voulez-vous continuer avec un autre tableau de contraintes ? (oui/non) ") == "oui"
            continue
        
        # Calcul des rangs des sommets et affichage
        rangs = calculer_rangs_graphe(graphe)
        print("Rangs des sommets :", rangs)
        
        # Calcul des calendriers au plus tôt et au plus tard et affichage
        calendrier_plus_tot, calendrier_plus_tard, marges = calculer_calendriers(graphe, rangs)
        print("Calendriers au plus tôt :", calendrier_plus_tot)
        print("Calendriers au plus tard :", calendrier_plus_tard)
        print("Marges :", marges)
        
        # Calcul des chemins critiques et affichage
        chemins_critiques = calculer_chemins_critiques(graphe, calendrier_plus_tot, calendrier_plus_tard)
        print("Chemins critiques :", chemins_critiques)
        
        menue = input("Voulez-vous continuer avec un autre tableau de contraintes ? (oui/non) ") == "oui"

if __name__ == "__main__":
    main()
