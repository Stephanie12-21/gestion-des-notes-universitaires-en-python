from PySide6.QtWidgets import QDialog
from supEtudiantMsgBox import Ui_EtudiantSupDialog

class SupEtudiantMessageBox(QDialog, Ui_EtudiantSupDialog):
    def __init__(self, id_etd, parent=None):
        super(SupEtudiantMessageBox, self).__init__(parent)
        self.setupUi(self)
        self.supBtn.clicked.connect(self.accept)
        self.cancelBtn.clicked.connect(self.reject)

        # Afficher l'ID de l'étudiant dans le label
        self.label.setText(f"Êtes-vous sûr de vouloir supprimer les données liées à l'ID {id_etd} ?")