import sys
import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle
from reportlab.lib.units import inch
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QPushButton, QFileDialog, QHBoxLayout, QWidget, QMessageBox, QDialog, QLCDNumber
from PySide6.QtGui import QFont, QIcon
from PySide6.QtCore import Qt, QSize
import PyQt6.QtWidgets as QtWidgets
from mainIndex import Ui_MainWindow
from ajoutEtdFile import EtdDialog
from ajoutProfFile import ProfDialog
from ajoutCoursFile import CoursDialog
from ajoutNotesFile import NotesDialog
from ajoutReleveFile import ReleveDialog
from showStudent import load_etudiants
from showProfs import load_prof
from showCours import load_cours
from showNotes import load_notes
from modifEdtFile import ModifEtdDialog
from modifProfFile import ModifProfDialog
from modifCoursFile import ModifCoursDialog
from supEtudiantMsgBox import Ui_EtudiantSupDialog
from supProfMsgBox import Ui_SupProfDialog
from supNotesMsgBox import Ui_Dialog
from supCoursMsgBox import Ui_CoursDialog
from delete_student import delete_student
from delete_prof import delete_prof
from cours_delete import delete_cours
from delete_notes import delete_notes
from countByLevel import count_students_by_level





class SupEtudiantMessageBox(QDialog, Ui_EtudiantSupDialog):
    def __init__(self, id_etd, parent=None):
        super(SupEtudiantMessageBox, self).__init__(parent)
        self.setupUi(self)
        self.supBtn.clicked.connect(self.accept)
        self.cancelBtn.clicked.connect(self.reject)

class SupProfMessageBox(QDialog, Ui_SupProfDialog):
    def __init__(self, id_prof, parent=None):
        super(SupProfMessageBox, self).__init__(parent)
        self.setupUi(self)
        self.supBtn.clicked.connect(self.accept)
        self.cancelBtn.clicked.connect(self.reject)

class SupNotesMessageBox(QDialog, Ui_Dialog):
    def __init__(self, id_notes, parent=None):
        super(SupNotesMessageBox, self).__init__(parent)
        self.setupUi(self)
        self.supBtn.clicked.connect(self.accept)
        self.cancelBtn.clicked.connect(self.reject)
        
