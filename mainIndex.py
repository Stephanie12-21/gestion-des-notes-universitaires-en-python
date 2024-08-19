# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainIndex.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLCDNumber, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
import ressources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1398, 786)
        MainWindow.setMinimumSize(QSize(1280, 680))
        font = QFont()
        font.setPointSize(9)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: #EBE9FC;\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color:#EBE9FC;\n"
"")
        self.verticalLayout_46 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.verticalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color:#EBE9FC ;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(120, 0))
        self.widget.setMaximumSize(QSize(120, 16777215))
        self.widget.setStyleSheet(u"background-color:   #303030;\n"
"border-radius:10px;\n"
"\n"
"\n"
"")
        self.verticalLayout_11 = QVBoxLayout(self.widget)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_4 = QSpacerItem(13, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(80, 80))
        self.label.setMaximumSize(QSize(80, 80))
        self.label.setPixmap(QPixmap(u":/icons/education.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label)

        self.horizontalSpacer_3 = QSpacerItem(13, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.verticalLayout_11.addLayout(self.horizontalLayout_3)

        self.frame_7 = QFrame(self.widget)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_7)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(11, 20, 11, 11)
        self.frame_5 = QFrame(self.frame_7)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_5)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.dashBtn1 = QPushButton(self.frame_5)
        self.dashBtn1.setObjectName(u"dashBtn1")
        self.dashBtn1.setMinimumSize(QSize(70, 50))
        self.dashBtn1.setStyleSheet(u"QPushButton {\n"
"color: #63C8DC;\n"
"}\n"
"QPushButton::hover{\n"
"color: #63C8DC;\n"
"	background-color:#FBFBFE;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/icons8-dashboard-layout-96 (1).png", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/icons/icons8-dashboard-layout-96.png", QSize(), QIcon.Normal, QIcon.On)
        icon.addFile(u":/icons/icons8-dashboard-layout-96.png", QSize(), QIcon.Active, QIcon.On)
        icon.addFile(u":/icons/icons8-dashboard-layout-96.png", QSize(), QIcon.Selected, QIcon.On)
        self.dashBtn1.setIcon(icon)
        self.dashBtn1.setIconSize(QSize(30, 30))
        self.dashBtn1.setCheckable(True)
        self.dashBtn1.setAutoExclusive(True)

        self.verticalLayout_8.addWidget(self.dashBtn1)

        self.etdBtn1 = QPushButton(self.frame_5)
        self.etdBtn1.setObjectName(u"etdBtn1")
        self.etdBtn1.setMinimumSize(QSize(70, 50))
        self.etdBtn1.setStyleSheet(u"QPushButton {\n"
"color: #63C8DC;\n"
"}\n"
"QPushButton::hover{\n"
"color: #63C8DC;\n"
"	background-color:#FBFBFE;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons8-groupe-d'utilisateurs-64 (1).png", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/icons/icons8-groupe-d'utilisateurs-64.png", QSize(), QIcon.Normal, QIcon.On)
        icon1.addFile(u":/icons/icons8-groupe-d'utilisateurs-64.png", QSize(), QIcon.Active, QIcon.On)
        icon1.addFile(u":/icons/icons8-groupe-d'utilisateurs-64.png", QSize(), QIcon.Selected, QIcon.On)
        self.etdBtn1.setIcon(icon1)
        self.etdBtn1.setIconSize(QSize(35, 35))
        self.etdBtn1.setCheckable(True)
        self.etdBtn1.setAutoExclusive(True)

        self.verticalLayout_8.addWidget(self.etdBtn1)

        self.esgBtn1 = QPushButton(self.frame_5)
        self.esgBtn1.setObjectName(u"esgBtn1")
        self.esgBtn1.setMinimumSize(QSize(70, 50))
        self.esgBtn1.setStyleSheet(u"QPushButton {\n"
"color: #63C8DC;\n"
"}\n"
"QPushButton::hover{\n"
"color: #63C8DC;\n"
"	background-color:#FBFBFE;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons8-teacher-100.png", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u":/icons/icons8-teacher-100 (1).png", QSize(), QIcon.Normal, QIcon.On)
        icon2.addFile(u":/icons/icons8-teacher-100 (1).png", QSize(), QIcon.Active, QIcon.On)
        icon2.addFile(u":/icons/icons8-teacher-100 (1).png", QSize(), QIcon.Selected, QIcon.On)
        self.esgBtn1.setIcon(icon2)
        self.esgBtn1.setIconSize(QSize(35, 35))
        self.esgBtn1.setCheckable(True)
        self.esgBtn1.setAutoExclusive(True)

        self.verticalLayout_8.addWidget(self.esgBtn1)

        self.coursBtn1 = QPushButton(self.frame_5)
        self.coursBtn1.setObjectName(u"coursBtn1")
        self.coursBtn1.setMinimumSize(QSize(70, 50))
        self.coursBtn1.setStyleSheet(u"QPushButton {\n"
"color: #63C8DC;\n"
"}\n"
"QPushButton::hover{\n"
"color: #63C8DC;\n"
"	background-color:#FBFBFE;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons8-manuel-100.png", QSize(), QIcon.Normal, QIcon.Off)
        icon3.addFile(u":/icons/icons8-user-manual-100.png", QSize(), QIcon.Normal, QIcon.On)
        icon3.addFile(u":/icons/icons8-user-manual-100.png", QSize(), QIcon.Active, QIcon.On)
        icon3.addFile(u":/icons/icons8-user-manual-100.png", QSize(), QIcon.Selected, QIcon.On)
        self.coursBtn1.setIcon(icon3)
        self.coursBtn1.setIconSize(QSize(35, 35))
        self.coursBtn1.setCheckable(True)
        self.coursBtn1.setAutoExclusive(True)

        self.verticalLayout_8.addWidget(self.coursBtn1)

        self.notesBtn1 = QPushButton(self.frame_5)
        self.notesBtn1.setObjectName(u"notesBtn1")
        self.notesBtn1.setMinimumSize(QSize(70, 50))
        self.notesBtn1.setStyleSheet(u"QPushButton {\n"
"color: #63C8DC;\n"
"}\n"
"QPushButton::hover{\n"
"color: #63C8DC;\n"
"	background-color:#FBFBFE;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons8-notes-64 (1).png", QSize(), QIcon.Normal, QIcon.Off)
        icon4.addFile(u":/icons/icons8-notes-64.png", QSize(), QIcon.Normal, QIcon.On)
        icon4.addFile(u":/icons/icons8-notes-64.png", QSize(), QIcon.Active, QIcon.On)
        icon4.addFile(u":/icons/icons8-notes-64.png", QSize(), QIcon.Selected, QIcon.On)
        self.notesBtn1.setIcon(icon4)
        self.notesBtn1.setIconSize(QSize(35, 35))
        self.notesBtn1.setCheckable(True)
        self.notesBtn1.setAutoExclusive(True)

        self.verticalLayout_8.addWidget(self.notesBtn1)

        self.rlvBtn1 = QPushButton(self.frame_5)
        self.rlvBtn1.setObjectName(u"rlvBtn1")
        self.rlvBtn1.setMinimumSize(QSize(70, 50))
        self.rlvBtn1.setStyleSheet(u"QPushButton {\n"
"color: #63C8DC;\n"
"}\n"
"QPushButton::hover{\n"
"color: #63C8DC;\n"
"	background-color:#FBFBFE;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons8-fichier-important-64 (1).png", QSize(), QIcon.Normal, QIcon.Off)
        icon5.addFile(u":/icons/icons8-fichier-important-64.png", QSize(), QIcon.Normal, QIcon.On)
        icon5.addFile(u":/icons/icons8-fichier-important-64.png", QSize(), QIcon.Active, QIcon.On)
        icon5.addFile(u":/icons/icons8-fichier-important-64.png", QSize(), QIcon.Selected, QIcon.On)
        self.rlvBtn1.setIcon(icon5)
        self.rlvBtn1.setIconSize(QSize(35, 35))
        self.rlvBtn1.setCheckable(True)
        self.rlvBtn1.setAutoExclusive(True)

        self.verticalLayout_8.addWidget(self.rlvBtn1)


        self.verticalLayout_10.addWidget(self.frame_5)

        self.verticalSpacer_2 = QSpacerItem(20, 171, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_2)

        self.frame_6 = QFrame(self.frame_7)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_6)
        self.verticalLayout_9.setSpacing(7)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.prmtBtn1 = QPushButton(self.frame_6)
        self.prmtBtn1.setObjectName(u"prmtBtn1")
        self.prmtBtn1.setMinimumSize(QSize(70, 50))
        self.prmtBtn1.setStyleSheet(u"QPushButton {\n"
"color: #63C8DC;\n"
"}\n"
"QPushButton::hover{\n"
"color: #63C8DC;\n"
"	background-color:#FBFBFE;\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons8-settings-96.png", QSize(), QIcon.Normal, QIcon.Off)
        icon6.addFile(u":/icons/icons8-param\u00e8tres-96.png", QSize(), QIcon.Normal, QIcon.On)
        icon6.addFile(u":/icons/icons8-param\u00e8tres-96.png", QSize(), QIcon.Active, QIcon.On)
        icon6.addFile(u":/icons/icons8-param\u00e8tres-96.png", QSize(), QIcon.Selected, QIcon.On)
        self.prmtBtn1.setIcon(icon6)
        self.prmtBtn1.setIconSize(QSize(32, 32))
        self.prmtBtn1.setCheckable(True)
        self.prmtBtn1.setAutoExclusive(True)

        self.verticalLayout_9.addWidget(self.prmtBtn1)

        self.quitBtn1 = QPushButton(self.frame_6)
        self.quitBtn1.setObjectName(u"quitBtn1")
        self.quitBtn1.setMinimumSize(QSize(70, 50))
        self.quitBtn1.setStyleSheet(u"QPushButton {\n"
"color: #63C8DC;\n"
"}\n"
"QPushButton::hover{\n"
"color: #63C8DC;\n"
"	background-color:#FBFBFE;\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons8-quitter-96.png", QSize(), QIcon.Normal, QIcon.Off)
        icon7.addFile(u":/icons/icons8-login-96.png", QSize(), QIcon.Normal, QIcon.On)
        icon7.addFile(u":/icons/icons8-login-96.png", QSize(), QIcon.Active, QIcon.On)
        icon7.addFile(u":/icons/icons8-login-96.png", QSize(), QIcon.Selected, QIcon.On)
        self.quitBtn1.setIcon(icon7)
        self.quitBtn1.setIconSize(QSize(32, 32))
        self.quitBtn1.setCheckable(True)
        self.quitBtn1.setAutoExclusive(True)

        self.verticalLayout_9.addWidget(self.quitBtn1)


        self.verticalLayout_10.addWidget(self.frame_6)


        self.verticalLayout_11.addWidget(self.frame_7)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_3 = QWidget(self.frame)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(0, 51))
        self.widget_3.setMaximumSize(QSize(16777215, 51))
        self.widget_3.setStyleSheet(u"background-color: #303030 ;\n"
"border-radius :10px;")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.menuBtn = QPushButton(self.widget_3)
        self.menuBtn.setObjectName(u"menuBtn")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.menuBtn.setFont(font1)
        self.menuBtn.setStyleSheet(u"QPushButton {\n"
"color: #63C8DC;\n"
"}\n"
"QPushButton::hover{\n"
"color: #63C8DC;\n"
"	background-color:#FBFBFE;\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons8-menu-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menuBtn.setIcon(icon8)
        self.menuBtn.setIconSize(QSize(35, 35))
        self.menuBtn.setCheckable(True)
        self.menuBtn.setFlat(True)

        self.horizontalLayout_4.addWidget(self.menuBtn)

        self.horizontalSpacer_5 = QSpacerItem(946, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)


        self.verticalLayout_2.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.frame)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(0, 0))
        self.widget_4.setMaximumSize(QSize(16777215, 16777215))
        self.widget_4.setFont(font)
        self.widget_4.setStyleSheet(u"background-color:#EBE9FC;\n"
"border-radius:10px;")
        self.verticalLayout_13 = QVBoxLayout(self.widget_4)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.pageContainer = QStackedWidget(self.widget_4)
        self.pageContainer.setObjectName(u"pageContainer")
        self.pageDashboard = QWidget()
        self.pageDashboard.setObjectName(u"pageDashboard")
        self.verticalLayout_30 = QVBoxLayout(self.pageDashboard)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.frame_14 = QFrame(self.pageDashboard)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setStyleSheet(u"border-color: rgb(170, 0, 0);")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_14)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.frameGraphs_2 = QFrame(self.frame_14)
        self.frameGraphs_2.setObjectName(u"frameGraphs_2")
        self.frameGraphs_2.setMinimumSize(QSize(0, 181))
        self.frameGraphs_2.setMaximumSize(QSize(16777215, 181))
        self.frameGraphs_2.setStyleSheet(u"")
        self.frameGraphs_2.setFrameShape(QFrame.StyledPanel)
        self.frameGraphs_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frameGraphs_2)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_12 = QFrame(self.frameGraphs_2)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(0, 158))
        self.frame_12.setMaximumSize(QSize(16777215, 158))
        self.frame_12.setStyleSheet(u"background-color: #303030;\n"
"color : #63C8DC;")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_12)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.widget_11 = QWidget(self.frame_12)
        self.widget_11.setObjectName(u"widget_11")
        self.widget_11.setStyleSheet(u"")
        self.horizontalLayout_11 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalSpacer_21 = QSpacerItem(20, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_25.addItem(self.verticalSpacer_21)

        self.label_28 = QLabel(self.widget_11)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMaximumSize(QSize(74, 68))
        self.label_28.setPixmap(QPixmap(u":/icons/icons8-groupe-d'utilisateurs-64.png"))
        self.label_28.setScaledContents(True)

        self.verticalLayout_25.addWidget(self.label_28)

        self.verticalSpacer_22 = QSpacerItem(20, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_25.addItem(self.verticalSpacer_22)


        self.horizontalLayout_11.addLayout(self.verticalLayout_25)

        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.label_29 = QLabel(self.widget_11)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMinimumSize(QSize(70, 31))
        self.label_29.setMaximumSize(QSize(16777215, 31))
        font2 = QFont()
        font2.setPointSize(10)
        self.label_29.setFont(font2)
        self.label_29.setAlignment(Qt.AlignCenter)

        self.verticalLayout_26.addWidget(self.label_29)

        self.verticalSpacer_23 = QSpacerItem(20, 28, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_26.addItem(self.verticalSpacer_23)

        self.L_1_Number = QLCDNumber(self.widget_11)
        self.L_1_Number.setObjectName(u"L_1_Number")
        self.L_1_Number.setMinimumSize(QSize(0, 41))
        self.L_1_Number.setMaximumSize(QSize(16777215, 41))
        self.L_1_Number.setFont(font2)
        self.L_1_Number.setSegmentStyle(QLCDNumber.Flat)

        self.verticalLayout_26.addWidget(self.L_1_Number)


        self.horizontalLayout_11.addLayout(self.verticalLayout_26)


        self.verticalLayout_28.addWidget(self.widget_11)


        self.horizontalLayout_12.addWidget(self.frame_12)

        self.frame_11 = QFrame(self.frameGraphs_2)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(0, 158))
        self.frame_11.setMaximumSize(QSize(16777215, 158))
        self.frame_11.setStyleSheet(u"background-color:#303030;\n"
"color : #63C8DC;")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_11)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.widget_7 = QWidget(self.frame_11)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setStyleSheet(u"border-color: rgb(255, 255, 0);")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalSpacer_9 = QSpacerItem(20, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_19.addItem(self.verticalSpacer_9)

        self.label_20 = QLabel(self.widget_7)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMaximumSize(QSize(74, 68))
        self.label_20.setPixmap(QPixmap(u":/icons/icons8-groupe-d'utilisateurs-64.png"))
        self.label_20.setScaledContents(True)

        self.verticalLayout_19.addWidget(self.label_20)

        self.verticalSpacer_10 = QSpacerItem(20, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_19.addItem(self.verticalSpacer_10)


        self.horizontalLayout_5.addLayout(self.verticalLayout_19)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_21 = QLabel(self.widget_7)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(70, 31))
        self.label_21.setMaximumSize(QSize(16777215, 31))
        self.label_21.setFont(font2)
        self.label_21.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_21)

        self.verticalSpacer_11 = QSpacerItem(20, 28, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_11)

        self.l2Numer = QLCDNumber(self.widget_7)
        self.l2Numer.setObjectName(u"l2Numer")
        self.l2Numer.setMinimumSize(QSize(0, 41))
        self.l2Numer.setMaximumSize(QSize(16777215, 41))
        self.l2Numer.setFont(font2)
        self.l2Numer.setStyleSheet(u"border-color:#63C8DC;\n"
"")
        self.l2Numer.setSegmentStyle(QLCDNumber.Flat)

        self.verticalLayout_14.addWidget(self.l2Numer)


        self.horizontalLayout_5.addLayout(self.verticalLayout_14)


        self.verticalLayout_24.addWidget(self.widget_7)


        self.horizontalLayout_12.addWidget(self.frame_11)

        self.frame_8 = QFrame(self.frameGraphs_2)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(0, 158))
        self.frame_8.setMaximumSize(QSize(16777215, 158))
        self.frame_8.setStyleSheet(u"background-color:#303030;\n"
"color : #63C8DC;")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_8)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.widget_9 = QWidget(self.frame_8)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setStyleSheet(u"border-color: rgb(255, 255, 0);")
        self.horizontalLayout_9 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalSpacer_15 = QSpacerItem(20, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_21.addItem(self.verticalSpacer_15)

        self.label_24 = QLabel(self.widget_9)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMaximumSize(QSize(74, 68))
        self.label_24.setPixmap(QPixmap(u":/icons/icons8-groupe-d'utilisateurs-64.png"))
        self.label_24.setScaledContents(True)

        self.verticalLayout_21.addWidget(self.label_24)

        self.verticalSpacer_16 = QSpacerItem(20, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_21.addItem(self.verticalSpacer_16)


        self.horizontalLayout_9.addLayout(self.verticalLayout_21)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_25 = QLabel(self.widget_9)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMinimumSize(QSize(70, 31))
        self.label_25.setMaximumSize(QSize(16777215, 31))
        self.label_25.setFont(font2)
        self.label_25.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_25)

        self.verticalSpacer_17 = QSpacerItem(20, 28, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_16.addItem(self.verticalSpacer_17)

        self.l3Number = QLCDNumber(self.widget_9)
        self.l3Number.setObjectName(u"l3Number")
        self.l3Number.setMinimumSize(QSize(0, 41))
        self.l3Number.setMaximumSize(QSize(16777215, 41))
        self.l3Number.setFont(font2)
        self.l3Number.setSegmentStyle(QLCDNumber.Flat)

        self.verticalLayout_16.addWidget(self.l3Number)


        self.horizontalLayout_9.addLayout(self.verticalLayout_16)


        self.verticalLayout_17.addWidget(self.widget_9)


        self.horizontalLayout_12.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.frameGraphs_2)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(0, 158))
        self.frame_9.setMaximumSize(QSize(16777215, 158))
        self.frame_9.setStyleSheet(u"background-color:#303030;\n"
"color : #63C8DC;")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_9)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.widget_8 = QWidget(self.frame_9)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setStyleSheet(u"border-color: rgb(255, 255, 0);")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalSpacer_12 = QSpacerItem(20, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_20.addItem(self.verticalSpacer_12)

        self.label_22 = QLabel(self.widget_8)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMaximumSize(QSize(74, 68))
        self.label_22.setPixmap(QPixmap(u":/icons/icons8-groupe-d'utilisateurs-64.png"))
        self.label_22.setScaledContents(True)

        self.verticalLayout_20.addWidget(self.label_22)

        self.verticalSpacer_13 = QSpacerItem(20, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_20.addItem(self.verticalSpacer_13)


        self.horizontalLayout_8.addLayout(self.verticalLayout_20)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_23 = QLabel(self.widget_8)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(70, 31))
        self.label_23.setMaximumSize(QSize(16777215, 31))
        self.label_23.setFont(font2)
        self.label_23.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_23)

        self.verticalSpacer_14 = QSpacerItem(20, 28, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer_14)

        self.m1Number = QLCDNumber(self.widget_8)
        self.m1Number.setObjectName(u"m1Number")
        self.m1Number.setMinimumSize(QSize(0, 41))
        self.m1Number.setMaximumSize(QSize(16777215, 41))
        self.m1Number.setFont(font2)
        self.m1Number.setSegmentStyle(QLCDNumber.Flat)

        self.verticalLayout_15.addWidget(self.m1Number)


        self.horizontalLayout_8.addLayout(self.verticalLayout_15)


        self.verticalLayout_18.addWidget(self.widget_8)


        self.horizontalLayout_12.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.frameGraphs_2)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(0, 158))
        self.frame_10.setMaximumSize(QSize(16777215, 158))
        self.frame_10.setStyleSheet(u"background-color:#303030;\n"
"color : #63C8DC;")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_10)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.widget_10 = QWidget(self.frame_10)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setStyleSheet(u"border-color: rgb(255, 255, 0);")
        self.horizontalLayout_10 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalSpacer_18 = QSpacerItem(20, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_22.addItem(self.verticalSpacer_18)

        self.label_26 = QLabel(self.widget_10)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMaximumSize(QSize(74, 68))
        self.label_26.setPixmap(QPixmap(u":/icons/icons8-groupe-d'utilisateurs-64.png"))
        self.label_26.setScaledContents(True)

        self.verticalLayout_22.addWidget(self.label_26)

        self.verticalSpacer_19 = QSpacerItem(20, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_22.addItem(self.verticalSpacer_19)


        self.horizontalLayout_10.addLayout(self.verticalLayout_22)

        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_27 = QLabel(self.widget_10)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMinimumSize(QSize(70, 31))
        self.label_27.setMaximumSize(QSize(16777215, 31))
        self.label_27.setFont(font2)
        self.label_27.setAlignment(Qt.AlignCenter)

        self.verticalLayout_23.addWidget(self.label_27)

        self.verticalSpacer_20 = QSpacerItem(20, 28, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_23.addItem(self.verticalSpacer_20)

        self.m2Number = QLCDNumber(self.widget_10)
        self.m2Number.setObjectName(u"m2Number")
        self.m2Number.setMinimumSize(QSize(0, 41))
        self.m2Number.setMaximumSize(QSize(16777215, 41))
        self.m2Number.setFont(font2)
        self.m2Number.setSegmentStyle(QLCDNumber.Flat)

        self.verticalLayout_23.addWidget(self.m2Number)


        self.horizontalLayout_10.addLayout(self.verticalLayout_23)


        self.verticalLayout_27.addWidget(self.widget_10)


        self.horizontalLayout_12.addWidget(self.frame_10)


        self.verticalLayout_29.addWidget(self.frameGraphs_2)

        self.frame_15 = QFrame(self.frame_14)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMinimumSize(QSize(0, 81))
        self.frame_15.setMaximumSize(QSize(16777215, 81))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_6 = QSpacerItem(516, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_6)

        self.frame_17 = QFrame(self.frame_15)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.pushButton_5 = QPushButton(self.frame_17)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(87, 50))
        self.pushButton_5.setMaximumSize(QSize(16777215, 50))
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet(u"QPushButton {\n"
"color: #63C8DC;\n"
"background-color: #303030 ;\n"
"border-radius:10px;\n"
"}\n"
"")

        self.horizontalLayout_6.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.frame_17)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(87, 50))
        self.pushButton_6.setMaximumSize(QSize(16777215, 50))
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet(u"QPushButton {\n"
"color: #63C8DC;\n"
"background-color: #303030 ;\n"
"border-radius:10px;\n"
"}\n"
"")

        self.horizontalLayout_6.addWidget(self.pushButton_6)

        self.pushButton_7 = QPushButton(self.frame_17)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(87, 50))
        self.pushButton_7.setMaximumSize(QSize(16777215, 50))
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet(u"QPushButton {\n"
"color: #63C8DC;\n"
"background-color: #303030 ;\n"
"border-radius:10px;\n"
"}\n"
"")

        self.horizontalLayout_6.addWidget(self.pushButton_7)

        self.pushButton_8 = QPushButton(self.frame_17)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(87, 50))
        self.pushButton_8.setMaximumSize(QSize(16777215, 50))
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet(u"QPushButton {\n"
"color: #63C8DC;\n"
"background-color: #303030 ;\n"
"border-radius:10px;\n"
"}\n"
"")

        self.horizontalLayout_6.addWidget(self.pushButton_8)

        self.pushButton_4 = QPushButton(self.frame_17)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(87, 50))
        self.pushButton_4.setMaximumSize(QSize(16777215, 50))
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet(u"QPushButton {\n"
"color: #63C8DC;\n"
"background-color: #303030 ;\n"
"border-radius:10px;\n"
"}\n"
"")

        self.horizontalLayout_6.addWidget(self.pushButton_4)


        self.horizontalLayout_7.addWidget(self.frame_17)


        self.verticalLayout_29.addWidget(self.frame_15)

        self.frameGraphs = QFrame(self.frame_14)
        self.frameGraphs.setObjectName(u"frameGraphs")
        self.frameGraphs.setFrameShape(QFrame.StyledPanel)
        self.frameGraphs.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frameGraphs)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(5, 5, 5, 5)
        self.graphWidget = QWidget(self.frameGraphs)
        self.graphWidget.setObjectName(u"graphWidget")
        self.graphWidget.setStyleSheet(u"border: 2px solid #06070a ;")

        self.verticalLayout_31.addWidget(self.graphWidget)


        self.verticalLayout_29.addWidget(self.frameGraphs)


        self.verticalLayout_30.addWidget(self.frame_14)

        self.pageContainer.addWidget(self.pageDashboard)
        self.pageEtudiants = QWidget()
        self.pageEtudiants.setObjectName(u"pageEtudiants")
        self.verticalLayout_32 = QVBoxLayout(self.pageEtudiants)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.frame_13 = QFrame(self.pageEtudiants)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setStyleSheet(u"border-color: rgb(255, 85, 0);")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.frame_13)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.frame_18 = QFrame(self.frame_13)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMinimumSize(QSize(0, 71))
        self.frame_18.setMaximumSize(QSize(16777215, 71))
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 20)
        self.frame_16 = QFrame(self.frame_18)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.ajoutEdtBtn = QPushButton(self.frame_16)
        self.ajoutEdtBtn.setObjectName(u"ajoutEdtBtn")
        self.ajoutEdtBtn.setMinimumSize(QSize(101, 41))
        self.ajoutEdtBtn.setMaximumSize(QSize(16777215, 51))
        font3 = QFont()
        font3.setPointSize(11)
        self.ajoutEdtBtn.setFont(font3)
        self.ajoutEdtBtn.setStyleSheet(u"QPushButton {\n"
"color: #63C8DC;\n"
"background-color: #303030;\n"
"border-radius:10px;\n"
"}\n"
"")

        self.horizontalLayout_13.addWidget(self.ajoutEdtBtn)

        self.pdfEtd = QPushButton(self.frame_16)
        self.pdfEtd.setObjectName(u"pdfEtd")
        self.pdfEtd.setMinimumSize(QSize(101, 41))
        self.pdfEtd.setMaximumSize(QSize(16777215, 51))
        self.pdfEtd.setFont(font3)
        self.pdfEtd.setStyleSheet(u"QPushButton {\n"
"color: #63C8DC;\n"
"background-color:#303030;\n"
"border-radius:10px;\n"
"}\n"
"")

        self.horizontalLayout_13.addWidget(self.pdfEtd)


        self.horizontalLayout_23.addWidget(self.frame_16)

        self.horizontalSpacer_7 = QSpacerItem(10, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_7)

        self.frame_36 = QFrame(self.frame_18)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setMinimumSize(QSize(661, 45))
        self.frame_36.setMaximumSize(QSize(16777215, 45))
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_36)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.niveauComboBox = QComboBox(self.frame_36)
        self.niveauComboBox.addItem("")
        self.niveauComboBox.addItem("")
        self.niveauComboBox.addItem("")
        self.niveauComboBox.addItem("")
        self.niveauComboBox.addItem("")
        self.niveauComboBox.addItem("")
        self.niveauComboBox.setObjectName(u"niveauComboBox")
        self.niveauComboBox.setMinimumSize(QSize(151, 41))
        self.niveauComboBox.setMaximumSize(QSize(151, 51))
        self.niveauComboBox.setFont(font3)
        self.niveauComboBox.setStyleSheet(u"color: #63C8DC;\n"
"background-color:#303030;\n"
"border: 2px solid #303030;")

        self.horizontalLayout_14.addWidget(self.niveauComboBox)

        self.mentionComboBox = QComboBox(self.frame_36)
        self.mentionComboBox.addItem("")
        self.mentionComboBox.addItem("")
        self.mentionComboBox.addItem("")
        self.mentionComboBox.addItem("")
        self.mentionComboBox.addItem("")
        self.mentionComboBox.addItem("")
        self.mentionComboBox.addItem("")
        self.mentionComboBox.setObjectName(u"mentionComboBox")
        self.mentionComboBox.setMinimumSize(QSize(170, 41))
        self.mentionComboBox.setMaximumSize(QSize(170, 51))
        self.mentionComboBox.setFont(font3)
        self.mentionComboBox.setStyleSheet(u"color: #63C8DC;\n"
"background-color:#303030;\n"
"border: 2px solid #303030;")

        self.horizontalLayout_14.addWidget(self.mentionComboBox)

        self.searchLineEditEtd = QLineEdit(self.frame_36)
        self.searchLineEditEtd.setObjectName(u"searchLineEditEtd")
        self.searchLineEditEtd.setMinimumSize(QSize(0, 41))
        self.searchLineEditEtd.setMaximumSize(QSize(16777215, 51))
        font4 = QFont()
        font4.setPointSize(11)
        font4.setBold(True)
        self.searchLineEditEtd.setFont(font4)
        self.searchLineEditEtd.setStyleSheet(u"color: #63C8DC;\n"
"background-color:#303030;\n"
"border: 2px solid #303030;")

        self.horizontalLayout_14.addWidget(self.searchLineEditEtd)


        self.horizontalLayout_23.addWidget(self.frame_36)


        self.verticalLayout_33.addWidget(self.frame_18)

        self.frame_19 = QFrame(self.frame_13)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_19)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.EtudiantTable = QTableWidget(self.frame_19)
        if (self.EtudiantTable.columnCount() < 9):
            self.EtudiantTable.setColumnCount(9)
        __qtablewidgetitem = QTableWidgetItem()
        self.EtudiantTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.EtudiantTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.EtudiantTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.EtudiantTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.EtudiantTable.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.EtudiantTable.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.EtudiantTable.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.EtudiantTable.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.EtudiantTable.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        self.EtudiantTable.setObjectName(u"EtudiantTable")
        self.EtudiantTable.setFont(font)
        self.EtudiantTable.setStyleSheet(u"QHeaderView::section {\n"
"    color: #63C8DC;\n"
"    background-color:  #303030;\n"
"    font-size: 19px;\n"
"}\n"
"QTableWidget::item {\n"
"     color:  #303564;\n"
"}\n"
"QTableWidget::item:selected {\n"
"    background-color: #444444;\n"
"}\n"
"\n"
"QTableWidget::item:hover {\n"
"    background-color: #555555;\n"
"}\n"
"")
        self.EtudiantTable.setAutoScrollMargin(15)
        self.EtudiantTable.horizontalHeader().setVisible(True)
        self.EtudiantTable.horizontalHeader().setCascadingSectionResizes(False)
        self.EtudiantTable.horizontalHeader().setMinimumSectionSize(125)
        self.EtudiantTable.horizontalHeader().setProperty("showSortIndicator", True)
        self.EtudiantTable.horizontalHeader().setStretchLastSection(True)
        self.EtudiantTable.verticalHeader().setVisible(False)
        self.EtudiantTable.verticalHeader().setMinimumSectionSize(60)
        self.EtudiantTable.verticalHeader().setDefaultSectionSize(35)
        self.EtudiantTable.verticalHeader().setHighlightSections(False)

        self.gridLayout_3.addWidget(self.EtudiantTable, 0, 0, 1, 1)


        self.verticalLayout_33.addWidget(self.frame_19)


        self.verticalLayout_32.addWidget(self.frame_13)

        self.pageContainer.addWidget(self.pageEtudiants)
        self.pageEnseignants = QWidget()
        self.pageEnseignants.setObjectName(u"pageEnseignants")
        self.verticalLayout_35 = QVBoxLayout(self.pageEnseignants)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.frame_20 = QFrame(self.pageEnseignants)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setStyleSheet(u"border-color: rgb(0, 170, 255);")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.frame_20)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.frame_21 = QFrame(self.frame_20)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMinimumSize(QSize(0, 80))
        self.frame_21.setMaximumSize(QSize(16777215, 80))
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 20)
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setSpacing(5)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(-1, -1, -1, 20)
        self.ajoutProfBtn = QPushButton(self.frame_21)
        self.ajoutProfBtn.setObjectName(u"ajoutProfBtn")
        self.ajoutProfBtn.setMinimumSize(QSize(111, 51))
        self.ajoutProfBtn.setMaximumSize(QSize(16777215, 51))
        self.ajoutProfBtn.setFont(font3)
        self.ajoutProfBtn.setStyleSheet(u"QPushButton {\n"
"color: #63C8DC;\n"
"background-color:#303030;\n"
"border-radius:10px;\n"
"}\n"
"")

        self.horizontalLayout_15.addWidget(self.ajoutProfBtn)


        self.horizontalLayout_24.addLayout(self.horizontalLayout_15)

        self.horizontalSpacer_8 = QSpacerItem(378, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_8)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(-1, -1, -1, 20)
        self.gradeComboBox = QComboBox(self.frame_21)
        self.gradeComboBox.addItem("")
        self.gradeComboBox.addItem("")
        self.gradeComboBox.addItem("")
        self.gradeComboBox.addItem("")
        self.gradeComboBox.addItem("")
        self.gradeComboBox.addItem("")
        self.gradeComboBox.setObjectName(u"gradeComboBox")
        self.gradeComboBox.setMinimumSize(QSize(151, 51))
        self.gradeComboBox.setMaximumSize(QSize(151, 51))
        self.gradeComboBox.setFont(font3)
        self.gradeComboBox.setStyleSheet(u"color: #63C8DC;\n"
"background-color:#303030;\n"
"border: 2px solid #303030;")

        self.horizontalLayout_16.addWidget(self.gradeComboBox)

        self.searchProfLineEditEtd = QLineEdit(self.frame_21)
        self.searchProfLineEditEtd.setObjectName(u"searchProfLineEditEtd")
        self.searchProfLineEditEtd.setMinimumSize(QSize(0, 51))
        self.searchProfLineEditEtd.setMaximumSize(QSize(16777215, 51))
        self.searchProfLineEditEtd.setFont(font4)
        self.searchProfLineEditEtd.setStyleSheet(u"color: #63C8DC;\n"
"background-color:#303030;\n"
"border: 2px solid #303030;")

        self.horizontalLayout_16.addWidget(self.searchProfLineEditEtd)


        self.horizontalLayout_24.addLayout(self.horizontalLayout_16)


        self.verticalLayout_34.addWidget(self.frame_21)

        self.frame_23 = QFrame(self.frame_20)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_45 = QVBoxLayout(self.frame_23)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.verticalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.ProfTable = QTableWidget(self.frame_23)
        if (self.ProfTable.columnCount() < 7):
            self.ProfTable.setColumnCount(7)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.ProfTable.setHorizontalHeaderItem(0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.ProfTable.setHorizontalHeaderItem(1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.ProfTable.setHorizontalHeaderItem(2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.ProfTable.setHorizontalHeaderItem(3, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.ProfTable.setHorizontalHeaderItem(4, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.ProfTable.setHorizontalHeaderItem(5, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.ProfTable.setHorizontalHeaderItem(6, __qtablewidgetitem15)
        self.ProfTable.setObjectName(u"ProfTable")
        self.ProfTable.setFont(font3)
        self.ProfTable.setStyleSheet(u"QHeaderView::section {\n"
"    color: #63C8DC;\n"
"    background-color:  #303030;\n"
"    font-size: 19px;\n"
"}\n"
"QTableWidget::item {\n"
"     color:  #303564;\n"
"}\n"
"QTableWidget::item:selected {\n"
"    background-color: #444444;\n"
"}\n"
"\n"
"QTableWidget::item:hover {\n"
"    background-color: #555555;\n"
"}\n"
"")
        self.ProfTable.horizontalHeader().setMinimumSectionSize(190)
        self.ProfTable.horizontalHeader().setProperty("showSortIndicator", True)
        self.ProfTable.horizontalHeader().setStretchLastSection(True)
        self.ProfTable.verticalHeader().setVisible(False)
        self.ProfTable.verticalHeader().setMinimumSectionSize(60)
        self.ProfTable.verticalHeader().setDefaultSectionSize(60)

        self.verticalLayout_45.addWidget(self.ProfTable)


        self.verticalLayout_34.addWidget(self.frame_23)


        self.verticalLayout_35.addWidget(self.frame_20)

        self.pageContainer.addWidget(self.pageEnseignants)
        self.pageCours = QWidget()
        self.pageCours.setObjectName(u"pageCours")
        self.verticalLayout_38 = QVBoxLayout(self.pageCours)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.frame_24 = QFrame(self.pageCours)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setStyleSheet(u"border-color: rgb(255, 85, 0);")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.frame_24)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_22 = QFrame(self.frame_24)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMinimumSize(QSize(0, 71))
        self.frame_22.setMaximumSize(QSize(16777215, 71))
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 20)
        self.frame_25 = QFrame(self.frame_22)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.ajoutCoursBtn = QPushButton(self.frame_25)
        self.ajoutCoursBtn.setObjectName(u"ajoutCoursBtn")
        self.ajoutCoursBtn.setMinimumSize(QSize(101, 51))
        self.ajoutCoursBtn.setMaximumSize(QSize(16777215, 51))
        self.ajoutCoursBtn.setFont(font3)
        self.ajoutCoursBtn.setStyleSheet(u"QPushButton {\n"
"color: #63C8DC;\n"
"background-color: #303030;\n"
"border-radius:10px;\n"
"}\n"
"")

        self.horizontalLayout_17.addWidget(self.ajoutCoursBtn)


        self.horizontalLayout_25.addWidget(self.frame_25)

        self.horizontalSpacer_9 = QSpacerItem(10, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_9)

        self.frame_37 = QFrame(self.frame_22)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setMinimumSize(QSize(661, 60))
        self.frame_37.setMaximumSize(QSize(16777215, 45))
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_37)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 15)
        self.creditComboBox = QComboBox(self.frame_37)
        self.creditComboBox.addItem("")
        self.creditComboBox.addItem("")
        self.creditComboBox.addItem("")
        self.creditComboBox.addItem("")
        self.creditComboBox.addItem("")
        self.creditComboBox.setObjectName(u"creditComboBox")
        self.creditComboBox.setMinimumSize(QSize(151, 51))
        self.creditComboBox.setMaximumSize(QSize(151, 51))
        self.creditComboBox.setFont(font3)
        self.creditComboBox.setStyleSheet(u"color: #63C8DC;\n"
"background-color:#303030;\n"
"border: 2px solid#303030;")

        self.horizontalLayout_18.addWidget(self.creditComboBox)

        self.semestreComboBox = QComboBox(self.frame_37)
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
        self.semestreComboBox.setMinimumSize(QSize(170, 51))
        self.semestreComboBox.setMaximumSize(QSize(170, 51))
        self.semestreComboBox.setFont(font3)
        self.semestreComboBox.setStyleSheet(u"color: #63C8DC;\n"
"background-color:#303030;\n"
"border: 2px solid #303030;")

        self.horizontalLayout_18.addWidget(self.semestreComboBox)

        self.searchLineEditEtd_2 = QLineEdit(self.frame_37)
        self.searchLineEditEtd_2.setObjectName(u"searchLineEditEtd_2")
        self.searchLineEditEtd_2.setMinimumSize(QSize(0, 51))
        self.searchLineEditEtd_2.setMaximumSize(QSize(16777215, 51))
        self.searchLineEditEtd_2.setFont(font4)
        self.searchLineEditEtd_2.setStyleSheet(u"color: #63C8DC;\n"
"background-color:#303030;\n"
"border: 2px solid #303030;")

        self.horizontalLayout_18.addWidget(self.searchLineEditEtd_2)


        self.horizontalLayout_25.addWidget(self.frame_37)


        self.verticalLayout.addWidget(self.frame_22)

        self.frame_38 = QFrame(self.frame_24)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.frame_38)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.CoursTable = QTableWidget(self.frame_38)
        if (self.CoursTable.columnCount() < 8):
            self.CoursTable.setColumnCount(8)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.CoursTable.setHorizontalHeaderItem(0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.CoursTable.setHorizontalHeaderItem(1, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.CoursTable.setHorizontalHeaderItem(2, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.CoursTable.setHorizontalHeaderItem(3, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.CoursTable.setHorizontalHeaderItem(4, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.CoursTable.setHorizontalHeaderItem(5, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.CoursTable.setHorizontalHeaderItem(6, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.CoursTable.setHorizontalHeaderItem(7, __qtablewidgetitem23)
        self.CoursTable.setObjectName(u"CoursTable")
        self.CoursTable.setStyleSheet(u"QHeaderView::section {\n"
"    color: #63C8DC;\n"
"    background-color:  #303030;\n"
"    font-size: 19px;\n"
"}\n"
"QTableWidget::item {\n"
"     color:  #303564;\n"
"}\n"
"QTableWidget::item:selected {\n"
"    background-color: #444444;\n"
"}\n"
"\n"
"QTableWidget::item:hover {\n"
"    background-color: #555555;\n"
"}\n"
"\n"
"")
        self.CoursTable.horizontalHeader().setCascadingSectionResizes(True)
        self.CoursTable.horizontalHeader().setMinimumSectionSize(125)
        self.CoursTable.horizontalHeader().setDefaultSectionSize(125)
        self.CoursTable.horizontalHeader().setProperty("showSortIndicator", True)
        self.CoursTable.horizontalHeader().setStretchLastSection(True)
        self.CoursTable.verticalHeader().setVisible(False)
        self.CoursTable.verticalHeader().setMinimumSectionSize(60)
        self.CoursTable.verticalHeader().setDefaultSectionSize(90)

        self.verticalLayout_37.addWidget(self.CoursTable)


        self.verticalLayout.addWidget(self.frame_38)


        self.verticalLayout_36.addLayout(self.verticalLayout)


        self.verticalLayout_38.addWidget(self.frame_24)

        self.pageContainer.addWidget(self.pageCours)
        self.pageNotes = QWidget()
        self.pageNotes.setObjectName(u"pageNotes")
        self.verticalLayout_41 = QVBoxLayout(self.pageNotes)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.frame_28 = QFrame(self.pageNotes)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setStyleSheet(u"border-color: rgb(255, 85, 0);")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.verticalLayout_39 = QVBoxLayout(self.frame_28)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.frame_29 = QFrame(self.frame_28)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setMinimumSize(QSize(0, 71))
        self.frame_29.setMaximumSize(QSize(16777215, 71))
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.frame_30 = QFrame(self.frame_29)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.ajoutNotesBtn = QPushButton(self.frame_30)
        self.ajoutNotesBtn.setObjectName(u"ajoutNotesBtn")
        self.ajoutNotesBtn.setMinimumSize(QSize(101, 51))
        self.ajoutNotesBtn.setMaximumSize(QSize(16777215, 51))
        self.ajoutNotesBtn.setFont(font3)
        self.ajoutNotesBtn.setStyleSheet(u"QPushButton {\n"
"color: #63C8DC;\n"
"background-color: #303030 ;\n"
"border-radius:10px;\n"
"}\n"
"")

        self.horizontalLayout_20.addWidget(self.ajoutNotesBtn)


        self.horizontalLayout_26.addWidget(self.frame_30)

        self.horizontalSpacer_10 = QSpacerItem(424, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_10)

        self.frame_39 = QFrame(self.frame_29)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setMinimumSize(QSize(661, 60))
        self.frame_39.setMaximumSize(QSize(16777215, 60))
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_39)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 15)
        self.seuilComboBox = QComboBox(self.frame_39)
        self.seuilComboBox.addItem("")
        self.seuilComboBox.addItem("")
        self.seuilComboBox.addItem("")
        self.seuilComboBox.addItem("")
        self.seuilComboBox.setObjectName(u"seuilComboBox")
        self.seuilComboBox.setMinimumSize(QSize(151, 51))
        self.seuilComboBox.setMaximumSize(QSize(151, 51))
        self.seuilComboBox.setFont(font3)
        self.seuilComboBox.setStyleSheet(u"color: #63C8DC;\n"
"background-color:#303030;\n"
"border: 2px solid#303030;")

        self.horizontalLayout_19.addWidget(self.seuilComboBox)

        self.sessionComboBox = QComboBox(self.frame_39)
        self.sessionComboBox.addItem("")
        self.sessionComboBox.addItem("")
        self.sessionComboBox.addItem("")
        self.sessionComboBox.setObjectName(u"sessionComboBox")
        self.sessionComboBox.setMinimumSize(QSize(170, 51))
        self.sessionComboBox.setMaximumSize(QSize(170, 51))
        self.sessionComboBox.setFont(font3)
        self.sessionComboBox.setStyleSheet(u"color: #63C8DC;\n"
"background-color:#303030;\n"
"border: 2px solid#303030;")

        self.horizontalLayout_19.addWidget(self.sessionComboBox)

        self.searchNotesLineEditEtd = QLineEdit(self.frame_39)
        self.searchNotesLineEditEtd.setObjectName(u"searchNotesLineEditEtd")
        self.searchNotesLineEditEtd.setMinimumSize(QSize(0, 51))
        self.searchNotesLineEditEtd.setMaximumSize(QSize(16777215, 51))
        self.searchNotesLineEditEtd.setFont(font4)
        self.searchNotesLineEditEtd.setStyleSheet(u"color: #63C8DC;\n"
"background-color:#303030;\n"
"border: 2px solid#303030;")

        self.horizontalLayout_19.addWidget(self.searchNotesLineEditEtd)


        self.horizontalLayout_26.addWidget(self.frame_39)


        self.verticalLayout_39.addWidget(self.frame_29)

        self.frame_31 = QFrame(self.frame_28)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_31)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.NotesTable = QTableWidget(self.frame_31)
        if (self.NotesTable.columnCount() < 7):
            self.NotesTable.setColumnCount(7)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.NotesTable.setHorizontalHeaderItem(0, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.NotesTable.setHorizontalHeaderItem(1, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.NotesTable.setHorizontalHeaderItem(2, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.NotesTable.setHorizontalHeaderItem(3, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.NotesTable.setHorizontalHeaderItem(4, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.NotesTable.setHorizontalHeaderItem(5, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.NotesTable.setHorizontalHeaderItem(6, __qtablewidgetitem30)
        self.NotesTable.setObjectName(u"NotesTable")
        self.NotesTable.setStyleSheet(u"QHeaderView::section {\n"
"    color: #63C8DC;\n"
"    background-color:  #303030;\n"
"    font-size: 19px;\n"
"}\n"
"QTableWidget::item {\n"
"	color:  #303564;\n"
"}\n"
"QTableWidget::item:selected {\n"
"    background-color: #444444;\n"
"}\n"
"\n"
"QTableWidget::item:hover {\n"
"    background-color: #555555;\n"
"}\n"
"\n"
"")
        self.NotesTable.horizontalHeader().setMinimumSectionSize(150)
        self.NotesTable.horizontalHeader().setProperty("showSortIndicator", True)
        self.NotesTable.horizontalHeader().setStretchLastSection(True)
        self.NotesTable.verticalHeader().setVisible(False)
        self.NotesTable.verticalHeader().setMinimumSectionSize(60)
        self.NotesTable.verticalHeader().setDefaultSectionSize(60)

        self.gridLayout_4.addWidget(self.NotesTable, 0, 0, 1, 1)


        self.verticalLayout_39.addWidget(self.frame_31)


        self.verticalLayout_41.addWidget(self.frame_28)

        self.pageContainer.addWidget(self.pageNotes)
        self.pageReleves = QWidget()
        self.pageReleves.setObjectName(u"pageReleves")
        self.verticalLayout_44 = QVBoxLayout(self.pageReleves)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.frame_32 = QFrame(self.pageReleves)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setStyleSheet(u"border-color: rgb(255, 85, 0);")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.verticalLayout_42 = QVBoxLayout(self.frame_32)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.frame_33 = QFrame(self.frame_32)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setMinimumSize(QSize(0, 71))
        self.frame_33.setMaximumSize(QSize(16777215, 71))
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_33)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 15)
        self.frame_34 = QFrame(self.frame_33)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.ajoutReleveBtn = QPushButton(self.frame_34)
        self.ajoutReleveBtn.setObjectName(u"ajoutReleveBtn")
        self.ajoutReleveBtn.setMinimumSize(QSize(101, 51))
        self.ajoutReleveBtn.setMaximumSize(QSize(16777215, 51))
        self.ajoutReleveBtn.setFont(font3)
        self.ajoutReleveBtn.setStyleSheet(u"QPushButton {\n"
"color: #63C8DC;\n"
"background-color:  #303030 ;\n"
"border-radius:10px;\n"
"}\n"
"")

        self.horizontalLayout_21.addWidget(self.ajoutReleveBtn)

        self.pdfReleveBtn = QPushButton(self.frame_34)
        self.pdfReleveBtn.setObjectName(u"pdfReleveBtn")
        self.pdfReleveBtn.setMinimumSize(QSize(101, 51))
        self.pdfReleveBtn.setMaximumSize(QSize(16777215, 51))
        self.pdfReleveBtn.setFont(font3)
        self.pdfReleveBtn.setStyleSheet(u"QPushButton {\n"
"color: #63C8DC;\n"
"background-color:  #303030 ;\n"
"border-radius:10px;\n"
"}\n"
"")

        self.horizontalLayout_21.addWidget(self.pdfReleveBtn)


        self.horizontalLayout_22.addWidget(self.frame_34)

        self.horizontalSpacer_11 = QSpacerItem(424, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_11)


        self.verticalLayout_42.addWidget(self.frame_33)

        self.frame_35 = QFrame(self.frame_32)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.verticalLayout_43 = QVBoxLayout(self.frame_35)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.frame_35)
        if (self.tableWidget.columnCount() < 7):
            self.tableWidget.setColumnCount(7)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem37)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"QHeaderView::section {\n"
"    color: #63C8DC;\n"
"    background-color:#303030;\n"
"    font-size: 19px;\n"
"}\n"
"QTableWidget::item {\n"
"   color:  #303564;\n"
"}\n"
"QTableWidget::item:selected {\n"
"    background-color: #444444;\n"
"}\n"
"\n"
"QTableWidget::item:hover {\n"
"    background-color: #555555;\n"
"}\n"
"\n"
"")
        self.tableWidget.horizontalHeader().setMinimumSectionSize(170)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)

        self.verticalLayout_43.addWidget(self.tableWidget)


        self.verticalLayout_42.addWidget(self.frame_35)


        self.verticalLayout_44.addWidget(self.frame_32)

        self.pageContainer.addWidget(self.pageReleves)

        self.verticalLayout_13.addWidget(self.pageContainer)


        self.verticalLayout_2.addWidget(self.widget_4)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 2, 1, 1)

        self.widget_2 = QWidget(self.frame)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(241, 0))
        self.widget_2.setMaximumSize(QSize(241, 16777215))
        self.widget_2.setStyleSheet(u"background-color:#303030 ;\n"
"border-radius:10px;\n"
"color: #63C8DC;\n"
"\n"
"")
        self.verticalLayout_7 = QVBoxLayout(self.widget_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(13, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(13)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(80, 80))
        self.label_2.setMaximumSize(QSize(80, 80))
        self.label_2.setPixmap(QPixmap(u":/icons/education.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label_2)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalSpacer_2 = QSpacerItem(13, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_7.addLayout(self.horizontalLayout_2)

        self.frame_4 = QFrame(self.widget_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_2 = QFrame(self.frame_4)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.dashBtn2 = QPushButton(self.frame_2)
        self.dashBtn2.setObjectName(u"dashBtn2")
        self.dashBtn2.setMinimumSize(QSize(157, 50))
        self.dashBtn2.setFont(font4)
        self.dashBtn2.setStyleSheet(u"QPushButton {\n"
"color: #63C8DC;\n"
"}\n"
"QPushButton::hover{\n"
"color: #63C8DC;\n"
"	background-color:#FBFBFE;\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons8-dashboard-layout-96 (1).png", QSize(), QIcon.Normal, QIcon.Off)
        icon9.addFile(u":/icons/icons8-dashboard-layout-96.png", QSize(), QIcon.Active, QIcon.On)
        self.dashBtn2.setIcon(icon9)
        self.dashBtn2.setIconSize(QSize(30, 30))
        self.dashBtn2.setCheckable(True)
        self.dashBtn2.setAutoExclusive(True)
        self.dashBtn2.setFlat(True)

        self.verticalLayout_4.addWidget(self.dashBtn2)

        self.etdBtn2 = QPushButton(self.frame_2)
        self.etdBtn2.setObjectName(u"etdBtn2")
        self.etdBtn2.setMinimumSize(QSize(157, 50))
        self.etdBtn2.setFont(font4)
        self.etdBtn2.setStyleSheet(u"QPushButton {\n"
"color: #63C8DC;\n"
"}\n"
"QPushButton::hover{\n"
"color: #63C8DC;\n"
"	background-color:#FBFBFE;\n"
"}")
        self.etdBtn2.setIcon(icon1)
        self.etdBtn2.setIconSize(QSize(35, 35))
        self.etdBtn2.setCheckable(True)
        self.etdBtn2.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.etdBtn2)

        self.esgBtn2 = QPushButton(self.frame_2)
        self.esgBtn2.setObjectName(u"esgBtn2")
        self.esgBtn2.setMinimumSize(QSize(157, 50))
        self.esgBtn2.setFont(font4)
        self.esgBtn2.setStyleSheet(u"QPushButton {\n"
"color: #63C8DC;\n"
"}\n"
"QPushButton::hover{\n"
"color: #63C8DC;\n"
"	background-color:#FBFBFE;\n"
"}")
        self.esgBtn2.setIcon(icon2)
        self.esgBtn2.setIconSize(QSize(35, 35))
        self.esgBtn2.setCheckable(True)
        self.esgBtn2.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.esgBtn2)

        self.coursBtn2 = QPushButton(self.frame_2)
        self.coursBtn2.setObjectName(u"coursBtn2")
        self.coursBtn2.setMinimumSize(QSize(157, 50))
        self.coursBtn2.setFont(font4)
        self.coursBtn2.setStyleSheet(u"QPushButton {\n"
"color: #63C8DC;\n"
"}\n"
"QPushButton::hover{\n"
"color: #63C8DC;\n"
"	background-color:#FBFBFE;\n"
"}")
        self.coursBtn2.setIcon(icon3)
        self.coursBtn2.setIconSize(QSize(35, 35))
        self.coursBtn2.setCheckable(True)
        self.coursBtn2.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.coursBtn2)

        self.notesBtn2 = QPushButton(self.frame_2)
        self.notesBtn2.setObjectName(u"notesBtn2")
        self.notesBtn2.setMinimumSize(QSize(157, 50))
        self.notesBtn2.setFont(font4)
        self.notesBtn2.setStyleSheet(u"QPushButton {\n"
"color: #63C8DC;\n"
"}\n"
"QPushButton::hover{\n"
"color: #63C8DC;\n"
"	background-color:#FBFBFE;\n"
"}")
        self.notesBtn2.setIcon(icon4)
        self.notesBtn2.setIconSize(QSize(40, 35))
        self.notesBtn2.setCheckable(True)
        self.notesBtn2.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.notesBtn2)

        self.rlvBtn2 = QPushButton(self.frame_2)
        self.rlvBtn2.setObjectName(u"rlvBtn2")
        self.rlvBtn2.setMinimumSize(QSize(157, 50))
        self.rlvBtn2.setFont(font4)
        self.rlvBtn2.setStyleSheet(u"QPushButton {\n"
"color: #63C8DC;\n"
"}\n"
"QPushButton::hover{\n"
"color: #63C8DC;\n"
"	background-color:#FBFBFE;\n"
"}")
        self.rlvBtn2.setIcon(icon5)
        self.rlvBtn2.setIconSize(QSize(35, 35))
        self.rlvBtn2.setCheckable(True)
        self.rlvBtn2.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.rlvBtn2)


        self.verticalLayout_6.addWidget(self.frame_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer)

        self.frame_3 = QFrame(self.frame_4)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.prmtBtn2 = QPushButton(self.frame_3)
        self.prmtBtn2.setObjectName(u"prmtBtn2")
        self.prmtBtn2.setMinimumSize(QSize(157, 50))
        self.prmtBtn2.setFont(font4)
        self.prmtBtn2.setStyleSheet(u"QPushButton {\n"
"color: #63C8DC;\n"
"}\n"
"QPushButton::hover{\n"
"color: #63C8DC;\n"
"	background-color:#FBFBFE;\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons8-settings-96.png", QSize(), QIcon.Normal, QIcon.Off)
        icon10.addFile(u":/icons/icons8-param\u00e8tres-96.png", QSize(), QIcon.Active, QIcon.On)
        icon10.addFile(u":/icons/icons8-param\u00e8tres-96.png", QSize(), QIcon.Selected, QIcon.On)
        self.prmtBtn2.setIcon(icon10)
        self.prmtBtn2.setIconSize(QSize(32, 32))
        self.prmtBtn2.setCheckable(True)
        self.prmtBtn2.setAutoExclusive(True)

        self.verticalLayout_5.addWidget(self.prmtBtn2)

        self.quitBtn2 = QPushButton(self.frame_3)
        self.quitBtn2.setObjectName(u"quitBtn2")
        self.quitBtn2.setMinimumSize(QSize(157, 50))
        self.quitBtn2.setFont(font4)
        self.quitBtn2.setStyleSheet(u"QPushButton {\n"
"color: #63C8DC;\n"
"}\n"
"QPushButton::hover{\n"
"color: #63C8DC;\n"
"	background-color:#FBFBFE;\n"
"}")
        self.quitBtn2.setIcon(icon7)
        self.quitBtn2.setIconSize(QSize(35, 35))
        self.quitBtn2.setCheckable(True)
        self.quitBtn2.setAutoExclusive(True)

        self.verticalLayout_5.addWidget(self.quitBtn2)


        self.verticalLayout_6.addWidget(self.frame_3)


        self.verticalLayout_7.addWidget(self.frame_4)


        self.gridLayout.addWidget(self.widget_2, 0, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.verticalLayout_46.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.menuBtn.toggled.connect(self.widget_2.setHidden)
        self.menuBtn.toggled.connect(self.widget.setVisible)
        self.quitBtn2.toggled.connect(MainWindow.close)
        self.quitBtn1.toggled.connect(MainWindow.close)

        self.pageContainer.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.dashBtn1.setText("")
        self.etdBtn1.setText("")
        self.esgBtn1.setText("")
        self.coursBtn1.setText("")
        self.notesBtn1.setText("")
        self.rlvBtn1.setText("")
        self.prmtBtn1.setText("")
        self.quitBtn1.setText("")
        self.menuBtn.setText("")
        self.label_28.setText("")
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Total L1", None))
        self.label_20.setText("")
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Total L2", None))
        self.label_24.setText("")
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Total L3", None))
        self.label_22.setText("")
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Total M1", None))
        self.label_26.setText("")
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Total M2", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"L1", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"L2", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"L3", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"M1", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"M2", None))
        self.ajoutEdtBtn.setText(QCoreApplication.translate("MainWindow", u"Ajouter", None))
        self.pdfEtd.setText(QCoreApplication.translate("MainWindow", u"PDF", None))
        self.niveauComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Choisir le niveau", None))
        self.niveauComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"L1", None))
        self.niveauComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"L2", None))
        self.niveauComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"L3", None))
        self.niveauComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"M1", None))
        self.niveauComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"M2", None))

        self.mentionComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Choisir la mention", None))
        self.mentionComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Informatique g\u00e9n\u00e9rale", None))
        self.mentionComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Syst\u00e8me et r\u00e9seaux", None))
        self.mentionComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"G\u00e9nie logiciel", None))
        self.mentionComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Syst\u00e8mes embarqu\u00e9s", None))
        self.mentionComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Cybers\u00e9curit\u00e9", None))
        self.mentionComboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"Intelligence Artificielle", None))

        self.searchLineEditEtd.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Rechercher...", None))
        ___qtablewidgetitem = self.EtudiantTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Matricule", None));
        ___qtablewidgetitem1 = self.EtudiantTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Noms", None));
        ___qtablewidgetitem2 = self.EtudiantTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Naissance", None));
        ___qtablewidgetitem3 = self.EtudiantTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Contact", None));
        ___qtablewidgetitem4 = self.EtudiantTable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        ___qtablewidgetitem5 = self.EtudiantTable.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Mention", None));
        ___qtablewidgetitem6 = self.EtudiantTable.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Niveau", None));
        ___qtablewidgetitem7 = self.EtudiantTable.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Adresse", None));
        ___qtablewidgetitem8 = self.EtudiantTable.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Actions", None));
        self.ajoutProfBtn.setText(QCoreApplication.translate("MainWindow", u"Ajouter", None))
        self.gradeComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Choisir le grade", None))
        self.gradeComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Enseignant vacataire", None))
        self.gradeComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Enseignant chercheur", None))
        self.gradeComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Docteur", None))
        self.gradeComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Professeur", None))
        self.gradeComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"HDR", None))

        self.searchProfLineEditEtd.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Rechercher...", None))
        ___qtablewidgetitem9 = self.ProfTable.horizontalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Matricule", None));
        ___qtablewidgetitem10 = self.ProfTable.horizontalHeaderItem(1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Noms", None));
        ___qtablewidgetitem11 = self.ProfTable.horizontalHeaderItem(2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Grade", None));
        ___qtablewidgetitem12 = self.ProfTable.horizontalHeaderItem(3)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Contact", None));
        ___qtablewidgetitem13 = self.ProfTable.horizontalHeaderItem(4)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        ___qtablewidgetitem14 = self.ProfTable.horizontalHeaderItem(5)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Adresse", None));
        ___qtablewidgetitem15 = self.ProfTable.horizontalHeaderItem(6)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Actions", None));
        self.ajoutCoursBtn.setText(QCoreApplication.translate("MainWindow", u"Ajouter", None))
        self.creditComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Choisir le cr\u00e9dit", None))
        self.creditComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"1", None))
        self.creditComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"2", None))
        self.creditComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"3", None))
        self.creditComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"4", None))

        self.semestreComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Choisir le semestre", None))
        self.semestreComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Semestre  1", None))
        self.semestreComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Semestre 2", None))
        self.semestreComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Semestre 3", None))
        self.semestreComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Semestre 4", None))
        self.semestreComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Semestre 5", None))
        self.semestreComboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"Semestre 6", None))
        self.semestreComboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"Semestre 7", None))
        self.semestreComboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"Semestre 8", None))
        self.semestreComboBox.setItemText(9, QCoreApplication.translate("MainWindow", u"Semestre 9", None))
        self.semestreComboBox.setItemText(10, QCoreApplication.translate("MainWindow", u"Semestre 10", None))

        self.searchLineEditEtd_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Rechercher...", None))
        ___qtablewidgetitem16 = self.CoursTable.horizontalHeaderItem(0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Unit\u00e9 d'enseignement", None));
        ___qtablewidgetitem17 = self.CoursTable.horizontalHeaderItem(1)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"El\u00e9ment constitutif", None));
        ___qtablewidgetitem18 = self.CoursTable.horizontalHeaderItem(2)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Enseignant", None));
        ___qtablewidgetitem19 = self.CoursTable.horizontalHeaderItem(3)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Semestre", None));
        ___qtablewidgetitem20 = self.CoursTable.horizontalHeaderItem(4)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Cr\u00e9dit", None));
        ___qtablewidgetitem21 = self.CoursTable.horizontalHeaderItem(5)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Niveau", None));
        ___qtablewidgetitem22 = self.CoursTable.horizontalHeaderItem(6)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Mention", None));
        ___qtablewidgetitem23 = self.CoursTable.horizontalHeaderItem(7)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Actions", None));
        self.ajoutNotesBtn.setText(QCoreApplication.translate("MainWindow", u"Ajouter", None))
        self.seuilComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Choisir le seuil", None))
        self.seuilComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"inf\u00e9rieur \u00e0 10 ", None))
        self.seuilComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"\u00e9gal \u00e0 10", None))
        self.seuilComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"sup\u00e9rieur \u00e0 10", None))

        self.sessionComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Choisir la session", None))
        self.sessionComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"session normale", None))
        self.sessionComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"rattrapage", None))

        self.searchNotesLineEditEtd.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Rechercher...", None))
        ___qtablewidgetitem24 = self.NotesTable.horizontalHeaderItem(0)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Nom de l'\u00e9tudiant", None));
        ___qtablewidgetitem25 = self.NotesTable.horizontalHeaderItem(1)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"El\u00e9ment constitutif", None));
        ___qtablewidgetitem26 = self.NotesTable.horizontalHeaderItem(2)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"Notes re\u00e7ues", None));
        ___qtablewidgetitem27 = self.NotesTable.horizontalHeaderItem(3)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"Semestre", None));
        ___qtablewidgetitem28 = self.NotesTable.horizontalHeaderItem(4)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"Date de l'examen", None));
        ___qtablewidgetitem29 = self.NotesTable.horizontalHeaderItem(5)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"Session", None));
        ___qtablewidgetitem30 = self.NotesTable.horizontalHeaderItem(6)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"Actions", None));
        self.ajoutReleveBtn.setText(QCoreApplication.translate("MainWindow", u"Ajouter", None))
        self.pdfReleveBtn.setText(QCoreApplication.translate("MainWindow", u"PDF", None))
        ___qtablewidgetitem31 = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"Num\u00e9ro du relev\u00e9", None));
        ___qtablewidgetitem32 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"Etudiant", None));
        ___qtablewidgetitem33 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"UE", None));
        ___qtablewidgetitem34 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"Note finale", None));
        ___qtablewidgetitem35 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"Cr\u00e9dit obtenu", None));
        ___qtablewidgetitem36 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"D\u00e9cision du Jury", None));
        ___qtablewidgetitem37 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"Actions", None));
        self.label_2.setText("")
        self.dashBtn2.setText(QCoreApplication.translate("MainWindow", u"      Dashboard", None))
        self.etdBtn2.setText(QCoreApplication.translate("MainWindow", u"       Etudiants", None))
        self.esgBtn2.setText(QCoreApplication.translate("MainWindow", u"    Enseignants", None))
        self.coursBtn2.setText(QCoreApplication.translate("MainWindow", u"              Cours", None))
        self.notesBtn2.setText(QCoreApplication.translate("MainWindow", u"            Notes", None))
        self.rlvBtn2.setText(QCoreApplication.translate("MainWindow", u"           Relev\u00e9s", None))
        self.prmtBtn2.setText(QCoreApplication.translate("MainWindow", u"      Param\u00e8tres", None))
        self.quitBtn2.setText(QCoreApplication.translate("MainWindow", u"             Quitter", None))
    # retranslateUi

