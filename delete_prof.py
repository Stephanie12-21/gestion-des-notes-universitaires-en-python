import pyodbc

# Remplacez ces valeurs par les informations de votre base de données
server = r'ROSEBUD\ESTF2024'
database = 'GestionDesNotesUniversitaires'
connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'

def delete_prof(id_prof):
    try:
        # Établir la connexion à la base de données
        
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()

        # Exécuter la commande de suppression
        delete_query = "DELETE FROM ProfTable WHERE idProf= ?"
        cursor.execute(delete_query, (id_prof,))
        conn.commit()

        print(f"L'enseignant avec l'ID {id_prof} a été supprimé avec succès.")
    except pyodbc.Error as e:
        print(f"Erreur lors de la suppression: {e}")
    finally:
        cursor.close()
        conn.close()


