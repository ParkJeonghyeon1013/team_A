# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'animal_farm_2.ui'
##
## Created by: Qt User Interface Compiler version 5.15.6
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore


class Ui_Form_2(object):
    def setupUi(self, Form_2):
        if not Form_2.objectName():
            Form_2.setObjectName(u"Form_2")
        Form_2.resize(361, 97)
        self.gridLayout = QGridLayout(Form_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label__animal_name = QLabel(Form_2)
        self.label__animal_name.setObjectName(u"label__animal_name")

        self.horizontalLayout_2.addWidget(self.label__animal_name)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.label__exist = QLabel(Form_2)
        self.label__exist.setObjectName(u"label__exist")

        self.horizontalLayout_2.addWidget(self.label__exist)


        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton__delete_file = QPushButton(Form_2)
        self.pushButton__delete_file.setObjectName(u"pushButton__delete_file")

        self.horizontalLayout.addWidget(self.pushButton__delete_file)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton__change_content = QPushButton(Form_2)
        self.pushButton__change_content.setObjectName(u"pushButton__change_content")

        self.horizontalLayout.addWidget(self.pushButton__change_content)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)


        self.retranslateUi(Form_2)

        QMetaObject.connectSlotsByName(Form_2)
    # setupUi

    def retranslateUi(self, Form_2):
        Form_2.setWindowTitle(QCoreApplication.translate("Form_2", u"file_exist", None))
        self.label__animal_name.setText(QCoreApplication.translate("Form_2", u"TextLabel", None))
        self.label__exist.setText(QCoreApplication.translate("Form_2", u"\ud30c\uc77c\uc774 \uc874\uc7ac\ud569\ub2c8\ub2e4.", None))
        self.pushButton__delete_file.setText(QCoreApplication.translate("Form_2", u"Delete file", None))
        self.pushButton__change_content.setText(QCoreApplication.translate("Form_2", u"Change content", None))
    # retranslateUi

