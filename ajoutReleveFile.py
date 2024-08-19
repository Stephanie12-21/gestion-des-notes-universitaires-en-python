from PySide6.QtWidgets import QDialog, QMessageBox
from PySide6.QtCore import Signal
from ajoutReleve import Ui_ReleveDialog  # Import de la classe générée
from db import get_db_connection

class ReleveDialog(QDialog):
    releve_ajoute = Signal(dict)  # Définir un signal pour indiquer l'ajout d'un relevé avec les détails

    def __init__(self, parent=None):
        super(ReleveDialog, self).__init__(parent)
        self.ui = Ui_ReleveDialog()
        self.ui.setupUi(self)

        # Connecter les combobox niveau et mention aux méthodes de filtrage
        self.ui.niveauComboBox.currentIndexChanged.connect(self.filter_data)
        self.ui.mentionComboBox.currentIndexChanged.connect(self.filter_data)

        # Connecter le bouton saveBtn à la méthode save_releve
        self.ui.saveBtn.clicked.connect(self.save_releve)
        
        # Charger initialement les étudiants et les UE
        self.load_etudiants()
        self.load_UE()

    def filter_data(self):
        # Filtrer les étudiants et les UE en fonction des sélections de niveau et mention
        self.load_etudiants()
        self.load_UE()

    def load_etudiants(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            niveau = self.ui.niveauComboBox.currentText()
            mention = self.ui.mentionComboBox.currentText()
            query = "SELECT idEtudiant, nomEtudiant FROM EtudiantTable WHERE niveau = ? AND mention = ?"
            cursor.execute(query, (niveau, mention))
            etudiants = cursor.fetchall()
            conn.close()

            # Ajouter une ligne d'invite
            self.ui.etudiantComboBox.clear()
            self.ui.etudiantComboBox.addItem("Choisir l'étudiant en question", None)

            # Ajouter les noms des étudiants
            for idEtudiant, nomEtudiant in etudiants:
                self.ui.etudiantComboBox.addItem(nomEtudiant, idEtudiant)

        except Exception as e:
            print(f"Une erreur s'est produite lors du chargement des étudiants : {e}")
            QMessageBox.critical(self, "Erreur", f"Une erreur s'est produite lors du chargement des étudiants : {e}")

    def load_UE(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            niveau = self.ui.niveauComboBox.currentText()
            mention = self.ui.mentionComboBox.currentText()
            query = "SELECT DISTINCT ueCours FROM CoursTable WHERE niveau = ? AND mention = ?"
            cursor.execute(query, (niveau, mention))
            ues = cursor.fetchall()
            conn.close()

            # Ajouter une ligne d'invite
            self.ui.uniteComboBox.clear()
            self.ui.uniteComboBox.addItem("Choisir l'unité d'enseignement", None)

            # Ajouter les noms des UE
            seen_ues = set()
            for ueCours in ues:
                if ueCours[0] not in seen_ues:
                    self.ui.uniteComboBox.addItem(ueCours[0])
                    seen_ues.add(ueCours[0])

        except Exception as e:
            print(f"Une erreur s'est produite lors du chargement des UE : {e}")
            QMessageBox.critical(self, "Erreur", f"Une erreur s'est produite lors du chargement des UE : {e}")

    def save_releve(self):
        # Récupérer les données des champs
        mention = self.ui.mentionComboBox.currentText()
        niveau = self.ui.niveauComboBox.currentText()
        etudiant_id = self.ui.etudiantComboBox.currentData()
        unite_id = self.ui.uniteComboBox.currentText()  # Modifier pour obtenir le texte au lieu de l'index
        etudiant_nom = self.ui.etudiantComboBox.currentText()

        # Valider les données si nécessaire
        if not all([mention, niveau, etudiant_id, unite_id]):
            QMessageBox.warning(self, "Erreur", "Veuillez sélectionner des valeurs.")
            return

        # Afficher les éléments constitutifs de l'unité d'enseignement sélectionnée avec leurs notes et calculer la moyenne
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            query = """
            SELECT ecCours, notes, CoursTable.credit
            FROM Table_Notes
            JOIN CoursTable ON Table_Notes.idCours = CoursTable.idCours
            WHERE ueCours = ?
            """
            cursor.execute(query, (unite_id,))
            elements_notes = cursor.fetchall()
            conn.close()

            print(f"Éléments constitutifs de l'UE '{unite_id}' et leurs notes :")
            total_notes = 0
            count_notes = 0
            total_credits = 0
            for ecCours, note, credits in elements_notes:
                print(f"- {ecCours}: {note} (Crédits: {credits})")
                total_notes += note
                count_notes += 1
                total_credits += credits

            if count_notes > 0:
                moyenne = total_notes / count_notes
                print(f"Moyenne des notes pour l'UE '{unite_id}': {moyenne:.2f}")

                # Calculer le total des crédits en fonction de la moyenne
                if moyenne < 5:
                    credits_obtenus = total_credits * 0.25
                elif 5 <= moyenne < 10:
                    credits_obtenus = total_credits * 0.33
                elif moyenne == 10:
                    credits_obtenus = total_credits * 0.50
                else:
                    credits_obtenus = total_credits

                # Calculer le pourcentage des crédits obtenus
                pourcentage_credits_obtenus = (credits_obtenus / total_credits) * 100

                print(f"Crédits obtenus pour l'UE '{unite_id}': {credits_obtenus:.2f}")
                print(f"Pourcentage des crédits obtenus pour l'UE '{unite_id}': {pourcentage_credits_obtenus:.2f}%")

                # Décision du jury
                decision_jury = "non valide" if pourcentage_credits_obtenus < 50 else "valide"
                print(f"Décision du jury pour l'UE '{unite_id}': {decision_jury}")

                # Émettre le signal avec les informations nécessaires
                releve_data = {
                    "nom_etudiant": etudiant_nom,
                    "unite_enseignement": unite_id,
                    "note_finale": moyenne,
                    "credit_obtenu": credits_obtenus,
                    "pourcentage_credits": pourcentage_credits_obtenus,  # Ajouter le pourcentage dans les données du relevé
                    "decision_jury": decision_jury
                }
                self.releve_ajoute.emit(releve_data)

                # Réinitialiser les QComboBox
                self.ui.niveauComboBox.setCurrentIndex(0)
                self.ui.mentionComboBox.setCurrentIndex(0)
                self.ui.etudiantComboBox.setCurrentIndex(0)
                self.ui.uniteComboBox.setCurrentIndex(0)

                # Fermer le modal
                self.accept()

            else:
                print(f"Aucune note disponible pour calculer la moyenne de l'UE '{unite_id}'")

        except Exception as e:
            print(f"Une erreur s'est produite lors de l'affichage des éléments constitutifs et des notes : {e}")
            QMessageBox.critical(self, "Erreur", f"Une erreur s'est produite lors de l'affichage des éléments constitutifs et des notes : {e}")