class SupCoursMessageBox(QDialog, Ui_Dialog):
    def __init__(self, id_cours, parent=None):
        super(SupCoursMessageBox, self).__init__(parent)
        self.setupUi(self)
        self.supBtn.clicked.connect(self.accept)
        self.cancelBtn.clicked.connect(self.reject)
        
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.update_student_count()
        

        # Connecter le signal etudiant_ajoute de EtdDialog à self.update_student_count
        self.etudiant_dialog = EtdDialog()
        self.etudiant_dialog.etudiant_ajoute.connect(self.update_student_count)

        count_l1 = count_students_by_level('L1')
        print(f"Nombre d'étudiants L1 : {count_l1}")  # Vérifiez dans la console si le nombre est correct
        self.ui.L_1_Number.display(count_l1) 

        count_l2 = count_students_by_level('L2')
        print(f"Nombre d'étudiants L2 : {count_l2}")  # Vérifiez dans la console si le nombre est correct
        self.ui.l2Numer.display(count_l2) 

        count_l3 = count_students_by_level('L3')
        print(f"Nombre d'étudiants L3 : {count_l3}")  # Vérifiez dans la console si le nombre est correct
        self.ui.l3Number.display(count_l3) 

        count_m1 = count_students_by_level('M1')
        print(f"Nombre d'étudiants M1 : {count_m1}")  # Vérifiez dans la console si le nombre est correct
        self.ui.m1Number.display(count_m1) 

        count_m2 = count_students_by_level('M2')
        print(f"Nombre d'étudiants M2 : {count_m2}")  # Vérifiez dans la console si le nombre est correct
        self.ui.m2Number.display(count_m2) 

        self.ui.dashBtn1.clicked.connect(self.show_dashboard_page)
        self.ui.dashBtn2.clicked.connect(self.show_dashboard_page)
        self.ui.etdBtn1.clicked.connect(self.show_etudiants_page)
        self.ui.etdBtn2.clicked.connect(self.show_etudiants_page)
        self.ui.esgBtn1.clicked.connect(self.show_enseignants_page)
        self.ui.esgBtn2.clicked.connect(self.show_enseignants_page)
        self.ui.coursBtn1.clicked.connect(self.show_cours_page)
        self.ui.coursBtn2.clicked.connect(self.show_cours_page)
        self.ui.notesBtn1.clicked.connect(self.show_notes_page)
        self.ui.notesBtn2.clicked.connect(self.show_notes_page)
        self.ui.rlvBtn1.clicked.connect(self.show_releves_page)
        self.ui.rlvBtn2.clicked.connect(self.show_releves_page)
        self.ui.ajoutEdtBtn.clicked.connect(self.show_ajout_etudiant_modal)
        self.ui.ajoutProfBtn.clicked.connect(self.show_ajout_prof_modal)
        self.ui.ajoutCoursBtn.clicked.connect(self.show_ajout_cours_modal)
        self.ui.ajoutNotesBtn.clicked.connect(self.show_ajout_notes_modal)
        self.ui.ajoutReleveBtn.clicked.connect(self.show_ajout_releve_modal)
        # Exemple de connexion du signal dans votre classe principale
        self.releve_dialog = ReleveDialog()
        self.releve_dialog.releve_ajoute.connect(self.add_releve_to_table)

        # Connecter le bouton pdfReleveBtn à la méthode export_to_pdf
        self.ui.pdfReleveBtn.clicked.connect(self.export_to_pdf)
        
        # Désactiver le bouton pdfReleveBtn par défaut
        self.ui.pdfReleveBtn.setEnabled(False)

        # Connecter le bouton pdfReleveBtn à la méthode export_to_pdf
        self.ui.pdfReleveBtn.clicked.connect(self.export_to_pdf)
        self.ui.pdfEtd.clicked.connect(self.export_etudiant_pdf)

        # Connecter la sélection de ligne à la méthode update_pdf_button_state
        selection_model = self.ui.tableWidget.selectionModel()
        selection_model.selectionChanged.connect(self.update_pdf_button_state)

        # Connectez le signal de changement de sélection de niveauComboBox à la méthode de filtrage
        self.ui.niveauComboBox.currentTextChanged.connect(self.print_selected_niveau)
        self.ui.niveauComboBox.currentTextChanged.connect(self.update_etudiant_table)
        self.ui.mentionComboBox.currentTextChanged.connect(self.update_etudiant_table)
        self.ui.searchLineEditEtd.textChanged.connect(self.update_etudiant_table)
        self.ui.gradeComboBox.currentTextChanged.connect(self.update_prof_table)
        self.ui.searchProfLineEditEtd.textChanged.connect(self.filter_prof_by_search)
        self.ui.semestreComboBox.currentTextChanged.connect(self.filter_cours_by_semestre)
        self.ui.semestreComboBox.currentTextChanged.connect(self.filter_cours)
        self.ui.creditComboBox.currentTextChanged.connect(self.filter_cours)
        self.ui.searchLineEditEtd_2.textChanged.connect(self.filter_cours)
        self.ui.seuilComboBox.currentTextChanged.connect(self.filter_notes)
        self.ui.sessionComboBox.currentTextChanged.connect(self.filter_notes)
        self.ui.searchNotesLineEditEtd.textChanged.connect(self.filter_notes_by_text) 


        self.load_and_display_etudiants()
        self.load_and_display_prof()
        self.load_and_display_cours()
        self.load_and_display_notes() 

    def show_dashboard_page(self):
        self.ui.pageContainer.setCurrentWidget(self.ui.pageDashboard)
    
    def show_etudiants_page(self):
        self.ui.pageContainer.setCurrentWidget(self.ui.pageEtudiants)

    def show_enseignants_page(self):
        self.ui.pageContainer.setCurrentWidget(self.ui.pageEnseignants)

    def show_cours_page(self):
        self.ui.pageContainer.setCurrentWidget(self.ui.pageCours)
    
    def show_notes_page(self):
        self.ui.pageContainer.setCurrentWidget(self.ui.pageNotes)
    
    def show_releves_page(self):
        self.ui.pageContainer.setCurrentWidget(self.ui.pageReleves)

    def show_ajout_etudiant_modal(self):
        self.ajoutEtd = EtdDialog(self)
        self.ajoutEtd.etudiant_ajoute.connect(self.load_and_display_etudiants)
        self.ajoutEtd.exec_()

    def load_and_display_etudiants(self):
        etudiant_data = load_etudiants()
        if etudiant_data:
            self.set_tableEtudiant_data(self.ui.EtudiantTable, etudiant_data)
        else:
            QMessageBox.critical(self, "Erreur", "Impossible de charger les données des étudiants.")
    
    def update_etudiant_table(self):
        niveau = self.ui.niveauComboBox.currentText()
        mention = self.ui.mentionComboBox.currentText()
        search_term = self.ui.searchLineEditEtd.text()
        
        print(f"Niveau sélectionné : {niveau}, Mention sélectionnée : {mention}, Terme de recherche : {search_term}")

        if niveau == "Choisir le niveau":
            niveau = None

        if mention == "Choisir la mention":
            mention = None

        etudiant_data = load_etudiants(niveau, mention, search_term)
        if etudiant_data:
            print(f"Données chargées : {etudiant_data}")
            self.set_tableEtudiant_data(self.ui.EtudiantTable, etudiant_data)
        else:
            QMessageBox.critical(self, "Erreur", "Impossible de charger les données des étudiants.")

    def set_tableEtudiant_data(self, table_widget, data):
        headers, rows = data

        if "Actions" not in headers:
            headers.append("Actions")

        table_widget.setColumnCount(len(headers))
        table_widget.setRowCount(len(rows))
        table_widget.setHorizontalHeaderLabels(headers)

        font = QFont()
        font.setPointSize(10)

        for row_idx, row_data in enumerate(rows):
            for col_idx, item in enumerate(row_data):
                table_item = QTableWidgetItem(str(item))
                table_item.setFont(font)
                table_item.setTextAlignment(Qt.AlignCenter)
                table_widget.setItem(row_idx, col_idx, table_item)

            action_layout = QHBoxLayout()
            edit_button = QPushButton()
            delete_button = QPushButton()

            edit_button.setIcon(QIcon(r"D:\LES PROJETS DE RYUK\projet pyhton tena izy\icons\icons8-modifier-64 (1).png"))
            delete_button.setIcon(QIcon(r"D:\LES PROJETS DE RYUK\projet pyhton tena izy\icons\icons8-poubelle-64.png"))
            edit_button.setIconSize(QSize(30, 30))
            delete_button.setIconSize(QSize(30, 30))

            edit_button.setCheckable(True)
            delete_button.setCheckable(True)

            edit_button.clicked.connect(lambda checked, row_idx=row_idx: self.show_modif_etudiant_modal(row_idx))
            delete_button.clicked.connect(lambda checked, row_idx=row_idx: self.show_sup_message_box(row_idx))

            action_layout.addWidget(edit_button)
            action_layout.addWidget(delete_button)

            action_widget = QWidget()
            action_widget.setLayout(action_layout)

            table_widget.setCellWidget(row_idx, len(headers) - 1, action_widget)
    
    def show_modif_etudiant_modal(self, row_idx):
        modif_etd = ModifEtdDialog(self)
        nom = self.ui.EtudiantTable.item(row_idx, 0).text()
        modif_etd.ui.nomLineEdit.setText(nom)
        modif_etd.exec_()

    def show_sup_message_box(self, row_idx):
        id_etd = self.ui.EtudiantTable.item(row_idx, 0).text()  # Suppose que l'ID est dans la première colonne
        sup_message_box = SupEtudiantMessageBox(id_etd, self)
        if sup_message_box.exec_() == QDialog.Accepted:
            delete_student(id_etd)
            self.load_and_display_etudiants()
            QMessageBox.information(self, "Supprimé", f"L'étudiant avec l'ID {id_etd} a été supprimé.")
        else:
            QMessageBox.information(self, "Annulé", "La suppression a été annulée.")

    def get_filtered_etudiants_data(self):
        niveau = self.ui.niveauComboBox.currentText()
        mention = self.ui.mentionComboBox.currentText()
        search_term = self.ui.searchLineEditEtd.text()

        if niveau == "Choisir le niveau":
            niveau = None

        if mention == "Choisir la mention":
            mention = None

        etudiant_data = load_etudiants(niveau, mention, search_term)
        return etudiant_data

    def print_selected_niveau(self, niveau):
        print(f"Niveau sélectionné : {niveau}")
        if niveau == "Choisir le niveau":
            etudiant_data = load_etudiants()  # Charger toutes les données
        else:
            etudiant_data = load_etudiants(niveau)  # Charger les données filtrées

        if etudiant_data:
            print(f"Données chargées : {etudiant_data}")
            self.set_tableEtudiant_data(self.ui.EtudiantTable, etudiant_data)
        else:
            QMessageBox.critical(self, "Erreur", "Impossible de charger les données des étudiants.")
    
    def update_student_count(self):
        # Fonction pour mettre à jour le nombre d'étudiants L1 dans le QLCDNumber
        count_l1 = count_students_by_level('L1')
        print(f"Nombre d'étudiants L1 : {count_l1}")  # Vérifiez dans la console si le nombre est correct
        self.ui.L_1_Number.display(count_l1) 

    def export_etudiant_pdf(self):
        # Récupérer les données filtrées des étudiants
        etudiant_data = self.get_filtered_etudiants_data()

        if not etudiant_data:
            QMessageBox.warning(self, "Aucune donnée", "Aucune donnée d'étudiant à exporter selon les filtres sélectionnés.")
            return

        headers, rows = etudiant_data

        # Ouvrir une boîte de dialogue pour choisir le chemin de sauvegarde du PDF
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_path, _ = QFileDialog.getSaveFileName(self, "Enregistrer sous PDF", "", "PDF Files (*.pdf);;All Files (*)", options=options)
        if not file_path:
            return  # Annuler si aucun fichier n'est choisi

        if not file_path.endswith('.pdf'):
            file_path += '.pdf'

        # Récupérer le niveau et la mention sélectionnés
        niveau = self.ui.niveauComboBox.currentText()
        mention = self.ui.mentionComboBox.currentText()

        # Définir le titre du PDF
        title = f"Liste des étudiants - Niveau : {niveau}, Mention : {mention}"

        # Initialiser le canvas PDF
        c = canvas.Canvas(file_path, pagesize=letter)
        width, height = letter

        # Définir la position initiale pour écrire les données
        x_offset = 50
        y_offset = height - 50
        line_height = 20

        # Ajouter le titre
        c.setFont("Helvetica-Bold", 16)
        c.drawString(x_offset, y_offset, title)
        y_offset -= line_height * 2

        # Sélectionner uniquement les colonnes à exporter et les mapper aux colonnes dans les données
        export_columns = ["Identifiant", "Nom", "Date de naissance", "Contact", "Email"]
        column_mapping = {
            "Identifiant": 0,  # Index de la colonne idEtudiant dans les données
            "Nom": 1,          # Index de la colonne nomEtudiant dans les données
            "Date de naissance": 2,  # Index de la colonne dateNaissance dans les données
            "Contact": 3,      # Index de la colonne numTelEtudiant dans les données
            "Email": 4         # Index de la colonne emailEtudiant dans les données
        }

        # Définir les données du tableau à exporter
        data = []
        data.append(export_columns)  # Ajouter les en-têtes de colonnes

        for row in rows:
            data_row = []
            for col in export_columns:
                try:
                    data_value = row[column_mapping[col]]
                    data_row.append(str(data_value))
                except IndexError as e:
                    data_row.append("")  # Gérer les cas où la valeur est manquante
                    print(f"Error accessing column '{col}': {e}")
            data.append(data_row)

        # Créer le tableau
        table = Table(data, colWidths=[1.5*inch]*len(export_columns))  # Ajuster la largeur des colonnes

        # Définir le style du tableau
        style = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ])
        table.setStyle(style)

        # Dessiner le tableau sur le canvas
        table.wrapOn(c, width, height)
        table.drawOn(c, x_offset, y_offset - len(data) * line_height)  # Ajuster la position y en fonction de la taille du tableau

        # Sauvegarder le PDF
        c.save()

        QMessageBox.information(self, "Succès", "Les données des étudiants ont été exportées en PDF avec succès!")
