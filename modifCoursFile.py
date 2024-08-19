from PySide6.QtWidgets import QDialog
from PySide6.QtCore import Qt
from modifCours import Ui_Dialog
from db import get_cours_by_id

class ModifCoursDialog(QDialog):
    def __init__(self, idCours, parent=None):
        super(ModifCoursDialog, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.idCours = idCours
        
        # Connectez les boutons du modal
        self.ui.saveBtn.clicked.connect(self.save_changes)
        self.ui.cancelBtn.clicked.connect(self.reject)
        
        # Chargez les données de l'étudiant correspondant à idEtd
        self.load_cours_data()

    def load_cours_data(self):
        # Récupérer les données de l'étudiant depuis la base de données
        cours_data = get_cours_by_id(self.idCours)
        
        if cours_data:
            # Exemple de pré-remplissage des champs avec les données récupérées
            self.ui.elemCLineEdit.setText(cours_data['ecCours'])
            self.ui.uniteLineEdit.setText(cours_data['ueCours'])
            
            
            # Sélectionnez la mention dans le comboBox
            index = self.ui.mentionComboBox.findText(cours_data['mention'])
            if index >= 0:
                self.ui.mentionComboBox.setCurrentIndex(index)
            
            # Sélectionnez le niveau dans le comboBox
            index = self.ui.niveauComboBox.findText(cours_data['niveau'])
            if index >= 0:
                self.ui.niveauComboBox.setCurrentIndex(index)
            
            # Sélectionnez le semestre dans le comboBox
            index = self.ui.semestreComboBox.findText(cours_data['semestre'])
            if index >= 0:
                self.ui.semestreComboBox.setCurrentIndex(index)
            
            # Sélectionnez le crédit dans le comboBox
            index = self.ui.creditComboBox.findText(cours_data['credit'])
            if index >= 0:
                self.ui.creditComboBox.setCurrentIndex(index)

            # Sélectionnez le prof dans le comboBox
            index = self.ui.profComboBox.findText(cours_data['idProf'])
            if index >= 0:
                self.ui.profComboBox.setCurrentIndex(index)
        else:
            # Gérer le cas où aucune donnée n'est trouvée pour idEtd
            pass

    def save_changes(self):
        # Ajoutez votre logique pour enregistrer les modifications des données de l'étudiant ici
        ue = self.ui.uniteLineEdit.text()
        ec = self.ui.elemCLineEdit.text()
        semestre = self.ui.semestreComboBox.currentText()
        credit = self.ui.creditComboBox.currentText()
        mention = self.ui.mentionComboBox.currentText()
        niveau = self.ui.niveauComboBox.currentText()
        
        # Enregistrer les modifications dans la base de données ou faire d'autres traitements nécessaires
        # Vous pouvez passer nom, date_naissance, contact, email, adresse, mention, niveau à une fonction pour enregistrer dans la base de données
        self.accept()  # Ferme le dialogue et renvoie QDialog.Accepted
