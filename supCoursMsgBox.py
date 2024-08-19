# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'supCoursMsgBox.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_CoursDialog(object):
    def setupUi(self, CoursDialog):
        if not CoursDialog.objectName():
            CoursDialog.setObjectName(u"CoursDialog")
        CoursDialog.resize(441, 221)
        CoursDialog.setMinimumSize(QSize(441, 221))
        CoursDialog.setMaximumSize(QSize(443, 221))
        CoursDialog.setStyleSheet(u"border-radius:10px; \n"
"background-color:#303030;\n"
"")
        self.verticalLayout_3 = QVBoxLayout(CoursDialog)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_2 = QFrame(CoursDialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(421, 61))
        self.frame_2.setMaximumSize(QSize(421, 61))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: #63C8DC;")

        self.verticalLayout_2.addWidget(self.label)


        self.verticalLayout_3.addWidget(self.frame_2)

        self.frame = QFrame(CoursDialog)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(421, 131))
        self.frame.setMaximumSize(QSize(421, 131))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.supBtn = QPushButton(self.frame)
        self.supBtn.setObjectName(u"supBtn")
        self.supBtn.setMinimumSize(QSize(120, 50))
        self.supBtn.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setPointSize(10)
        self.supBtn.setFont(font1)
        self.supBtn.setStyleSheet(u"\n"
"QPushButton {\n"
"color: rgb(48, 48, 48);\n"
"	background-color: rgb(83, 177, 220);\n"
"border-radius:10px;\n"
"border: 1px solid #63C8DC;\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.supBtn)

        self.cancelBtn = QPushButton(self.frame)
        self.cancelBtn.setObjectName(u"cancelBtn")
        self.cancelBtn.setMinimumSize(QSize(120, 50))
        self.cancelBtn.setMaximumSize(QSize(16777215, 16777215))
        self.cancelBtn.setFont(font1)
        self.cancelBtn.setStyleSheet(u"QPushButton {\n"
"color: #63C8DC;\n"
"background-color: #303030;\n"
"border-radius:10px;\n"
"border: 1px solid #63C8DC;\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.cancelBtn)


        self.verticalLayout_3.addWidget(self.frame)


        self.retranslateUi(CoursDialog)

        QMetaObject.connectSlotsByName(CoursDialog)
    # setupUi

    def retranslateUi(self, CoursDialog):
        CoursDialog.setWindowTitle(QCoreApplication.translate("CoursDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("CoursDialog", u"Etes-vous s\u00fbr de vouloir supprimer ces donn\u00e9es?", None))
        self.supBtn.setText(QCoreApplication.translate("CoursDialog", u"Supprimer", None))
        self.cancelBtn.setText(QCoreApplication.translate("CoursDialog", u"Annuler", None))
    # retranslateUi

