from db import get_db_connection

def load_etudiants(niveau=None, mention=None, search_term=None):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        query = """
        SELECT idEtudiant AS Identifiant, nomEtudiant, dateNaisEtudiant, contactEtudiant, emailEtudiant, adresseEtudiant, mention, niveau 
        FROM EtudiantTable
        """
        filters = []
        params = []

        if niveau and niveau != "Choisir le niveau":
            filters.append("niveau = ?")
            params.append(niveau)

        if mention and mention != "Choisir la mention":
            filters.append("mention = ?")
            params.append(mention)

        if search_term:
            filters.append("(nomEtudiant LIKE ? OR contactEtudiant LIKE ? OR emailEtudiant LIKE ? OR adresseEtudiant LIKE ?)")
            search_pattern = f"%{search_term}%"
            params.extend([search_pattern] * 4)

        if filters:
            query += " WHERE " + " AND ".join(filters)

        cursor.execute(query, params)
        result = cursor.fetchall()
        conn.close()

        data = [(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]) for row in result]
        headers = ["Identifiant", "Nom", "Naissance", "Contact", "Email", "Adresse", "Mention", "Niveau"]

        return (headers, data)

    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
        return None
