# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'animal_farm_3.ui'
##
## Created by: Qt User Interface Compiler version 5.15.6
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
        Form.resize(371, 292)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label__animal_name = QLabel(Form)
        self.label__animal_name.setObjectName(u"label__animal_name")

        self.horizontalLayout.addWidget(self.label__animal_name)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label__newfile = QLabel(Form)
        self.label__newfile.setObjectName(u"label__newfile")
        self.label__newfile.setLayoutDirection(Qt.RightToLeft)

        self.horizontalLayout.addWidget(self.label__newfile)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.textBrowser_animlist_view = QTextBrowser(Form)
        self.textBrowser_animlist_view.setObjectName(u"textBrowser_animlist_view")

        self.verticalLayout.addWidget(self.textBrowser_animlist_view)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"animList", None))
        self.label__animal_name.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label__newfile.setText(QCoreApplication.translate("Form", u"\ud30c\uc77c\uc744 \uc0dd\uc131\ud569\ub2c8\ub2e4.", None))
    # retranslateUi

