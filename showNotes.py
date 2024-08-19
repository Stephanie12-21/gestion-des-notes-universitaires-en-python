from db import get_db_connection
def load_notes(seuil=None, session=None):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        query = """
        SELECT n.idNotes AS Identifiant, e.nomEtudiant, n.session, c.ecCours, n.notes, n.dateExamen
        FROM Table_Notes n
        JOIN EtudiantTable e ON n.idEtudiant = e.idEtudiant
        JOIN CoursTable c ON n.idCours = c.idCours
        """
        conditions = []
        params = []

        if seuil and seuil != "Choisir le seuil":
            if seuil == "inférieur à 10":
                conditions.append("n.notes < 10")
            elif seuil == "égal à 10":
                conditions.append("n.notes = 10")
            elif seuil == "supérieur à 10":
                conditions.append("n.notes > 10")

        if session and session != "Choisir la session":
            conditions.append("session = ?")
            params.append(session)

        if conditions:
            query += " WHERE " + " AND ".join(conditions)

        cursor.execute(query, params)
        result = cursor.fetchall()
        conn.close()

        # Créer une liste de tuples pour les données et les en-têtes
        data = [(row[0], row[1], row[2], row[3], row[4], row[5]) for row in result]
        headers = ["Identifiant", "Étudiant", "Session", "Elément constitutif", "Notes reçues", "Date Examen"]

        return (headers, data)

    except Exception as e:
        print(f"Une erreur s'est produite : {e}")  # Afficher l'erreur dans la console
        return None
