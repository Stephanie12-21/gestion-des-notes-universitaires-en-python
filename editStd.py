# editStd.py
from PySide6.QtWidgets import QMessageBox

def edit_student(idEtd):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setText(f"Editing student with ID: {idEtd}")
    msg.setWindowTitle("Edit Student")
    msg.exec_()
