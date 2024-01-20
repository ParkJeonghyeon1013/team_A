# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'animal_farm_1.ui'
##
## Created by: Qt User Interface Compiler version 5.15.6
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore


class Ui_Form_main(object):
    def setupUi(self, Form_main):
        if not Form_main.objectName():
            Form_main.setObjectName(u"Form_main")
        Form_main.resize(379, 175)
        self.gridLayout = QGridLayout(Form_main)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(Form_main)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label__main_title1 = QLabel(self.groupBox)
        self.label__main_title1.setObjectName(u"label__main_title1")

        self.horizontalLayout.addWidget(self.label__main_title1)

        self.label__path = QLabel(self.groupBox)
        self.label__path.setObjectName(u"label__path")

        self.horizontalLayout.addWidget(self.label__path)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.toolButton__main_select_path = QToolButton(self.groupBox)
        self.toolButton__main_select_path.setObjectName(u"toolButton__main_select_path")

        self.horizontalLayout.addWidget(self.toolButton__main_select_path)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label__main_title2 = QLabel(self.groupBox)
        self.label__main_title2.setObjectName(u"label__main_title2")

        self.horizontalLayout_2.addWidget(self.label__main_title2)

        self.lineEdit__main_animal_name = QLineEdit(self.groupBox)
        self.lineEdit__main_animal_name.setObjectName(u"lineEdit__main_animal_name")

        self.horizontalLayout_2.addWidget(self.lineEdit__main_animal_name)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label__main_title3 = QLabel(self.groupBox)
        self.label__main_title3.setObjectName(u"label__main_title3")

        self.horizontalLayout_3.addWidget(self.label__main_title3)

        self.lineEdit__main_animal_sound = QLineEdit(self.groupBox)
        self.lineEdit__main_animal_sound.setObjectName(u"lineEdit__main_animal_sound")

        self.horizontalLayout_3.addWidget(self.lineEdit__main_animal_sound)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.pushButton__main_animal_search = QPushButton(Form_main)
        self.pushButton__main_animal_search.setObjectName(u"pushButton__main_animal_search")

        self.gridLayout.addWidget(self.pushButton__main_animal_search, 1, 0, 1, 1)


        self.retranslateUi(Form_main)

        QMetaObject.connectSlotsByName(Form_main)
    # setupUi

    def retranslateUi(self, Form_main):
        Form_main.setWindowTitle(QCoreApplication.translate("Form_main", u"Main", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form_main", u"Animal Farm", None))
        self.label__main_title1.setText(QCoreApplication.translate("Form_main", u"Path", None))
        self.label__path.setText(QCoreApplication.translate("Form_main", u"/home/rapa", None))
        self.toolButton__main_select_path.setText(QCoreApplication.translate("Form_main", u"...", None))
        self.label__main_title2.setText(QCoreApplication.translate("Form_main", u"Animal Name", None))
        self.label__main_title3.setText(QCoreApplication.translate("Form_main", u"Animal Sound", None))
        self.pushButton__main_animal_search.setText(QCoreApplication.translate("Form_main", u"Animal Search", None))
    # retranslateUi

