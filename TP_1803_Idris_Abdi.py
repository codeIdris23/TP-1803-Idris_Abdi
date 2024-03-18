# -*- coding: 1252 -*-
def lire_csv(nom_fichier):
    donnees = []
    with open(nom_fichier, 'r') as fichier:
        lignes = fichier.readlines()
        for ligne in lignes:
            donnee = ligne.strip().split(',')
            donnees.append(donnee)
    return donnees

def ecrire_csv(nom_fichier, donnees):
    with open(nom_fichier, 'w') as fichier:
        for donnee in donnees:
            ligne = ','.join(map(str, donnee)) + '\n'
            fichier.write(ligne)

def moyenne_precipitations_ville(donnees):
    total_precipitations = 0
    nombre_jours = 0
    
    for jour in donnees:
        if jour[1] == 'Ville':
            total_precipitations += jour[4]
            nombre_jours += 1
    
    moyenne = total_precipitations / nombre_jours if nombre_jours else 0
    print(f"Moyenne des précipitations à Ville : {moyenne} mm")

def filtrer_ville(donnees):
    ville = input("Entrez le nom de la ville à filtrer : ")
    for enregistrement in donnees:
        if enregistrement[1] == ville:
            print(enregistrement)

def filtrer_periode(donnees):
    date_debut = input("Entrez la date de début (YYYY-MM-DD) : ")
    date_fin = input("Entrez la date de fin (YYYY-MM-DD) : ")
    for enregistrement in donnees:
        if date_debut <= enregistrement[0] <= date_fin:
            print(enregistrement)

def temperature_extremes_ville(donnees):
    ville = input("Entrez le nom de la ville : ")
    temperatures = [int(jour[2]) for jour in donnees if jour[1] == ville] + [int(jour[3]) for jour in donnees if jour[1] == ville]
    print(f"Température maximale à {ville} : {max(temperatures)}°C")
    print(f"Température minimale à {ville} : {min(temperatures)}°C")

def temperature_moyenne_ville(donnees):
    ville = input("Entrez le nom de la ville : ")
    temperatures = [int(jour[2]) for jour in donnees if jour[1] == ville] + [int(jour[3]) for jour in donnees if jour[1] == ville]
    moyenne = sum(temperatures) / len(temperatures) if temperatures else 0
    print(f"Température moyenne à {ville} : {moyenne}°C")

def afficher_menu():
    print("\nMenu du programme:")
    print("1. Filtrer les données météo d'une ville")
    print("2. Filtrer les données météo d'une ville pendant une période")
    print("3. Déterminer les températures maximale et minimale d'une ville")
    print("4. Déterminer la température moyenne d'une ville")
    print("5. Déterminer la moyenne des précipitations d'une ville")
    print("6. Quitter")

def main():
    donnees_meteo = [
        ['2024-01-01', 'Toulouse', 5, 9, 15],
        ['2024-01-02', 'Toulouse', 19, 5, 14],
        ['2024-01-03', 'Toulouse', 7, -5, 13],
        ['2024-01-04', 'Toulouse', 22, 5, 15],
        ['2024-01-05', 'Toulouse', 2, 2, 20],
        ['2024-01-06', 'Toulouse', -1, -2, 20],
        ['2024-01-07', 'Toulouse', 5, 6, 15],
        ['2024-01-08', 'Toulouse', 4, -4, 9],
        ['2024-01-09', 'Toulouse', 5, 5, 3],
        ['2024-01-10', 'Toulouse', 31, 30, 17],
        ['2024-01-01', 'Nice', 32, 5, 8],
        ['2024-01-02', 'Nice', 0, -2, 20],
        ['2024-01-03', 'Nice', 22, 4, 1],
        ['2024-01-04', 'Nice', 26, -10, 8],
        ['2024-01-05', 'Nice', 16, 7, 6],
        ['2024-01-06', 'Nice', 11, 2, 11],
        ['2024-01-07', 'Nice', 10, 23, 20],
        ['2024-01-08', 'Nice', 3, 7, 8],
        ['2024-01-09', 'Nice', 34, 24, 17],
        ['2024-01-10', 'Nice', -3, 25, 11],
        ['2024-01-01', 'Bordeaux', 5, 9, 15],
        ['2024-01-02', 'Bordeaux', 19, 5, 14],
        ['2024-01-03', 'Bordeaux', 7, -5, 13],
        ['2024-01-04', 'Bordeaux', 22, 5, 15],
        ['2024-01-05', 'Bordeaux', 2, 2, 20],
        ['2024-01-06', 'Bordeaux', -1, -2, 20],
        ['2024-01-07', 'Bordeaux', 5, 6, 15],
        ['2024-01-08', 'Bordeaux', 4, -4, 9],
        ['2024-01-09', 'Bordeaux', 5, 5, 3],
        ['2024-01-10', 'Bordeaux', 31, 30, 17],
        ['2024-01-01', 'Marseille', 32, 5, 8],
        ['2024-01-02', 'Marseille', 0, -2, 20],
        ['2024-01-03', 'Marseille', 22, 4, 1],
        ['2024-01-04', 'Marseille', 26, -10, 8],
        ['2024-01-05', 'Marseille', 16, 7, 6],
        ['2024-01-06', 'Marseille', 11, 2, 11],
        ['2024-01-07', 'Marseille', 10, 23, 20],
        ['2024-01-08', 'Marseille', 3, 7, 8],
        ['2024-01-09', 'Marseille', 34, 24, 17],
        ['2024-01-10', 'Marseille', -3, 25, 11]
    ]
    
    while True:
        afficher_menu()
        choix = input("Entrez votre choix (1-6) : ")
        
        if choix == '1':
            filtrer_ville(donnees_meteo)
        elif choix == '2':
            filtrer_periode(donnees_meteo)
        elif choix == '3':
            temperature_extremes_ville(donnees_meteo)
        elif choix == '4':
            temperature_moyenne_ville(donnees_meteo)
        elif choix == '5':
            moyenne_precipitations_ville(donnees_meteo)
        elif choix == '6':
            print("Fin du programme.")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()