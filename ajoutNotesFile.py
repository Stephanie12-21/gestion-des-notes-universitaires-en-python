from PySide6.QtWidgets import QDialog, QMessageBox
from PySide6.QtCore import Qt, QDate, QObject, Signal
from ajoutNotes import Ui_Dialog  # Import de la classe générée
from db import get_db_connection

class NotesDialog(QDialog):
    notes_ajoute = Signal()  # Définir un signal pour indiquer l'ajout d'une note

    def __init__(self, parent=None):
        super(NotesDialog, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # Charger les noms des étudiants dans le ComboBox
        self.load_etudiants()

        # Charger les éléments constitutifs dans le ComboBox
        self.load_element()

        # Connecter le bouton saveBtn à la méthode save_notes
        self.ui.saveBtn.clicked.connect(self.save_notes)
    
    def load_etudiants(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            query = "SELECT idEtudiant, nomEtudiant FROM EtudiantTable"
            cursor.execute(query)
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

    def load_element(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            query = "SELECT idCours, ecCours FROM CoursTable"
            cursor.execute(query)
            cours = cursor.fetchall()
            conn.close()

            # Ajouter une ligne d'invite 
            self.ui.elemCfComboBox.clear()
            self.ui.elemCfComboBox.addItem("Choisir l'élément constitutif concerné", None)

            # Ajouter les éléments constitutifs 
            for idCours, ecCours in cours:
                self.ui.elemCfComboBox.addItem(ecCours, idCours)

        except Exception as e:
            print(f"Une erreur s'est produite lors du chargement des éléments constitutifs : {e}")
            QMessageBox.critical(self, "Erreur", f"Une erreur s'est produite lors du chargement des éléments constitutifs : {e}")

    def save_notes(self):
        # Récupérer les données des champs
        date_examen = self.ui.dateEdit.date().toString(Qt.ISODate)
        semestre = self.ui.semestreComboBox.currentText()
        notes = self.ui.noteLineEdit.text()
        session = self.ui.sessionComboBox.currentText()
        idCours = self.ui.elemCfComboBox.currentData()
        idEtudiant = self.ui.etudiantComboBox.currentData()

        # Valider les données si nécessaire
        if not all([notes, date_examen, semestre, session, idCours, idEtudiant]):
            QMessageBox.warning(self, "Erreur", "Tous les champs doivent être remplis.")
            return

        
        # Insérer les données dans la base de données
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            query = """INSERT INTO Table_Notes 
                    (idEtudiant, idCours, notes, semestre, dateExamen, session) 
                    VALUES (?, ?, ?, ?, ?, ?)"""
            cursor.execute(query, (idEtudiant, idCours, notes, semestre, date_examen, session))
            conn.commit()
            conn.close()

            # Afficher un message de succès
            QMessageBox.information(self, "Succès", "Les données ont été insérées avec succès.")
            
            # Émettre le signal indiquant l'ajout d'une note
            self.notes_ajoute.emit()
            
            # Réinitialiser les champs
            self.ui.dateEdit.setDate(QDate.currentDate())
            self.ui.semestreComboBox.setCurrentIndex(0)
            self.ui.sessionComboBox.setCurrentIndex(0)
            self.ui.elemCfComboBox.setCurrentIndex(0)
            self.ui.etudiantComboBox.setCurrentIndex(0)
            self.ui.noteLineEdit.clear()
            
            # Fermer le modal
            self.accept()

        except Exception as e:
            print(f"Une erreur s'est produite : {e}")  # Afficher l'erreur dans la console
            QMessageBox.critical(self, "Erreur", f"Une erreur s'est produite : {e}")
