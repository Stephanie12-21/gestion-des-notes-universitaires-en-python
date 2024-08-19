import pyodbc

# Remplacez ces valeurs par les informations de votre base de données
server = r'ROSEBUD\ESTF2024'
database = 'GestionDesNotesUniversitaires'
connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'

def delete_student(id_etd):
    try:
        # Établir la connexion à la base de données
        
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()

        # Exécuter la commande de suppression
        delete_query = "DELETE FROM EtudiantTable WHERE idEtudiant= ?"
        cursor.execute(delete_query, (id_etd,))
        conn.commit()

        print(f"L'étudiant avec l'ID {id_etd} a été supprimé avec succès.")
    except pyodbc.Error as e:
        print(f"Erreur lors de la suppression de l'étudiant: {e}")
    finally:
        cursor.close()
        conn.close()


