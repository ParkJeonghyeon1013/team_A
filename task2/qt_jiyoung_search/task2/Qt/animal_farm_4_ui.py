# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'animal_farm_4.ui'
##
## Created by: Qt User Interface Compiler version 5.15.8
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(296, 166)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.animal_delete_note = QGroupBox(Form)
        self.animal_delete_note.setObjectName(u"animal_delete_note")
        self.animal_delete_btn = QPlainTextEdit(self.animal_delete_note)
        self.animal_delete_btn.setObjectName(u"animal_delete_btn")
        self.animal_delete_btn.setGeometry(QRect(20, 40, 201, 31))
        self.animal_delete_ok_btn = QPushButton(self.animal_delete_note)
        self.animal_delete_ok_btn.setObjectName(u"animal_delete_ok_btn")
        self.animal_delete_ok_btn.setGeometry(QRect(70, 90, 113, 32))

        self.verticalLayout.addWidget(self.animal_delete_note)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.animal_delete_note.setTitle(QCoreApplication.translate("Form", u"GroupBox", None))
        self.animal_delete_btn.setPlainText(QCoreApplication.translate("Form", u"\ub3d9\ubb3c \ud55c \ub9c8\ub9ac\uac00 \uba78\uc885\ub418\uc5c8\uc2b5\ub2c8\ub2e4.", None))
        self.animal_delete_ok_btn.setText(QCoreApplication.translate("Form", u"ok", None))
    # retranslateUi

