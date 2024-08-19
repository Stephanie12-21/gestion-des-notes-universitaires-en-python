# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'supMessageBox.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(464, 222)
        Dialog.setStyleSheet(u"QPushButton {\n"
"border-radius: 15px;\n"
"border: 2px solid red;\n"
"\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.frame_4 = QFrame(Dialog)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_7.setSpacing(20)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.supBtn = QPushButton(self.frame_4)
        self.supBtn.setObjectName(u"supBtn")
        self.supBtn.setMinimumSize(QSize(120, 50))
        self.supBtn.setMaximumSize(QSize(120, 50))
        font = QFont()
        font.setPointSize(10)
        self.supBtn.setFont(font)
        self.supBtn.setStyleSheet(u"")

        self.horizontalLayout_7.addWidget(self.supBtn)

        self.cancelBtn = QPushButton(self.frame_4)
        self.cancelBtn.setObjectName(u"cancelBtn")
        self.cancelBtn.setMinimumSize(QSize(120, 50))
        self.cancelBtn.setMaximumSize(QSize(120, 50))
        self.cancelBtn.setFont(font)

        self.horizontalLayout_7.addWidget(self.cancelBtn)


        self.verticalLayout.addWidget(self.frame_4)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Dialog)
        self.cancelBtn.toggled.connect(Dialog.close)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Etes-vous s\u00fbr de vouloir supprimer ces donn\u00e9es?</span></p></body></html>", None))
        self.supBtn.setText(QCoreApplication.translate("Dialog", u"Supprimer", None))
        self.cancelBtn.setText(QCoreApplication.translate("Dialog", u"Annuler", None))
    # retranslateUi