###########################################POUR LA PAGE ENSEIGNANT######################################

    def show_ajout_prof_modal(self):
        self.ajoutProf = ProfDialog(self)
        self.ajoutProf.prof_ajoute.connect(self.load_and_display_prof)
        self.ajoutProf.exec_()

    def update_prof_table(self):
        grade = self.ui.gradeComboBox.currentText()
        print(f"Grade sélectionné : {grade}")

        if grade == "Choisir le grade":
            grade = None

        self.load_and_display_prof(grade=grade)

    def filter_prof_by_search(self):
        search_text = self.ui.searchProfLineEditEtd.text()
        print(f"Texte de recherche : {search_text}")
        
        grade = self.ui.gradeComboBox.currentText()
        if grade == "Choisir le grade":
            grade = None

        self.load_and_display_prof(grade=grade, search_text=search_text)

    def load_and_display_prof(self, grade=None, search_text=None):
        prof_data = load_prof(grade, search_text)
        if prof_data:
            self.set_tableProf_data(self.ui.ProfTable, prof_data)
        else:
            QMessageBox.critical(self, "Erreur", "Impossible de charger les données des professeurs.")

    def set_tableProf_data(self, table_widget, data):
        headers, rows = data

        if "Actions" not in headers:
            headers.append("Actions")

        table_widget.setColumnCount(len(headers))
        table_widget.setRowCount(len(rows))
        table_widget.setHorizontalHeaderLabels(headers)

        font = QFont()
        font.setPointSize(10)

        for row_idx, row_data in enumerate(rows):
            for col_idx, item in enumerate(row_data):
                table_item = QTableWidgetItem(str(item))
                table_item.setFont(font)
                table_item.setTextAlignment(Qt.AlignCenter)
                table_widget.setItem(row_idx, col_idx, table_item)

            action_layout = QHBoxLayout()
            edit_button = QPushButton()
            delete_button = QPushButton()

            edit_button.setIcon(QIcon(r"D:\LES PROJETS DE RYUK\projet pyhton tena izy\icons\icons8-modifier-64 (1).png"))
            delete_button.setIcon(QIcon(r"D:\LES PROJETS DE RYUK\projet pyhton tena izy\icons\icons8-poubelle-64.png"))
            edit_button.setIconSize(QSize(30, 30))
            delete_button.setIconSize(QSize(30, 30))

            edit_button.setCheckable(True)
            delete_button.setCheckable(True)

            edit_button.clicked.connect(lambda checked, row_idx=row_idx: self.show_modif_prof_modal(row_idx))
            delete_button.clicked.connect(lambda checked, row_idx=row_idx: self.show_supProf_message_box(row_idx))

            action_layout.addWidget(edit_button)
            action_layout.addWidget(delete_button)

            action_widget = QWidget()
            action_widget.setLayout(action_layout)

            table_widget.setCellWidget(row_idx, len(headers) - 1, action_widget)
            
    def show_modif_prof_modal(self, row_idx):
        modif_prof = ModifProfDialog(self)
        nom = self.ui.ProfTable.item(row_idx, 0).text()
        modif_prof.ui.nomLineEdit.setText(nom)
        modif_prof.exec_()

    def show_supProf_message_box(self, row_idx):
        id_prof = self.ui.ProfTable.item(row_idx, 0).text()  # Suppose que l'ID est dans la première colonne
        sup_message_box = SupProfMessageBox(id_prof, self)
        if sup_message_box.exec_() == QDialog.Accepted:
            delete_prof(id_prof)
            self.load_and_display_prof()
            QMessageBox.information(self, "Supprimé", f"L'enseignant avec l'ID {id_prof} a été supprimé.")
        else:
            QMessageBox.information(self, "Annulé", "La suppression a été annulée.")

    def filter_etudiants_by_niveau(self, niveau):
        etudiant_data = load_etudiants()  # Chargez les données des étudiants depuis votre source de données
        if not etudiant_data:
            return

        filtered_data = []
        if niveau == "Tous":  # Si "Tous" est sélectionné, affichez tous les étudiants
            filtered_data = etudiant_data[1]  # Utilisez les données brutes
        else:
            # Sinon, filtrez les étudiants par niveau sélectionné
            for row in etudiant_data[1]:
                if row[2] == niveau:  # Supposant que le niveau est à l'index 2 dans vos données
                    filtered_data.append(row)

        self.set_tableEtudiant_data(self.ui.EtudiantTable, (etudiant_data[0], filtered_data))
