# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'modifProf.ui'
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
        Dialog.resize(574, 598)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"border-radius:10px; \n"
"background-color: #06070a ;\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame)
        self.verticalLayout_7.setSpacing(7)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_7)

        self.label = QLabel(self.frame_2)
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

        self.horizontalSpacer_2 = QSpacerItem(157, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_7.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.niveauComboBox = QComboBox(self.frame_3)
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
        self.niveauComboBox.setStyleSheet(u"color: #63C8DC;\n"
"background-color:#EBE9FC;\n"
"border-radius:10px;")

        self.horizontalLayout_6.addWidget(self.niveauComboBox)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_8)


        self.verticalLayout_7.addWidget(self.frame_3)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(11, -1, 11, -1)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(181, 31))
        self.label_2.setMaximumSize(QSize(181, 31))
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: #63C8DC;")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.nomLineEdit = QLineEdit(self.frame)
        self.nomLineEdit.setObjectName(u"nomLineEdit")
        self.nomLineEdit.setMinimumSize(QSize(520, 41))
        self.nomLineEdit.setMaximumSize(QSize(520, 41))
        font2 = QFont()
        font2.setPointSize(9)
        self.nomLineEdit.setFont(font2)
        self.nomLineEdit.setStyleSheet(u"color: #63C8DC;\n"
"background-color:#EBE9FC;\n"
"border-radius:10px;")

        self.verticalLayout_2.addWidget(self.nomLineEdit)


        self.verticalLayout_6.addLayout(self.verticalLayout_2)

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

        self.numTelLineEdit = QLineEdit(self.frame)
        self.numTelLineEdit.setObjectName(u"numTelLineEdit")
        self.numTelLineEdit.setMinimumSize(QSize(520, 41))
        self.numTelLineEdit.setMaximumSize(QSize(520, 41))
        self.numTelLineEdit.setFont(font2)
        self.numTelLineEdit.setStyleSheet(u"color: #63C8DC;\n"
"background-color:#EBE9FC;\n"
"border-radius:10px;")

        self.verticalLayout_3.addWidget(self.numTelLineEdit)


        self.verticalLayout_6.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(181, 31))
        self.label_4.setMaximumSize(QSize(181, 31))
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"color: #63C8DC;")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.emailLineEdit = QLineEdit(self.frame)
        self.emailLineEdit.setObjectName(u"emailLineEdit")
        self.emailLineEdit.setMinimumSize(QSize(461, 41))
        self.emailLineEdit.setMaximumSize(QSize(520, 41))
        self.emailLineEdit.setFont(font2)
        self.emailLineEdit.setStyleSheet(u"color: #63C8DC;\n"
"background-color:#EBE9FC;\n"
"border-radius:10px;")

        self.verticalLayout_4.addWidget(self.emailLineEdit)


        self.verticalLayout_6.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(181, 31))
        self.label_5.setMaximumSize(QSize(181, 31))
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"color: #63C8DC;")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_6)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)

        self.adresseLineEdit = QLineEdit(self.frame)
        self.adresseLineEdit.setObjectName(u"adresseLineEdit")
        self.adresseLineEdit.setMinimumSize(QSize(461, 41))
        self.adresseLineEdit.setMaximumSize(QSize(520, 41))
        self.adresseLineEdit.setFont(font2)
        self.adresseLineEdit.setStyleSheet(u"color: #63C8DC;\n"
"background-color:#EBE9FC;\n"
"border-radius:10px;")

        self.verticalLayout_5.addWidget(self.adresseLineEdit)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)


        self.verticalLayout_7.addLayout(self.verticalLayout_6)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 11, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer)

        self.frame_4 = QFrame(self.frame_5)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_7.setSpacing(20)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.saveBtn = QPushButton(self.frame_4)
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

        self.cancelBtn = QPushButton(self.frame_4)
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


        self.horizontalLayout_8.addWidget(self.frame_4)


        self.verticalLayout_7.addWidget(self.frame_5)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Modification", None))
        self.niveauComboBox.setItemText(0, QCoreApplication.translate("Dialog", u"Choisir le grade", None))
        self.niveauComboBox.setItemText(1, QCoreApplication.translate("Dialog", u"Enseignant vacataire", None))
        self.niveauComboBox.setItemText(2, QCoreApplication.translate("Dialog", u"Enseignant chercheur", None))
        self.niveauComboBox.setItemText(3, QCoreApplication.translate("Dialog", u"Docteur", None))
        self.niveauComboBox.setItemText(4, QCoreApplication.translate("Dialog", u"Professeur", None))
        self.niveauComboBox.setItemText(5, QCoreApplication.translate("Dialog", u"HDR", None))

        self.label_2.setText(QCoreApplication.translate("Dialog", u"Nom complet:", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Num\u00e9ro de t\u00e9l\u00e9phone:", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Email:", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Adresse exacte:", None))
        self.adresseLineEdit.setText("")
        self.saveBtn.setText(QCoreApplication.translate("Dialog", u"Modifer", None))
        self.cancelBtn.setText(QCoreApplication.translate("Dialog", u"Annuler", None))
    # retranslateUi

