from db import get_db_connection

def count_students_by_level(level):
    conn = get_db_connection()
    cursor = conn.cursor()

    query = "SELECT COUNT(*) FROM EtudiantTable WHERE niveau = ?"

    try:
        cursor.execute(query, (level,))
        row = cursor.fetchone()

        if row:
            count = row[0]
            return count
        else:
            return 0  # Retourne 0 si aucun étudiant n'est trouvé avec ce niveau

    except Exception as e:
        print(f"Erreur lors du comptage des étudiants par niveau : {str(e)}")
        return 0

    finally:
        cursor.close()
        conn.close()