############################################POUR LA PAGE ENSEIGNANT######################################

############################################POUR LA PAGE COURS######################################
    def show_ajout_cours_modal(self):
        self.ajoutCours = CoursDialog(self)
        self.ajoutCours.cours_ajoute.connect(self.load_and_display_cours)
        self.ajoutCours.exec_()

    def load_and_display_cours(self, semestre=None, credit=None, search_text=None):
        cours_data = load_cours(semestre, credit, search_text)
        if cours_data:
            self.set_tableCours_data(self.ui.CoursTable, cours_data)
        else:
            QMessageBox.critical(self, "Erreur", "Impossible de charger les données des cours.")

    def filter_cours(self):
        semestre = self.ui.semestreComboBox.currentText()
        credit = self.ui.creditComboBox.currentText()
        search_text = self.ui.searchLineEditEtd_2.text()
        print(f"Semestre sélectionné : {semestre}")
        print(f"Crédit sélectionné : {credit}")
        print(f"Texte de recherche : {search_text}")

        if semestre == "Choisir le semestre":
            semestre = None
        if credit == "Choisir le crédit":
            credit = None

        self.load_and_display_cours(semestre=semestre, credit=credit, search_text=search_text)

    def set_tableCours_data(self, table_widget, data):
        headers, rows = data

        if "Actions" not in headers:
            headers.append("Actions")

        table_widget.setColumnCount(len(headers))
        table_widget.setRowCount(len(rows))
        table_widget.setHorizontalHeaderLabels(headers)

        font = QFont()
        font.setPointSize(10)

        for row_idx, row_data in enumerate(rows):
            for col_idx, item in enumerate(row_data):
                table_item = QTableWidgetItem(str(item))
                table_item.setFont(font)
                table_item.setTextAlignment(Qt.AlignCenter)
                table_widget.setItem(row_idx, col_idx, table_item)

            action_layout = QHBoxLayout()
            edit_button = QPushButton()
            delete_button = QPushButton()

            edit_button.setIcon(QIcon(r"D:\LES PROJETS DE RYUK\projet pyhton tena izy\icons\icons8-modifier-64 (1).png"))
            delete_button.setIcon(QIcon(r"D:\LES PROJETS DE RYUK\projet pyhton tena izy\icons\icons8-poubelle-64.png"))
            edit_button.setIconSize(QSize(30, 30))
            delete_button.setIconSize(QSize(30, 30))

            edit_button.setCheckable(True)
            delete_button.setCheckable(True)

            edit_button.clicked.connect(lambda checked, row_idx=row_idx: self.show_modif_cours_modal(row_idx))
            delete_button.clicked.connect(lambda checked, row_idx=row_idx: self.show_supCours_message_box(row_idx))

            action_layout.addWidget(edit_button)
            action_layout.addWidget(delete_button)

            action_widget = QWidget()
            action_widget.setLayout(action_layout)

            table_widget.setCellWidget(row_idx, len(headers) - 1, action_widget)

    def show_modif_cours_modal(self, row_idx):
        modif_prof = ModifCoursDialog(self)
        nom = self.ui.CoursTable.item(row_idx, 0).text()
        modif_prof.exec_()

    def show_supCours_message_box(self, row_idx):
        id_cours = self.ui.CoursTable.item(row_idx, 0).text()  # Suppose que l'ID est dans la première colonne
        sup_message_box = SupCoursMessageBox(id_cours, self)
        if sup_message_box.exec_() == QDialog.Accepted:
            delete_cours(id_cours)
            self.load_and_display_cours()
            QMessageBox.information(self, "Supprimé", f"L'enseignant avec l'ID {id_cours} a été supprimé.")
        else:
            QMessageBox.information(self, "Annulé", "La suppression a été annulée.")
    
    def filter_cours_by_semestre(self):
        semestre = self.ui.semestreComboBox.currentText()
        print(f"Semestre sélectionné : {semestre}")

        if semestre == "Choisir le semestre":
            semestre = None

        self.load_and_display_cours(semestre=semestre)

