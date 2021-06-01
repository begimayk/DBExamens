#!/usr/bin/python3

from utils import db


#def select_tous_les_bateaux(conn):
    #"""
    #Affiche la liste de tous les bateaux.

    #:param conn: Connexion à la base de données
    #"""
    #cur = conn.cursor()
    #cur.execute("SELECT * FROM Bateaux")

    #rows = cur.fetchall()

    #for row in rows:
        #print(row)

def select_cours_6_credits(conn):
    cur = conn.cursor()
    cur.execute("SELECT matiere "
                "FROM Cours "
                "WHERE credits=6")

    rows = cur.fetchall()
    for row in rows:
        print(row)

def select_cours_3_credits(conn):
    cur = conn.cursor()
    cur.execute("SELECT matiere "
                "FROM Cours "
                "WHERE credits=3")

    rows = cur.fetchall()
    for row in rows:
        print(row)

def select_tous_les_cours(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM Cours")

    rows = cur.fetchall()

    for row in rows:
        print(row)

def etudiants_parcours_inf(conn):
    cur = conn.cursor()
    cur.execute("SELECT nom,prenom "
                "FROM Etudiants JOIN Promotions USING (promo)"
                "WHERE parcours='INF'")

    rows = cur.fetchall()

    for row in rows:
        print(row)

def etudiants_parcours_ges(conn):
    cur = conn.cursor()
    cur.execute("SELECT nom,prenom "
                "FROM Etudiants JOIN Promotions USING (promo)"
                "WHERE parcours='INF+ges'")

    rows = cur.fetchall()

    for row in rows:
        print(row)

def tous_les_etudiants(conn):
        cur = conn.cursor()
        cur.execute("SELECT numero, nom,prenom "
                    "FROM Etudiants ")

        rows = cur.fetchall()

        for row in rows:
            print(row)

def info_promo(conn, promotion):
    cur = conn.cursor()
    cur.execute("SELECT COUNT(numero) AS nb_etu, parcours "
                "FROM Etudiants JOIN Promotions USING (promo) "
                "WHERE promo=?"
                "GROUP BY promo", [promotion])

    rows = cur.fetchall()

    for row in rows:
        print(row)

def planning_examens(conn, p):
    cur = conn.cursor()
    cur.execute("""SELECT date_exam,nom,prenom
                   FROM Professeurs JOIN Examens USING (matiere)
                   WHERE promo=?""", [p])
    rows = cur.fetchall()

    for row in rows:
        print(row)

def info_cours(conn,cours):
    cur = conn.cursor()
    cur.execute("""SELECT nom, prenom, credits, date_exam
                    FROM Professeurs JOIN Cours USING (matiere)
                                     JOIN Examens USING (matiere)
                    WHERE matiere=?""", [cours])
    rows = cur.fetchall()

    for row in rows:
        print(row)

def main():
    # Nom de la BD à créer
    db_file = "data/Projet.db"

    # Créer une connexion a la BD
    conn = db.creer_connexion(db_file)

    # Remplir la BD
    print("1. On crée la bd et on l'initialise avec des premières valeurs.")
    db.mise_a_jour_bd(conn, "data/Projet_creation.sql")
    db.mise_a_jour_bd(conn, "data/Projet_Insert_ok.sql")

    while True:
        print("""Les cours:
              Tapez 1 pour afficher les matieres qui valent 6 credits
              Tapez 2 pour afficher les  matieres qui valent 3 credits
              Tapez q pour quitter""")

        c = input("Votre choix : ")

        if c=="1":
            select_cours_6_credits(conn)
        elif c=="2":
            select_cours_3_credits(conn)
        elif c=="q":
            break;

        print("""Liste des etudiants:
                Tapez 1 pour voir noms et prenoms des etudiants qui suivent le parcours INF
                Tapez 2 pour voir noms et prenoms des etudiants qui suivent le parcours INF+ges
                Tapez 3 pour voir la liste complete des etudiants (avec le numero d'tudiant)
                Tapez q pour quitter""")
        c2 = input("Votre choix : ")

        if c2=="1":
            etudiants_parcours_inf(conn)
        elif c2=="2":
            etudiants_parcours_ges(conn)
        elif c2=="3":
            tous_les_etudiants(conn)
        elif c2 =="q":
            break;

        print("Voulez vous consulter des information d'une promotion en particulier?")
        c3 = input("Repondez oui ou non : ")

        if c3 =="oui" or c3 == "OUI":
            c4 = input("Choisissez la promotion que vous aimerez consulter : ")
            print("Nombre d'etudiants et le parcours de la promotion ", c4)
            info_promo(conn, c4)
        elif c3=="non" or c3 == "NON":
            break;

        print("Voulez vous consulter le planning des examens?")
        c4 = input("Repondez oui ou non : ")
        if c4 == "oui" or c3 == "OUI":
            c5=input("Choisissez la promo dont la date et le professeur qui surveille l'examen vous aimerez voir : ")
            planning_examens(conn, c5)
        elif c4=="non" or c4 == "NON":
            break;

        print("Voulez vous consulter des information d'une matiere particuliere?")
        c6=input("Repondez oui ou non : ")
        if c6 == "oui" or c6 == "OUI":
            c7=input("Entrez la metiere dont vous aimerez avoir des information : ")
            print("Le professeur de", c7, "Le nombre de credits et les dates de l'examen pour ", c7)
            info_cours(conn,c7)
        elif c6=="non" or c6=="NON":
            break;

        c7 = input("Appuyez sur n'importe quelle touche pour revenir a la page Les cours,"
                   "Sinon, appuyez q pour quitter : ")
        if c7=="q" or "Q":
            break;


    # Lire la BD
    #print("2. Liste de tous les bateaux")
    #select_tous_les_bateaux(conn)


if __name__ == "__main__":
    main()
