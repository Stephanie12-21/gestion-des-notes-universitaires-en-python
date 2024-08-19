from PySide6.QtWidgets import QDialog
from PySide6.QtCore import Qt
from modifProf import Ui_Dialog
from db import get_prof_by_id

class ModifProfDialog(QDialog):
    def __init__(self, idProf, parent=None):
        super(ModifProfDialog, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.idProf = idProf
        
        # Connectez les boutons du modal
        self.ui.saveBtn.clicked.connect(self.save_changes)
        self.ui.cancelBtn.clicked.connect(self.reject)
        
        # Chargez les données de l'enseignant correspondant à idEtd
        self.load_prof_data()

    def load_prof_data(self):
        # Récupérer les données de l'enseignant depuis la base de données
        student_data = get_prof_by_id(self.idProf)
        
        if student_data:
            # Exemple de pré-remplissage des champs avec les données récupérées
            self.ui.nomLineEdit.setText(student_data['nomProf'])
            self.ui.numTelLineEdit.setText(student_data['contactProf'])
            self.ui.emailLineEdit.setText(student_data['emailProf'])
            self.ui.adresseLineEdit.setText(student_data['adresseProf'])
            
            # Sélectionnez le niveau dans le comboBox
            index = self.ui.niveauComboBox.findText(student_data['gradeProf'])
            if index >= 0:
                self.ui.niveauComboBox.setCurrentIndex(index)
        else:
            # Gérer le cas où aucune donnée n'est trouvée pour idEtd
            pass

    def save_changes(self):
        # Ajoutez votre logique pour enregistrer les modifications des données de l'enseignant ici
        nom = self.ui.nomLineEdit.text()
        contact = self.ui.numTelLineEdit.text()
        email = self.ui.emailLineEdit.text()
        adresse = self.ui.adresseLineEdit.text()
        niveau = self.ui.niveauComboBox.currentText()
        
        # Enregistrer les modifications dans la base de données ou faire d'autres traitements nécessaires
        # Vous pouvez passer nom, date_naissance, contact, email, adresse, mention, niveau à une fonction pour enregistrer dans la base de données
        self.accept()  # Ferme le dialogue et renvoie QDialog.Accepted