############################################POUR LA PAGE COURS######################################

############################################POUR LA PAGE NOTES######################################
    def show_ajout_notes_modal(self):
        self.ajoutNotes = NotesDialog(self)
        self.ajoutNotes.notes_ajoute.connect(self.load_and_display_notes)
        self.ajoutNotes.exec_()
    
    def filter_notes(self):
        seuil = self.ui.seuilComboBox.currentText()
        session = self.ui.sessionComboBox.currentText()
        print(f"Seuil sélectionné : {seuil}, Session sélectionnée : {session}")

        if seuil == "Choisir le seuil":
            seuil = None
        if session == "Choisir la session":
            session = None

        self.load_and_display_notes(seuil=seuil, session=session)

    def load_and_display_notes(self, seuil=None, session=None):
        notes_data = load_notes(seuil, session)
        if notes_data:
            self.set_tableNotes_data(self.ui.NotesTable, notes_data)
        else:
            QMessageBox.critical(self, "Erreur", "Impossible de charger les données des notes.")

    def set_tableNotes_data(self, table_widget, data):
        headers, rows = data

        if "Actions" not in headers:
            headers.append("Actions")

        table_widget.setColumnCount(len(headers))
        table_widget.setRowCount(len(rows))
        table_widget.setHorizontalHeaderLabels(headers)

        font = QFont()
        font.setPointSize(10)

        for row_idx, row_data in enumerate(rows):
            for col_idx, item in enumerate(row_data):
                table_item = QTableWidgetItem(str(item))
                table_item.setFont(font)
                table_item.setTextAlignment(Qt.AlignCenter)
                table_widget.setItem(row_idx, col_idx, table_item)

            action_layout = QHBoxLayout()
            # edit_button = QPushButton()
            delete_button = QPushButton()

            # edit_button.setIcon(QIcon(r"D:\LES PROJETS DE RYUK\projet pyhton tena izy\icons\icons8-modifier-64 (1).png"))
            delete_button.setIcon(QIcon(r"D:\LES PROJETS DE RYUK\projet pyhton tena izy\icons\icons8-poubelle-64.png"))
            # edit_button.setIconSize(QSize(30, 30))
            delete_button.setIconSize(QSize(30, 30))

            # edit_button.setCheckable(True)
            delete_button.setCheckable(True)

            # edit_button.clicked.connect(lambda checked, row_idx=row_idx: self.show_modif_notes_modal(row_idx))
            delete_button.clicked.connect(lambda checked, row_idx=row_idx: self.show_supNotes_message_box(row_idx))

            # action_layout.addWidget(edit_button)
            action_layout.addWidget(delete_button)

            action_widget = QWidget()
            action_widget.setLayout(action_layout)

            table_widget.setCellWidget(row_idx, len(headers) - 1, action_widget)
    
    def show_supNotes_message_box(self, row_idx):
        id_notes = self.ui.NotesTable.item(row_idx, 0).text()  # Suppose que l'ID est dans la première colonne
        sup_message_box = SupNotesMessageBox(id_notes, self)
        if sup_message_box.exec_() == QDialog.Accepted:
            delete_notes(id_notes)
            self.load_and_display_notes()
            QMessageBox.information(self, "Supprimé", f"Les données avec l'ID {id_notes} a été supprimé.")
        else:
            QMessageBox.information(self, "Annulé", "La suppression a été annulée.")
     
    def filter_notes_by_text(self, text):
        filtered_text = text.strip()  # Supprimer les espaces de début et de fin du texte

        # Si le texte filtré est vide, charger toutes les notes
        if not filtered_text:
            self.load_and_display_notes(seuil=self.ui.seuilComboBox.currentText(), session=self.ui.sessionComboBox.currentText())
            return

        filtered_data = []
        headers, all_notes_data = load_notes(seuil=self.ui.seuilComboBox.currentText(), session=self.ui.sessionComboBox.currentText())

        if all_notes_data:
            for row in all_notes_data:
                if any(filtered_text.lower() in str(item).lower() for item in row):
                    filtered_data.append(row)

        # Mettre à jour la table avec les données filtrées
        self.set_tableNotes_data(self.ui.NotesTable, (headers, filtered_data))

