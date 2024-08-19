from PySide6.QtWidgets import QDialog, QMessageBox
from PySide6.QtCore import Qt, QDate, QObject, Signal
from ajoutEtd import Ui_EtdDialog  # Import de la classe générée
from db import get_db_connection

class EtdDialog(QDialog):
    # Définir un signal pour indiquer l'ajout d'un étudiant
    etudiant_ajoute = Signal()

    def __init__(self, parent=None):
        super(EtdDialog, self).__init__(parent)
        self.ui = Ui_EtdDialog()
        self.ui.setupUi(self)

        # Connecter le bouton saveBtn à la méthode save_etudiant
        self.ui.saveBtn.clicked.connect(self.save_etudiant)

    def save_etudiant(self):
        # Récupérer les données des champs
        mention = self.ui.mentionComboBox.currentText()
        niveau = self.ui.niveauComboBox.currentText()
        date_naissance = self.ui.dateNaissance.date().toString(Qt.ISODate)
        nom = self.ui.nomLineEdit.text()
        num_tel = self.ui.numTelLineEdit.text()
        email = self.ui.emailLineEdit.text()
        adresse = self.ui.adresseLineEdit.text()

        # Valider les données si nécessaire
        if not all([mention, niveau, date_naissance, nom, num_tel, email, adresse]):
            QMessageBox.warning(self, "Erreur", "Tous les champs doivent être remplis.")
            return

        # Insérer les données dans la base de données
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            query = """INSERT INTO EtudiantTable 
                       (nomEtudiant, dateNaisEtudiant, contactEtudiant, emailEtudiant, adresseEtudiant, mention, niveau) 
                       VALUES (?, ?, ?, ?, ?, ?, ?)"""
            cursor.execute(query, (nom, date_naissance, num_tel, email, adresse, mention, niveau))
            conn.commit()
            conn.close()

            # Afficher un message de succès
            QMessageBox.information(self, "Succès", "Les données ont été insérées avec succès.")
            
            # Émettre le signal indiquant l'ajout d'un étudiant
            self.etudiant_ajoute.emit()
            
            # Réinitialiser les champs
            self.ui.nomLineEdit.clear()
            self.ui.numTelLineEdit.clear()
            self.ui.emailLineEdit.clear()
            self.ui.adresseLineEdit.clear()
            self.ui.mentionComboBox.setCurrentIndex(0)
            self.ui.niveauComboBox.setCurrentIndex(0)
            self.ui.dateNaissance.setDate(QDate.currentDate())
            
            # Fermer le modal
            self.accept()

        except Exception as e:
            print(f"Une erreur s'est produite : {e}")  # Afficher l'erreur dans la console
            QMessageBox.critical(self, "Erreur", f"Une erreur s'est produite : {e}")
    etudiant_ajoute = Signal()  # Définir un signal pour indiquer l'ajout d'un étudiant

    def __init__(self, parent=None):
        super(EtdDialog, self).__init__(parent)
        self.ui = Ui_EtdDialog()
        self.ui.setupUi(self)

        # Connecter le bouton saveBtn à la méthode save_etudiant
        self.ui.saveBtn.clicked.connect(self.save_etudiant)

    def save_etudiant(self):
        # Récupérer les données des champs
        mention = self.ui.mentionComboBox.currentText()
        niveau = self.ui.niveauComboBox.currentText()
        date_naissance = self.ui.dateNaissance.date().toString(Qt.ISODate)
        nom = self.ui.nomLineEdit.text()
        # Modifier la récupération du numéro de téléphone pour le formater en tant que chaîne de caractères
        num_tel = self.ui.numTelLineEdit.text()
        email = self.ui.emailLineEdit.text()
        adresse = self.ui.adresseLineEdit.text()

        



        # Valider les données si nécessaire
        if not all([mention, niveau, date_naissance, nom, num_tel, email, adresse]):
            QMessageBox.warning(self, "Erreur", "Tous les champs doivent être remplis.")
            return

        # Insérer les données dans la base de données
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            query = """INSERT INTO EtudiantTable 
                       (nomEtudiant, dateNaisEtudiant, contactEtudiant, emailEtudiant, adresseEtudiant, mention, niveau) 
                       VALUES (?, ?, ?, ?, ?, ?, ?)"""
            cursor.execute(query, (nom, date_naissance, num_tel, email, adresse, mention, niveau))
            conn.commit()
            conn.close()

            # Afficher un message de succès
            QMessageBox.information(self, "Succès", "Les données ont été insérées avec succès.")
            
            # Émettre le signal indiquant l'ajout d'un étudiant
            self.etudiant_ajoute.emit()
            
            # Réinitialiser les champs
            self.ui.nomLineEdit.clear()
            self.ui.numTelLineEdit.clear()
            self.ui.emailLineEdit.clear()
            self.ui.adresseLineEdit.clear()
            self.ui.mentionComboBox.setCurrentIndex(0)
            self.ui.niveauComboBox.setCurrentIndex(0)
            self.ui.dateNaissance.setDate(QDate.currentDate())
            
            # Fermer le modal
            self.accept()

        except Exception as e:
            print(f"Une erreur s'est produite : {e}")  # Afficher l'erreur dans la console
            QMessageBox.critical(self, "Erreur", f"Une erreur s'est produite : {e}")