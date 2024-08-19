import pyodbc

def get_db_connection():
    server = r'ROSEBUD\ESTF2024'
    database = 'GestionDesNotesUniversitaires'
    connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
    conn = pyodbc.connect(connection_string)
    return conn



def get_student_by_id(idEtd):
    conn = get_db_connection()
    cursor = conn.cursor()

    # Préparez votre requête SQL pour sélectionner les données de l'étudiant par son ID
    query = "SELECT nomEtudiant, dateNaisEtudiant, contactEtudiant, emailEtudiant, adresseEtudiant, mention, niveau FROM EtudiantTable WHERE idEtudiant = ?"

    try:
        # Exécutez la requête SQL avec l'ID passé en paramètre
        cursor.execute(query, (idEtd,))  # Passer idEtd comme tuple (idEtd,)
        row = cursor.fetchone()

        if row:
            # Créez un dictionnaire pour stocker les données de l'étudiant
            student_data = {
                'nom': row.nomEtudiant,
                'date_naissance': row. dateNaisEtudiant,
                'contact': row.contactEtudiant,
                'email': row.emailEtudiant,
                'adresse': row. adresseEtudiant,
                'mention': row.mention,
                'niveau': row.niveau
            }
            return student_data
        else:
            return None  # Retourne None si aucun étudiant n'est trouvé avec cet ID

    except Exception as e:
        print(f"Erreur lors de la récupération des données de l'étudiant: {str(e)}")
        return None

    finally:
        cursor.close()
        conn.close()



def get_prof_by_id(idProf):
    conn = get_db_connection()
    cursor = conn.cursor()

    # Préparez votre requête SQL pour sélectionner les données de l'étudiant par son ID
    query = "SELECT nomProf, contactProf, emailProf, adresseProf, gradeProf FROM ProfTable WHERE idProf = ?"

    try:
        # Exécutez la requête SQL avec l'ID passé en paramètre
        cursor.execute(query, (idProf,))  # Passer idEtd comme tuple (idEtd,)
        row = cursor.fetchone()

        if row:
            # Créez un dictionnaire pour stocker les données de l'étudiant
            prof_data = {
                'nom': row.nomProf,
                'contact': row.contactProf,
                'email': row.emailProf,
                'adresse': row. adresseProf,
                'grade': row.gradeProf
            }
            return prof_data
        else:
            return None  # Retourne None si aucun étudiant n'est trouvé avec cet ID

    except Exception as e:
        print(f"Erreur lors de la récupération des données de l'étudiant: {str(e)}")
        return None

    finally:
        cursor.close()
        conn.close()


def get_cours_by_id(idCours):
    conn = get_db_connection()
    cursor = conn.cursor()

    # Préparez votre requête SQL pour sélectionner les données de l'étudiant par son ID
    query = "SELECT ueCours, ecCours, idProf, semestre, credit, niveau, mention FROM CoursTable WHERE idCours = ?"

    try:
        # Exécutez la requête SQL avec l'ID passé en paramètre
        cursor.execute(query, (idCours,))  # Passer idEtd comme tuple (idEtd,)
        row = cursor.fetchone()

        if row:
            # Créez un dictionnaire pour stocker les données de l'étudiant
            cours_data = {
                'ue': row.ueCours,
                'ec': row.ecCours,
                'prof': row.idProf,
                'semestre': row. semestre,
                'niveau': row.niveau,
                'mention' : row.mention
            }
            return cours_data
        else:
            return None  # Retourne None si aucun étudiant n'est trouvé avec cet ID

    except Exception as e:
        print(f"Erreur lors de la récupération des données de l'étudiant: {str(e)}")
        return None

    finally:
        cursor.close()
        conn.close()

def get_notes_by_id(idNotes):
    conn = get_db_connection()
    cursor = conn.cursor()

    # Préparez votre requête SQL pour sélectionner les données des notes par son ID
    query = "SELECT idCours, idEtudiant, semestre, dateExamen, session FROM NotesTable WHERE idNotes = ?"

    try:
        # Exécutez la requête SQL avec l'ID passé en paramètre
        cursor.execute(query, (idNotes,))  # Passer idEtd comme tuple (idEtd,)
        row = cursor.fetchone()

        if row:
            # Créez un dictionnaire pour stocker les données de l'étudiant
            notes_data = {
                'etudiant': row.idEtudiant,
                'ec': row.idCours,
                'dateExam': row. dateExamen,
                'semestre': row.semestre,
                'session' : row.session
            }
            return notes_data
        else:
            return None  # Retourne None si aucun étudiant n'est trouvé avec cet ID

    except Exception as e:
        print(f"Erreur lors de la récupération des données de la notes: {str(e)}")
        return None

    finally:
        cursor.close()
        conn.close()