############################################POUR LA PAGE NOTES######################################
############################################POUR LA PAGE RELEVE######################################

    def show_ajout_releve_modal(self):
        self.ajoutReleve = ReleveDialog(self)
        self.ajoutReleve.releve_ajoute.connect(self.add_releve_to_table)
        self.ajoutReleve.exec_()

    def add_releve_to_table(self, releve_data):
        # Ajouter une nouvelle ligne au tableau
        row_position = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(row_position)

        # Utiliser le pourcentage de crédits obtenus directement à partir de releve_data
        pourcentage_credits_obtenus = releve_data["pourcentage_credits"]

        # Ajouter les données dans chaque colonne
        self.ui.tableWidget.setItem(row_position, 0, QTableWidgetItem(str(row_position + 1)))  # Numéro de relevé
        self.ui.tableWidget.setItem(row_position, 1, QTableWidgetItem(releve_data["nom_etudiant"]))  # Nom de l'étudiant
        self.ui.tableWidget.setItem(row_position, 2, QTableWidgetItem(releve_data["unite_enseignement"]))  # Unité d'enseignement
        self.ui.tableWidget.setItem(row_position, 3, QTableWidgetItem(f"{releve_data['note_finale']:.2f}"))  # Note finale
        self.ui.tableWidget.setItem(row_position, 4, QTableWidgetItem(f"{pourcentage_credits_obtenus:.2f}%"))  # Crédit obtenu (en pourcentage)
        self.ui.tableWidget.setItem(row_position, 5, QTableWidgetItem(releve_data["decision_jury"]))  # Décision du jury

        # Ajouter un bouton de suppression
        delete_button = QPushButton()
        delete_button.setIcon(QIcon('D:\LES PROJETS DE RYUK\projet pyhton tena izy\icons\icons8-poubelle-64.png'))  # Remplacer par le chemin de votre icône de suppression
        delete_button.clicked.connect(lambda: self.delete_releve(row_position))
        self.ui.tableWidget.setCellWidget(row_position, 6, delete_button)  # Action

    def delete_releve(self, row):
        reply = QMessageBox.question(self, 'Confirmation', 'Êtes-vous sûr de vouloir supprimer ce relevé ?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.ui.tableWidget.removeRow(row)
    
    def update_pdf_button_state(self, selected, deselected):
        # Activer le bouton pdfReleveBtn si une ligne est sélectionnée
        if selected.indexes():
            self.ui.pdfReleveBtn.setEnabled(True)
        else:
            self.ui.pdfReleveBtn.setEnabled(False)

    def export_to_pdf(self):
        # Récupérer la ligne sélectionnée
        selected_indexes = self.ui.tableWidget.selectionModel().selectedIndexes()
        
        if not selected_indexes:
            QMessageBox.warning(self, "Erreur", "Aucune ligne sélectionnée pour l'exportation PDF.")
            return

        # Récupérer les données de la ligne sélectionnée
        row = selected_indexes[0].row()
        nom_etudiant = self.ui.tableWidget.item(row, 1).text()
        unite_enseignement = self.ui.tableWidget.item(row, 2).text()
        note_finale = self.ui.tableWidget.item(row, 3).text()
        pourcentage_credits = self.ui.tableWidget.item(row, 4).text()
        decision_jury = self.ui.tableWidget.item(row, 5).text()

        # Ouvrir une boîte de dialogue pour choisir le chemin de sauvegarde du PDF
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_path, _ = QFileDialog.getSaveFileName(self, "Save PDF", "", "PDF Files (*.pdf);;All Files (*)", options=options)
        if not file_path:
            return  # Annuler si aucun fichier n'est choisi

        if not file_path.endswith('.pdf'):
            file_path += '.pdf'

        c = canvas.Canvas(file_path, pagesize=letter)
        width, height = letter

        # Définir les données du tableau à exporter
        data = [
            ["Nom de l'étudiant", "Unité d'enseignement", "Note", "Crédit(en %)", "Décision du jury"],
            [nom_etudiant, unite_enseignement, note_finale, pourcentage_credits, decision_jury]
        ]

        # Créer le tableau
        table = Table(data, colWidths=[1.5*inch]*5)  # Ajuster la largeur des colonnes

        # Définir le style du tableau
        style = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ])
        table.setStyle(style)

        # Dessiner le tableau sur le canvas
        table.wrapOn(c, width, height)
        table.drawOn(c, 50, height - 100)

        # Sauvegarder le PDF
        c.save()

        QMessageBox.information(self, "Succès", "Les données ont été exportées en PDF avec succès!")
############################################POUR LA PAGE RELEVE######################################
############################################POUR #####################################

############################################POUR LA PAGE RELEVE######################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
