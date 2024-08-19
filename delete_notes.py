import pyodbc

# Remplacez ces valeurs par les informations de votre base de données
server = r'ROSEBUD\ESTF2024'
database = 'GestionDesNotesUniversitaires'
connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'

def delete_notes(id_notes):
    try:
        # Établir la connexion à la base de données
        
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()

        # Exécuter la commande de suppression
        delete_query = "DELETE FROM Table_Notes  WHERE idNotes= ?"
        cursor.execute(delete_query, (id_notes,))
        conn.commit()

        print(f"Les données avec l'ID {id_notes} ont été supprimées avec succès.")
    except pyodbc.Error as e:
        print(f"Erreur lors de la suppression des données: {e}")
    finally:
        cursor.close()
        conn.close()


