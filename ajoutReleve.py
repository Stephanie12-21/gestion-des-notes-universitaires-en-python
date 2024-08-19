# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ajoutReleve.ui'
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
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_ReleveDialog(object):
    def setupUi(self, ReleveDialog):
        if not ReleveDialog.objectName():
            ReleveDialog.setObjectName(u"ReleveDialog")
        ReleveDialog.resize(550, 367)
        ReleveDialog.setMinimumSize(QSize(550, 367))
        ReleveDialog.setMaximumSize(QSize(550, 367))
        self.verticalLayout = QVBoxLayout(ReleveDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(ReleveDialog)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 0))
        self.frame.setMaximumSize(QSize(16777215, 16777215))
        self.frame.setStyleSheet(u"border-radius:10px; \n"
"background-color:#303030;\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(152, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: #63C8DC;")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(151, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addWidget(self.frame_2)

        self.verticalSpacer = QSpacerItem(20, 11, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.niveauComboBox = QComboBox(self.frame_4)
        self.niveauComboBox.addItem("")
        self.niveauComboBox.addItem("")
        self.niveauComboBox.addItem("")
        self.niveauComboBox.addItem("")
        self.niveauComboBox.addItem("")
        self.niveauComboBox.addItem("")
        self.niveauComboBox.setObjectName(u"niveauComboBox")
        self.niveauComboBox.setMinimumSize(QSize(151, 41))
        self.niveauComboBox.setMaximumSize(QSize(151, 41))
        font1 = QFont()
        font1.setPointSize(10)
        self.niveauComboBox.setFont(font1)
        self.niveauComboBox.setStyleSheet(u"color: rgb(83, 177, 220);\n"
"border:1px solid #63C8DC;")

        self.horizontalLayout_2.addWidget(self.niveauComboBox)

        self.mentionComboBox = QComboBox(self.frame_4)
        self.mentionComboBox.addItem("")
        self.mentionComboBox.addItem("")
        self.mentionComboBox.addItem("")
        self.mentionComboBox.addItem("")
        self.mentionComboBox.addItem("")
        self.mentionComboBox.addItem("")
        self.mentionComboBox.addItem("")
        self.mentionComboBox.setObjectName(u"mentionComboBox")
        self.mentionComboBox.setMinimumSize(QSize(170, 41))
        self.mentionComboBox.setMaximumSize(QSize(170, 41))
        self.mentionComboBox.setFont(font1)
        self.mentionComboBox.setStyleSheet(u"color: rgb(83, 177, 220);\n"
"border:1px solid #63C8DC;\n"
"")

        self.horizontalLayout_2.addWidget(self.mentionComboBox)

        self.horizontalSpacer_4 = QSpacerItem(182, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)


        self.verticalLayout_3.addWidget(self.frame_4)

        self.verticalSpacer_3 = QSpacerItem(20, 12, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setSpacing(7)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.etudiantComboBox = QComboBox(self.frame_3)
        self.etudiantComboBox.addItem("")
        self.etudiantComboBox.setObjectName(u"etudiantComboBox")
        self.etudiantComboBox.setMinimumSize(QSize(520, 41))
        self.etudiantComboBox.setMaximumSize(QSize(520, 41))
        self.etudiantComboBox.setFont(font1)
        self.etudiantComboBox.setStyleSheet(u"color: rgb(83, 177, 220);\n"
"border:1px solid #63C8DC;")

        self.verticalLayout_2.addWidget(self.etudiantComboBox)

        self.uniteComboBox = QComboBox(self.frame_3)
        self.uniteComboBox.addItem("")
        self.uniteComboBox.setObjectName(u"uniteComboBox")
        self.uniteComboBox.setMinimumSize(QSize(520, 41))
        self.uniteComboBox.setMaximumSize(QSize(520, 41))
        self.uniteComboBox.setFont(font1)
        self.uniteComboBox.setStyleSheet(u"color: rgb(83, 177, 220);\n"
"border:1px solid #63C8DC;")

        self.verticalLayout_2.addWidget(self.uniteComboBox)


        self.verticalLayout_3.addWidget(self.frame_3)

        self.verticalSpacer_4 = QSpacerItem(20, 11, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_3)

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
"color: rgb(48, 48, 48);\n"
"	background-color: rgb(83, 177, 220);\n"
"border-radius:10px;\n"
"border: 1px solid #63C8DC;\n"
"}\n"
"")

        self.horizontalLayout_7.addWidget(self.saveBtn)

        self.cancelBtn = QPushButton(self.frame_6)
        self.cancelBtn.setObjectName(u"cancelBtn")
        self.cancelBtn.setMinimumSize(QSize(120, 50))
        self.cancelBtn.setMaximumSize(QSize(120, 50))
        self.cancelBtn.setFont(font1)
        self.cancelBtn.setStyleSheet(u"QPushButton {\n"
"color: #63C8DC;\n"
"background-color: #303030;\n"
"border-radius:10px;\n"
"border: 1px solid #63C8DC;\n"
"}\n"
"")

        self.horizontalLayout_7.addWidget(self.cancelBtn)


        self.horizontalLayout_8.addWidget(self.frame_6)


        self.verticalLayout_3.addWidget(self.frame_5)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(ReleveDialog)

        QMetaObject.connectSlotsByName(ReleveDialog)
    # setupUi

    def retranslateUi(self, ReleveDialog):
        ReleveDialog.setWindowTitle(QCoreApplication.translate("ReleveDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("ReleveDialog", u"Nouveau relev\u00e9", None))
        self.niveauComboBox.setItemText(0, QCoreApplication.translate("ReleveDialog", u"Choisir le niveau", None))
        self.niveauComboBox.setItemText(1, QCoreApplication.translate("ReleveDialog", u"L1", None))
        self.niveauComboBox.setItemText(2, QCoreApplication.translate("ReleveDialog", u"L2", None))
        self.niveauComboBox.setItemText(3, QCoreApplication.translate("ReleveDialog", u"L3", None))
        self.niveauComboBox.setItemText(4, QCoreApplication.translate("ReleveDialog", u"M1", None))
        self.niveauComboBox.setItemText(5, QCoreApplication.translate("ReleveDialog", u"M2", None))

        self.mentionComboBox.setItemText(0, QCoreApplication.translate("ReleveDialog", u"Choisir la mention", None))
        self.mentionComboBox.setItemText(1, QCoreApplication.translate("ReleveDialog", u"Informatique g\u00e9n\u00e9rale", None))
        self.mentionComboBox.setItemText(2, QCoreApplication.translate("ReleveDialog", u"Syst\u00e8me et r\u00e9seaux", None))
        self.mentionComboBox.setItemText(3, QCoreApplication.translate("ReleveDialog", u"G\u00e9nie logiciel", None))
        self.mentionComboBox.setItemText(4, QCoreApplication.translate("ReleveDialog", u"Syst\u00e8mes embarqu\u00e9s", None))
        self.mentionComboBox.setItemText(5, QCoreApplication.translate("ReleveDialog", u"Cybers\u00e9curit\u00e9", None))
        self.mentionComboBox.setItemText(6, QCoreApplication.translate("ReleveDialog", u"Intelligence Artificielle", None))

        self.etudiantComboBox.setItemText(0, QCoreApplication.translate("ReleveDialog", u"Choisir l'\u00e9tudiant en question", None))

        self.uniteComboBox.setItemText(0, QCoreApplication.translate("ReleveDialog", u"Choisir l'unit\u00e9 d'enseignement concern\u00e9", None))

        self.saveBtn.setText(QCoreApplication.translate("ReleveDialog", u"Cr\u00e9er", None))
        self.cancelBtn.setText(QCoreApplication.translate("ReleveDialog", u"Annuler", None))
    # retranslateUi

