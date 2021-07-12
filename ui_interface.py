# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaceaglUsv.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(737, 473)
        MainWindow.setMinimumSize(QSize(737, 473))
        MainWindow.setStyleSheet(u"*{\n"
"	border: none;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(24, 24, 36);\n"
"color: white;")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.side_menu_container = QFrame(self.centralwidget)
        self.side_menu_container.setObjectName(u"side_menu_container")
        self.side_menu_container.setMaximumSize(QSize(0, 16777215))
        self.side_menu_container.setStyleSheet(u"background-color: rgb(9,5,13);")
        self.side_menu_container.setFrameShape(QFrame.StyledPanel)
        self.side_menu_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.side_menu_container)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.side_menu = QFrame(self.side_menu_container)
        self.side_menu.setObjectName(u"side_menu")
        self.side_menu.setMinimumSize(QSize(196, 0))
        self.side_menu.setFrameShape(QFrame.StyledPanel)
        self.side_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.side_menu)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(6, 0, 0, 0)
        self.app_name_header_frame = QFrame(self.side_menu)
        self.app_name_header_frame.setObjectName(u"app_name_header_frame")
        self.app_name_header_frame.setFrameShape(QFrame.StyledPanel)
        self.app_name_header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.app_name_header_frame)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_app_name = QLabel(self.app_name_header_frame)
        self.label_app_name.setObjectName(u"label_app_name")

        self.horizontalLayout_7.addWidget(self.label_app_name, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.label_app_logo = QLabel(self.app_name_header_frame)
        self.label_app_logo.setObjectName(u"label_app_logo")
        self.label_app_logo.setMaximumSize(QSize(30, 30))
        self.label_app_logo.setPixmap(QPixmap(u":/icons/icons/twitter.svg"))
        self.label_app_logo.setScaledContents(True)

        self.horizontalLayout_7.addWidget(self.label_app_logo, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer)


        self.verticalLayout_6.addWidget(self.app_name_header_frame, 0, Qt.AlignTop)

        self.frame_8 = QFrame(self.side_menu)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy)
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_8)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 9)
        self.toolBox = QToolBox(self.frame_8)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setStyleSheet(u"QToolBox{\n"
"	background-color: rgb(24, 24, 36);\n"
"	text-align: left;\n"
"}\n"
"QToolBox::tab{\n"
"	border-radius: 5px;\n"
"	background-color: rgb(17, 16, 26);\n"
"	text-align: left;\n"
"}\n"
"")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.page_1.setGeometry(QRect(0, 0, 190, 309))
        self.verticalLayout_8 = QVBoxLayout(self.page_1)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 6)
        self.frame_10 = QFrame(self.page_1)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_10)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.pushButton_10 = QPushButton(self.frame_10)
        self.pushButton_10.setObjectName(u"pushButton_10")
        icon = QIcon()
        icon.addFile(u":/icons/icons/alert-triangle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_10.setIcon(icon)

        self.verticalLayout_9.addWidget(self.pushButton_10)

        self.pushButton_11 = QPushButton(self.frame_10)
        self.pushButton_11.setObjectName(u"pushButton_11")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/bar-chart-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_11.setIcon(icon1)

        self.verticalLayout_9.addWidget(self.pushButton_11)

        self.pushButton_12 = QPushButton(self.frame_10)
        self.pushButton_12.setObjectName(u"pushButton_12")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/key.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_12.setIcon(icon2)

        self.verticalLayout_9.addWidget(self.pushButton_12)


        self.verticalLayout_8.addWidget(self.frame_10, 0, Qt.AlignTop)

        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/chevron-down.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox.addItem(self.page_1, icon3, u"Drop Menu 1")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 190, 309))
        self.verticalLayout_10 = QVBoxLayout(self.page_2)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 6)
        self.frame_11 = QFrame(self.page_2)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_11)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.pushButton_13 = QPushButton(self.frame_11)
        self.pushButton_13.setObjectName(u"pushButton_13")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/phone-incoming.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_13.setIcon(icon4)

        self.verticalLayout_11.addWidget(self.pushButton_13)

        self.pushButton_14 = QPushButton(self.frame_11)
        self.pushButton_14.setObjectName(u"pushButton_14")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/printer.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_14.setIcon(icon5)

        self.verticalLayout_11.addWidget(self.pushButton_14)


        self.verticalLayout_10.addWidget(self.frame_11, 0, Qt.AlignTop)

        self.label_4 = QLabel(self.page_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setWordWrap(True)

        self.verticalLayout_10.addWidget(self.label_4)

        self.toolBox.addItem(self.page_2, icon3, u"Drop Menu 2")

        self.verticalLayout_7.addWidget(self.toolBox)


        self.verticalLayout_6.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.side_menu)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 6)
        self.pushButton_9 = QPushButton(self.frame_9)
        self.pushButton_9.setObjectName(u"pushButton_9")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/external-link.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_9.setIcon(icon6)

        self.horizontalLayout_8.addWidget(self.pushButton_9)


        self.verticalLayout_6.addWidget(self.frame_9, 0, Qt.AlignLeft|Qt.AlignVCenter)


        self.verticalLayout_2.addWidget(self.side_menu)


        self.horizontalLayout.addWidget(self.side_menu_container)

        self.main_body = QFrame(self.centralwidget)
        self.main_body.setObjectName(u"main_body")
        self.main_body.setFrameShape(QFrame.StyledPanel)
        self.main_body.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.main_body)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_frame = QFrame(self.main_body)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setStyleSheet(u"background-color: rgb(9,5,13);")
        self.header_frame.setFrameShape(QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_6 = QFrame(self.header_frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_6)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.side_menu_button = QPushButton(self.frame_6)
        self.side_menu_button.setObjectName(u"side_menu_button")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/align-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.side_menu_button.setIcon(icon7)
        self.side_menu_button.setIconSize(QSize(32, 32))

        self.verticalLayout_5.addWidget(self.side_menu_button, 0, Qt.AlignVCenter)


        self.horizontalLayout_2.addWidget(self.frame_6, 0, Qt.AlignLeft|Qt.AlignTop)

        self.frame_2 = QFrame(self.header_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.lineEdit = QLineEdit(self.frame_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(142, 0))
        self.lineEdit.setStyleSheet(u"QLineEdit[text=\"\"]{\n"
"	color:rgb(186, 189, 182);\n"
"}\n"
"QLineEdit{\n"
"	border-bottom: 3px solid rgb(230, 5, 64);\n"
"}")

        self.horizontalLayout_6.addWidget(self.lineEdit, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.pushButton_6 = QPushButton(self.frame_2)
        self.pushButton_6.setObjectName(u"pushButton_6")
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon8)

        self.horizontalLayout_6.addWidget(self.pushButton_6, 0, Qt.AlignLeft|Qt.AlignVCenter)


        self.horizontalLayout_2.addWidget(self.frame_2, 0, Qt.AlignLeft|Qt.AlignTop)

        self.frame = QFrame(self.header_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame)
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.pushButton_5 = QPushButton(self.frame)
        self.pushButton_5.setObjectName(u"pushButton_5")
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon9)

        self.horizontalLayout_5.addWidget(self.pushButton_5)

        self.pushButton_4 = QPushButton(self.frame)
        self.pushButton_4.setObjectName(u"pushButton_4")
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/bell.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon10)

        self.horizontalLayout_5.addWidget(self.pushButton_4)


        self.horizontalLayout_2.addWidget(self.frame, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.frame_3 = QFrame(self.header_frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(6, 0, 6, 6)
        self.minimize_window_button = QPushButton(self.frame_3)
        self.minimize_window_button.setObjectName(u"minimize_window_button")
        icon11 = QIcon()
        icon11.addFile(u":/icons/icons/arrow-down-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_window_button.setIcon(icon11)

        self.horizontalLayout_4.addWidget(self.minimize_window_button)

        self.maximize_window_button = QPushButton(self.frame_3)
        self.maximize_window_button.setObjectName(u"maximize_window_button")
        icon12 = QIcon()
        icon12.addFile(u":/icons/icons/maximize-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.maximize_window_button.setIcon(icon12)

        self.horizontalLayout_4.addWidget(self.maximize_window_button)

        self.exit_button = QPushButton(self.frame_3)
        self.exit_button.setObjectName(u"exit_button")
        icon13 = QIcon()
        icon13.addFile(u":/icons/icons/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.exit_button.setIcon(icon13)

        self.horizontalLayout_4.addWidget(self.exit_button)


        self.horizontalLayout_2.addWidget(self.frame_3, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout.addWidget(self.header_frame, 0, Qt.AlignTop)

        self.main_body_contents = QFrame(self.main_body)
        self.main_body_contents.setObjectName(u"main_body_contents")
        sizePolicy.setHeightForWidth(self.main_body_contents.sizePolicy().hasHeightForWidth())
        self.main_body_contents.setSizePolicy(sizePolicy)
        self.main_body_contents.setFrameShape(QFrame.StyledPanel)
        self.main_body_contents.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.main_body_contents)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_5 = QLabel(self.main_body_contents)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(60, 60))
        self.label_5.setMaximumSize(QSize(60, 60))
        self.label_5.setStyleSheet(u"border: 3px dot-dash rgb(230, 5, 64);\n"
"border-radius: 30;")
        self.label_5.setPixmap(QPixmap(u":/icons/icons/alert-triangle.svg"))
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_5, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.label_6 = QLabel(self.main_body_contents)
        self.label_6.setObjectName(u"label_6")
        font = QFont()
        font.setFamily(u"Ubuntu Light")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)

        self.verticalLayout_12.addWidget(self.label_6, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout.addWidget(self.main_body_contents)

        self.footer = QFrame(self.main_body)
        self.footer.setObjectName(u"footer")
        self.footer.setFrameShape(QFrame.StyledPanel)
        self.footer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.footer)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.footer)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(6, 0, 0, 6)
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")

        self.verticalLayout_4.addWidget(self.label, 0, Qt.AlignHCenter)


        self.horizontalLayout_3.addWidget(self.frame_4, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.frame_5 = QFrame(self.footer)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy1)
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 6)
        self.pushButton_7 = QPushButton(self.frame_5)
        self.pushButton_7.setObjectName(u"pushButton_7")
        icon14 = QIcon()
        icon14.addFile(u":/icons/icons/box.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_7.setIcon(icon14)

        self.verticalLayout_3.addWidget(self.pushButton_7, 0, Qt.AlignRight)


        self.horizontalLayout_3.addWidget(self.frame_5, 0, Qt.AlignVCenter)

        self.size_grip = QFrame(self.footer)
        self.size_grip.setObjectName(u"size_grip")
        self.size_grip.setMinimumSize(QSize(10, 10))
        self.size_grip.setMaximumSize(QSize(10, 10))
        self.size_grip.setFrameShape(QFrame.StyledPanel)
        self.size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.size_grip, 0, Qt.AlignHCenter|Qt.AlignBottom)


        self.verticalLayout.addWidget(self.footer, 0, Qt.AlignBottom)


        self.horizontalLayout.addWidget(self.main_body)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 737, 22))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        self.toolBox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Modern UI v.1.0.0", None))
        self.label_app_name.setText(QCoreApplication.translate("MainWindow", u"APP NAME", None))
        self.label_app_logo.setText("")
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"ITEM 1", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"ITEM 2", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"ITEM 3", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_1), QCoreApplication.translate("MainWindow", u"Drop Menu 1", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"SUB MENU", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"SUB MENU", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Some texts you would like to fill here", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"Drop Menu 2", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.side_menu_button.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.pushButton_6.setText("")
        self.pushButton_5.setText("")
        self.pushButton_4.setText("")
        self.minimize_window_button.setText("")
        self.maximize_window_button.setText("")
        self.exit_button.setText("")
        self.label_5.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Construction Ahead", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Modern UI v.1.0.0", None))
        self.pushButton_7.setText("")
    # retranslateUi

