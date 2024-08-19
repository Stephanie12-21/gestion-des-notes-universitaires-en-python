from PySide6.QtWidgets import QDialog
from PySide6.QtCore import Qt
from modifEtd import Ui_Dialog
from db import get_student_by_id

class ModifEtdDialog(QDialog):
    def __init__(self, idEtudiant, parent=None):
        super(ModifEtdDialog, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.idEtudiant = idEtudiant
        
        # Connectez les boutons du modal
        self.ui.saveBtn.clicked.connect(self.save_changes)
        self.ui.cancelBtn.clicked.connect(self.reject)
        
        # Chargez les données de l'étudiant correspondant à idEtd
        self.load_student_data()

    def load_student_data(self):
        # Récupérer les données de l'étudiant depuis la base de données
        student_data = get_student_by_id(self.idEtudiant)
        
        if student_data:
            # Exemple de pré-remplissage des champs avec les données récupérées
            self.ui.nomLineEdit.setText(student_data['nomEtudiant'])
            #self.ui.dateNaisEdit.setDate(student_data['date_naissance'])
            self.ui.numTelLineEdit.setText(student_data['contactEtudiant'])
            self.ui.emailLineEdit.setText(student_data['emailEtudiant'])
            self.ui.adresseLineEdit.setText(student_data['adresseEtudiant'])
            
            # Sélectionnez la mention dans le comboBox
            index = self.ui.mentionComboBox.findText(student_data['mention'])
            if index >= 0:
                self.ui.mentionComboBox.setCurrentIndex(index)
            
            # Sélectionnez le niveau dans le comboBox
            index = self.ui.niveauComboBox.findText(student_data['niveau'])
            if index >= 0:
                self.ui.niveauComboBox.setCurrentIndex(index)
        else:
            # Gérer le cas où aucune donnée n'est trouvée pour idEtd
            pass

    def save_changes(self):
        # Ajoutez votre logique pour enregistrer les modifications des données de l'étudiant ici
        nom = self.ui.nomLineEdit.text()
        date_naissance = self.ui.dateNaisEdit.date().toString(Qt.ISODate)
        contact = self.ui.numTelLineEdit.text()
        email = self.ui.emailLineEdit.text()
        adresse = self.ui.adresseLineEdit.text()
        mention = self.ui.mentionComboBox.currentText()
        niveau = self.ui.niveauComboBox.currentText()
        
        # Enregistrer les modifications dans la base de données ou faire d'autres traitements nécessaires
        # Vous pouvez passer nom, date_naissance, contact, email, adresse, mention, niveau à une fonction pour enregistrer dans la base de données
        self.accept()  # Ferme le dialogue et renvoie QDialog.Accepted
