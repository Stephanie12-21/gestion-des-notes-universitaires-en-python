from PySide6.QtWidgets import QDialog, QMessageBox
from PySide6.QtCore import Qt, QDate, QObject, Signal
from ajoutProf import Ui_Dialog  # Import de la classe générée
from db import get_db_connection

class ProfDialog(QDialog):
    prof_ajoute = Signal()  # Définir un signal pour indiquer l'ajout d'un étudiant

    def __init__(self, parent=None):
        super(ProfDialog, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # Connecter le bouton saveBtn à la méthode save_etudiant
        self.ui.saveBtn.clicked.connect(self.save_prof)

    def save_prof(self):
        grade = self.ui.gradeComboBox.currentText()
        nom = self.ui.nomLineEdit.text()
        num_tel = self.ui.numTelLineEdit.text()
        email = self.ui.emailLineEdit.text()
        adresse = self.ui.adresseLineEdit.text()

        



        # Valider les données si nécessaire
        if not all([nom, num_tel, email, adresse, grade]):
            QMessageBox.warning(self, "Erreur", "Tous les champs doivent être remplis.")
            return

        # Insérer les données dans la base de données
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            query = """INSERT INTO ProfTable 
                       (nomProf, contactProf, emailProf, adresseProf,gradeProf) 
                       VALUES (?, ?, ?, ?, ?)"""
            cursor.execute(query, (nom, num_tel, email, adresse, grade))
            conn.commit()
            conn.close()

            # Afficher un message de succès
            QMessageBox.information(self, "Succès", "Les données ont été insérées avec succès.")
            
            # Émettre le signal indiquant l'ajout d'un étudiant
            self.prof_ajoute.emit()
            
            # Réinitialiser les champs
            self.ui.nomLineEdit.clear()
            self.ui.numTelLineEdit.clear()
            self.ui.emailLineEdit.clear()
            self.ui.adresseLineEdit.clear()
            self.ui.gradeComboBox.setCurrentIndex(0)
            
            # Fermer le modal
            self.accept()

        except Exception as e:
            print(f"Une erreur s'est produite : {e}")  # Afficher l'erreur dans la console
            QMessageBox.critical(self, "Erreur", f"Une erreur s'est produite : {e}")