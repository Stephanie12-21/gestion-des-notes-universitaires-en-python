# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ajoutNotes.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDialog,
    QFrame, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(551, 440)
        Dialog.setMinimumSize(QSize(551, 440))
        Dialog.setMaximumSize(QSize(551, 440))
        self.verticalLayout_3 = QVBoxLayout(Dialog)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(551, 440))
        self.frame.setMaximumSize(QSize(551, 440))
        self.frame.setStyleSheet(u"border-radius:10px; \n"
"background-color: #06070a ;\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_9 = QSpacerItem(145, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_9)

        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(211, 31))
        self.label_2.setMaximumSize(QSize(211, 31))
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: #63C8DC;")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.horizontalSpacer_10 = QSpacerItem(145, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_10)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.verticalSpacer = QSpacerItem(20, 26, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.etudiantComboBox = QComboBox(self.frame)
        self.etudiantComboBox.addItem("")
        self.etudiantComboBox.setObjectName(u"etudiantComboBox")
        self.etudiantComboBox.setMinimumSize(QSize(520, 41))
        self.etudiantComboBox.setMaximumSize(QSize(520, 41))
        font1 = QFont()
        font1.setPointSize(10)
        self.etudiantComboBox.setFont(font1)
        self.etudiantComboBox.setStyleSheet(u"color: #63C8DC;\n"
"background-color:#EBE9FC;\n"
"border-radius:10px;")

        self.verticalLayout.addWidget(self.etudiantComboBox)

        self.elemCfComboBox = QComboBox(self.frame)
        self.elemCfComboBox.addItem("")
        self.elemCfComboBox.setObjectName(u"elemCfComboBox")
        self.elemCfComboBox.setMinimumSize(QSize(520, 41))
        self.elemCfComboBox.setMaximumSize(QSize(520, 41))
        self.elemCfComboBox.setFont(font1)
        self.elemCfComboBox.setStyleSheet(u"color: #63C8DC;\n"
"background-color:#EBE9FC;\n"
"border-radius:10px;")

        self.verticalLayout.addWidget(self.elemCfComboBox)

        self.noteLineEdit = QLineEdit(self.frame)
        self.noteLineEdit.setObjectName(u"noteLineEdit")
        self.noteLineEdit.setMinimumSize(QSize(520, 41))
        self.noteLineEdit.setMaximumSize(QSize(520, 41))
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(False)
        self.noteLineEdit.setFont(font2)
        self.noteLineEdit.setStyleSheet(u"color: #63C8DC;\n"
"background-color:#EBE9FC;\n"
"border-radius:10px;")

        self.verticalLayout.addWidget(self.noteLineEdit)

        self.sessionComboBox = QComboBox(self.frame)
        self.sessionComboBox.addItem("")
        self.sessionComboBox.addItem("")
        self.sessionComboBox.addItem("")
        self.sessionComboBox.setObjectName(u"sessionComboBox")
        self.sessionComboBox.setMinimumSize(QSize(520, 41))
        self.sessionComboBox.setMaximumSize(QSize(520, 41))
        self.sessionComboBox.setFont(font1)
        self.sessionComboBox.setStyleSheet(u"color: #63C8DC;\n"
"background-color:#EBE9FC;\n"
"border-radius:10px;")

        self.verticalLayout.addWidget(self.sessionComboBox)

        self.semestreComboBox = QComboBox(self.frame)
        self.semestreComboBox.addItem("")
        self.semestreComboBox.addItem("")
        self.semestreComboBox.addItem("")
        self.semestreComboBox.addItem("")
        self.semestreComboBox.addItem("")
        self.semestreComboBox.addItem("")
        self.semestreComboBox.addItem("")
        self.semestreComboBox.addItem("")
        self.semestreComboBox.addItem("")
        self.semestreComboBox.addItem("")
        self.semestreComboBox.addItem("")
        self.semestreComboBox.setObjectName(u"semestreComboBox")
        self.semestreComboBox.setMinimumSize(QSize(520, 41))
        self.semestreComboBox.setMaximumSize(QSize(520, 41))
        self.semestreComboBox.setFont(font1)
        self.semestreComboBox.setStyleSheet(u"color: #63C8DC;\n"
"background-color:#EBE9FC;\n"
"border-radius:10px;")

        self.verticalLayout.addWidget(self.semestreComboBox)

        self.dateEdit = QDateEdit(self.frame)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setMinimumSize(QSize(520, 41))
        self.dateEdit.setMaximumSize(QSize(520, 41))
        self.dateEdit.setFont(font1)
        self.dateEdit.setStyleSheet(u"color: #63C8DC;\n"
"background-color:#EBE9FC;\n"
"border-radius:10px;")

        self.verticalLayout.addWidget(self.dateEdit)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 26, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 11, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer)

        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_7.setSpacing(20)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.saveBtn = QPushButton(self.frame_6)
        self.saveBtn.setObjectName(u"saveBtn")
        self.saveBtn.setMinimumSize(QSize(120, 50))
        self.saveBtn.setMaximumSize(QSize(120, 50))
        self.saveBtn.setFont(font1)
        self.saveBtn.setStyleSheet(u"\n"
"QPushButton {\n"
"color: #63C8DC;\n"
"background-color:#EBE9FC;\n"
"border-radius:10px;\n"
"border: 1px solid #63C8DC;\n"
"}\n"
"QPushButton::hover {\n"
"color: #63C8DC;\n"
"background-color: #06070a ;\n"
"border-radius:10px;\n"
"}")

        self.horizontalLayout_7.addWidget(self.saveBtn)

        self.cancelBtn = QPushButton(self.frame_6)
        self.cancelBtn.setObjectName(u"cancelBtn")
        self.cancelBtn.setMinimumSize(QSize(120, 50))
        self.cancelBtn.setMaximumSize(QSize(120, 50))
        font3 = QFont()
        font3.setPointSize(10)
        font3.setUnderline(False)
        self.cancelBtn.setFont(font3)
        self.cancelBtn.setStyleSheet(u"QPushButton {\n"
"color: #63C8DC;\n"
"background-color: #06070a ;\n"
"border-radius:10px;\n"
"border: 1px solid #63C8DC;\n"
"}\n"
"")

        self.horizontalLayout_7.addWidget(self.cancelBtn)


        self.horizontalLayout_8.addWidget(self.frame_6)


        self.verticalLayout_2.addWidget(self.frame_5)


        self.verticalLayout_3.addWidget(self.frame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Nouvelle note", None))
        self.etudiantComboBox.setItemText(0, QCoreApplication.translate("Dialog", u"Choisir l'\u00e9tudiant en question", None))

        self.elemCfComboBox.setItemText(0, QCoreApplication.translate("Dialog", u"Choisir l'\u00e9l\u00e9ment constitutif concern\u00e9", None))

        self.noteLineEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"Entrer la note obtenue", None))
        self.sessionComboBox.setItemText(0, QCoreApplication.translate("Dialog", u"Choisir la session de l'examen", None))
        self.sessionComboBox.setItemText(1, QCoreApplication.translate("Dialog", u"session normale ", None))
        self.sessionComboBox.setItemText(2, QCoreApplication.translate("Dialog", u"rattrapage", None))

        self.semestreComboBox.setItemText(0, QCoreApplication.translate("Dialog", u"Choisir le semestre", None))
        self.semestreComboBox.setItemText(1, QCoreApplication.translate("Dialog", u"Semestre1", None))
        self.semestreComboBox.setItemText(2, QCoreApplication.translate("Dialog", u"Semestre 2", None))
        self.semestreComboBox.setItemText(3, QCoreApplication.translate("Dialog", u"Semestre 3", None))
        self.semestreComboBox.setItemText(4, QCoreApplication.translate("Dialog", u"Semestre 4", None))
        self.semestreComboBox.setItemText(5, QCoreApplication.translate("Dialog", u"Semestre 5", None))
        self.semestreComboBox.setItemText(6, QCoreApplication.translate("Dialog", u"Semestre 6", None))
        self.semestreComboBox.setItemText(7, QCoreApplication.translate("Dialog", u"Semestre 7", None))
        self.semestreComboBox.setItemText(8, QCoreApplication.translate("Dialog", u"Semestre 8", None))
        self.semestreComboBox.setItemText(9, QCoreApplication.translate("Dialog", u"Semestre 9", None))
        self.semestreComboBox.setItemText(10, QCoreApplication.translate("Dialog", u"Semestre 10", None))

        self.saveBtn.setText(QCoreApplication.translate("Dialog", u"Enregistrer", None))
        self.cancelBtn.setText(QCoreApplication.translate("Dialog", u"Annuler", None))
    # retranslateUi

