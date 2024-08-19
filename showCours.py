from db import get_db_connection

def load_cours(semestre=None, credit=None, search_text=None):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        query = """
        SELECT c.idCours AS Identifiant, c.ueCours, c.ecCours, p.nomProf, c.semestre, c.credit, c.niveau, c.mention
        FROM CoursTable c
        JOIN ProfTable p ON c.idProf = p.idProf
        """
        conditions = []
        params = []

        if semestre and semestre != "Choisir le semestre":
            conditions.append("c.semestre = ?")
            params.append(semestre)

        if credit and credit != "Choisir le crédit":
            conditions.append("c.credit = ?")
            params.append(credit)

        if search_text:
            search_pattern = f"%{search_text}%"
            conditions.append("(c.ueCours LIKE ? OR c.ecCours LIKE ? OR p.nomProf LIKE ? OR c.niveau LIKE ? OR c.mention LIKE ?)")
            params.extend([search_pattern] * 5)

        if conditions:
            query += " WHERE " + " AND ".join(conditions)

        cursor.execute(query, params)
        result = cursor.fetchall()
        conn.close()

        # Créer une liste de tuples pour les données et les en-têtes
        data = [(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]) for row in result]
        headers = ["Identifiant", "UE", "EC", "Prof", "Semestre", "Crédit", "Niveau", "Mention"]

        return (headers, data)

    except Exception as e:
        print(f"Une erreur s'est produite : {e}")  # Afficher l'erreur dans la console
        return None
