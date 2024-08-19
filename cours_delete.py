import pyodbc

# Remplacez ces valeurs par les informations de votre base de données
server = r'ROSEBUD\ESTF2024'
database = 'GestionDesNotesUniversitaires'
connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'

def delete_cours(id_cours):
    try:
        # Établir la connexion à la base de données
        
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()

        # Exécuter la commande de suppression
        delete_query = "DELETE FROM CoursTable WHERE idCours= ?"
        cursor.execute(delete_query, (id_cours,))
        conn.commit()

        print(f"Les données liées à l'ID {id_cours} ont été supprimées avec succès.")
    except pyodbc.Error as e:
        print(f"Erreur lors de la suppression de l'étudiant: {e}")
    finally:
        cursor.close()
        conn.close()


