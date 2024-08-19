from PySide6.QtWidgets import QDialog, QMessageBox
from PySide6.QtCore import Qt, QDate, QObject, Signal
from ajoutCours import Ui_Dialog  # Import de la classe générée
from db import get_db_connection

class CoursDialog(QDialog):
    cours_ajoute = Signal()  # Définir un signal pour indiquer l'ajout d'un cours

    def __init__(self, parent=None):
        super(CoursDialog, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # Charger les noms des professeurs dans le profComboBox
        self.load_professors()

        # Connecter le bouton saveBtn à la méthode save_cours
        self.ui.saveBtn.clicked.connect(self.save_cours)

    def load_professors(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            query = "SELECT idProf, nomProf FROM ProfTable"
            cursor.execute(query)
            professeurs = cursor.fetchall()
            conn.close()

            # Ajouter une ligne d'invite au profComboBox
            self.ui.profComboBox.clear()
            self.ui.profComboBox.addItem("Enseignant en charge", None)

            # Ajouter les noms des professeurs au profComboBox
            for idProf, nomProf in professeurs:
                self.ui.profComboBox.addItem(nomProf, idProf)

        except Exception as e:
            print(f"Une erreur s'est produite lors du chargement des professeurs : {e}")
            QMessageBox.critical(self, "Erreur", f"Une erreur s'est produite lors du chargement des professeurs : {e}")

    def save_cours(self):
        # Récupérer les données des champs
        mention = self.ui.mentionComboBox.currentText()
        niveau = self.ui.niveauComboBox.currentText()
        semestre = self.ui.semestreComboBox.currentText()
        prof_index = self.ui.profComboBox.currentIndex()
        idProf = self.ui.profComboBox.itemData(prof_index)
        credit = self.ui.creditComboBox.currentText()
        elementC = self.ui.elemCLineEdit.text()
        uniteE = self.ui.uniteLineEdit.text()

        # Valider les données si nécessaire
        if not all([mention, niveau, semestre, idProf, credit, elementC, uniteE]):
            QMessageBox.warning(self, "Erreur", "Tous les champs doivent être remplis.")
            return

        # Insérer les données dans la base de données
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            query = """INSERT INTO CoursTable 
                       (ueCours, ecCours, idProf, semestre, credit, niveau, mention) 
                       VALUES (?, ?, ?, ?, ?, ?, ?)"""
            cursor.execute(query, (uniteE, elementC, idProf, semestre, credit, niveau, mention))
            conn.commit()
            conn.close()

            # Afficher un message de succès
            QMessageBox.information(self, "Succès", "Les données ont été insérées avec succès.")
            
            # Émettre le signal indiquant l'ajout d'un cours
            self.cours_ajoute.emit()
            
            # Réinitialiser les champs
            self.ui.uniteLineEdit.clear()
            self.ui.elemCLineEdit.clear()
            self.ui.creditComboBox.setCurrentIndex(0)
            self.ui.profComboBox.setCurrentIndex(0)
            self.ui.semestreComboBox.setCurrentIndex(0)
            self.ui.mentionComboBox.setCurrentIndex(0)
            self.ui.niveauComboBox.setCurrentIndex(0)
            
            # Fermer le modal
            self.accept()

        except Exception as e:
            print(f"Une erreur s'est produite : {e}")  # Afficher l'erreur dans la console
            QMessageBox.critical(self, "Erreur", f"Une erreur s'est produite : {e}")
