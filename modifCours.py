# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'modifCours.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(550, 593)
        Dialog.setMinimumSize(QSize(550, 593))
        Dialog.setMaximumSize(QSize(550, 593))
        self.verticalLayout_6 = QVBoxLayout(Dialog)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"border-radius:10px; \n"
"background-color: #06070a ;\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 0))
        self.frame_3.setMaximumSize(QSize(16777215, 50))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_7)

        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(211, 31))
        self.label.setMaximumSize(QSize(211, 31))
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: #63C8DC;")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer_8 = QSpacerItem(151, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_8)


        self.verticalLayout_4.addWidget(self.frame_3)

        self.verticalSpacer_3 = QSpacerItem(20, 21, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(7)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(181, 31))
        self.label_2.setMaximumSize(QSize(181, 31))
        font1 = QFont()
        font1.setPointSize(10)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: #63C8DC;")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.uniteLineEdit = QLineEdit(self.frame)
        self.uniteLineEdit.setObjectName(u"uniteLineEdit")
        self.uniteLineEdit.setMinimumSize(QSize(520, 41))
        self.uniteLineEdit.setMaximumSize(QSize(520, 41))
        font2 = QFont()
        font2.setPointSize(9)
        self.uniteLineEdit.setFont(font2)
        self.uniteLineEdit.setStyleSheet(u"color: #63C8DC;\n"
"background-color:#EBE9FC;\n"
"border-radius:10px;")

        self.verticalLayout_2.addWidget(self.uniteLineEdit)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(181, 31))
        self.label_3.setMaximumSize(QSize(181, 31))
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"color: #63C8DC;")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.elemCLineEdit = QLineEdit(self.frame)
        self.elemCLineEdit.setObjectName(u"elemCLineEdit")
        self.elemCLineEdit.setMinimumSize(QSize(520, 41))
        self.elemCLineEdit.setMaximumSize(QSize(520, 41))
        self.elemCLineEdit.setFont(font2)
        self.elemCLineEdit.setStyleSheet(u"color: #63C8DC;\n"
"background-color:#EBE9FC;\n"
"border-radius:10px;")

        self.verticalLayout_3.addWidget(self.elemCLineEdit)


        self.verticalLayout.addLayout(self.verticalLayout_3)

        self.profComboBox = QComboBox(self.frame)
        self.profComboBox.addItem("")
        self.profComboBox.setObjectName(u"profComboBox")
        self.profComboBox.setMinimumSize(QSize(520, 41))
        self.profComboBox.setMaximumSize(QSize(520, 41))
        self.profComboBox.setFont(font1)
        self.profComboBox.setStyleSheet(u"color: #63C8DC;\n"
"background-color:#EBE9FC;\n"
"border-radius:10px;")

        self.verticalLayout.addWidget(self.profComboBox)

        self.mentionComboBox = QComboBox(self.frame)
        self.mentionComboBox.addItem("")
        self.mentionComboBox.addItem("")
        self.mentionComboBox.addItem("")
        self.mentionComboBox.addItem("")
        self.mentionComboBox.addItem("")
        self.mentionComboBox.addItem("")
        self.mentionComboBox.addItem("")
        self.mentionComboBox.setObjectName(u"mentionComboBox")
        self.mentionComboBox.setMinimumSize(QSize(520, 41))
        self.mentionComboBox.setMaximumSize(QSize(520, 41))
        self.mentionComboBox.setFont(font1)
        self.mentionComboBox.setStyleSheet(u"color: #63C8DC;\n"
"background-color:#EBE9FC;\n"
"border-radius:10px;")

        self.verticalLayout.addWidget(self.mentionComboBox)

        self.niveauComboBox = QComboBox(self.frame)
        self.niveauComboBox.addItem("")
        self.niveauComboBox.addItem("")
        self.niveauComboBox.addItem("")
        self.niveauComboBox.addItem("")
        self.niveauComboBox.addItem("")
        self.niveauComboBox.addItem("")
        self.niveauComboBox.setObjectName(u"niveauComboBox")
        self.niveauComboBox.setMinimumSize(QSize(520, 41))
        self.niveauComboBox.setMaximumSize(QSize(520, 41))
        self.niveauComboBox.setFont(font1)
        self.niveauComboBox.setStyleSheet(u"color: #63C8DC;\n"
"background-color:#EBE9FC;\n"
"border-radius:10px;")

        self.verticalLayout.addWidget(self.niveauComboBox)

        self.semestreComboBox = QComboBox(self.frame)
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

        self.creditComboBox = QComboBox(self.frame)
        self.creditComboBox.addItem("")
        self.creditComboBox.addItem("")
        self.creditComboBox.addItem("")
        self.creditComboBox.addItem("")
        self.creditComboBox.addItem("")
        self.creditComboBox.setObjectName(u"creditComboBox")
        self.creditComboBox.setMinimumSize(QSize(520, 41))
        self.creditComboBox.setMaximumSize(QSize(520, 41))
        self.creditComboBox.setFont(font1)
        self.creditComboBox.setStyleSheet(u"color: #63C8DC;\n"
"background-color:#EBE9FC;\n"
"border-radius:10px;")

        self.verticalLayout.addWidget(self.creditComboBox)


        self.verticalLayout_4.addLayout(self.verticalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(16777215, 100))
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
        self.cancelBtn.setFont(font1)
        self.cancelBtn.setStyleSheet(u"QPushButton {\n"
"color: #63C8DC;\n"
"background-color: #06070a ;\n"
"border-radius:10px;\n"
"border: 1px solid #63C8DC;\n"
"}\n"
"")

        self.horizontalLayout_7.addWidget(self.cancelBtn)


        self.horizontalLayout_8.addWidget(self.frame_6)


        self.verticalLayout_4.addWidget(self.frame_5)


        self.verticalLayout_6.addWidget(self.frame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Modification ", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Unit\u00e9 d'enseignement:", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"El\u00e9ment constitutif:", None))
        self.profComboBox.setItemText(0, QCoreApplication.translate("Dialog", u"Enseignant en charge", None))

        self.mentionComboBox.setItemText(0, QCoreApplication.translate("Dialog", u"Choisir la mention", None))
        self.mentionComboBox.setItemText(1, QCoreApplication.translate("Dialog", u"Informatique g\u00e9n\u00e9rale", None))
        self.mentionComboBox.setItemText(2, QCoreApplication.translate("Dialog", u"Syst\u00e8me et R\u00e9seaux", None))
        self.mentionComboBox.setItemText(3, QCoreApplication.translate("Dialog", u"G\u00e9nie logiciel", None))
        self.mentionComboBox.setItemText(4, QCoreApplication.translate("Dialog", u"Syst\u00e8mes embarqu\u00e9s", None))
        self.mentionComboBox.setItemText(5, QCoreApplication.translate("Dialog", u"Cybers\u00e9curit\u00e9", None))
        self.mentionComboBox.setItemText(6, QCoreApplication.translate("Dialog", u"Intelligence Artificielle", None))

        self.niveauComboBox.setItemText(0, QCoreApplication.translate("Dialog", u"Choisir le niveau", None))
        self.niveauComboBox.setItemText(1, QCoreApplication.translate("Dialog", u"L1", None))
        self.niveauComboBox.setItemText(2, QCoreApplication.translate("Dialog", u"L2", None))
        self.niveauComboBox.setItemText(3, QCoreApplication.translate("Dialog", u"L3", None))
        self.niveauComboBox.setItemText(4, QCoreApplication.translate("Dialog", u"M1", None))
        self.niveauComboBox.setItemText(5, QCoreApplication.translate("Dialog", u"M2", None))

        self.semestreComboBox.setItemText(0, QCoreApplication.translate("Dialog", u"Choisir le semestre", None))
        self.semestreComboBox.setItemText(1, QCoreApplication.translate("Dialog", u"Semestre1", None))
        self.semestreComboBox.setItemText(2, QCoreApplication.translate("Dialog", u"Semestre 2", None))

        self.creditComboBox.setItemText(0, QCoreApplication.translate("Dialog", u"Choisir le cr\u00e9dit", None))
        self.creditComboBox.setItemText(1, QCoreApplication.translate("Dialog", u"1", None))
        self.creditComboBox.setItemText(2, QCoreApplication.translate("Dialog", u"2", None))
        self.creditComboBox.setItemText(3, QCoreApplication.translate("Dialog", u"3", None))
        self.creditComboBox.setItemText(4, QCoreApplication.translate("Dialog", u"4", None))

        self.saveBtn.setText(QCoreApplication.translate("Dialog", u"Enregistrer", None))
        self.cancelBtn.setText(QCoreApplication.translate("Dialog", u"Annuler", None))
    # retranslateUi

