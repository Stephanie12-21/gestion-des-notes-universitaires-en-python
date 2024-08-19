from db import get_db_connection

def load_prof(grade=None, search_text=None):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        query = """
        SELECT idProf AS Identifiant, nomProf, contactProf, emailProf, gradeProf
        FROM ProfTable
        """
        filters = []
        params = []

        if grade and grade != "Choisir le grade":
            filters.append("gradeProf = ?")
            params.append(grade)

        if search_text:
            filters.append("(nomProf LIKE ? OR contactProf LIKE ? OR emailProf LIKE ?)")
            search_param = f"%{search_text}%"
            params.extend([search_param, search_param, search_param])

        if filters:
            query += " WHERE " + " AND ".join(filters)

        cursor.execute(query, params)
        result = cursor.fetchall()
        conn.close()

        data = [(row[0], row[1], row[2], row[3], row[4]) for row in result]
        headers = ["Identifiant", "Nom", "Contact", "Email", "Grade"]

        return (headers, data)

    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
        return None
