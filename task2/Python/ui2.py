import sys

from PySide2 import QtWidgets

import importlib


sys.path.append('/task2/Qt')

# import animal_farm_3_ui
from task2.Qt import animal_farm_2_ui

importlib.reload(animal_farm_2_ui)
import ui1
import ui3

from task1.save_search_animal import *

class UI_2(QtWidgets.QWidget, animal_farm_2_ui.Ui_Form_2):
    def __init__(self, parent = None):
        super(UI_2, self).__init__(parent)

        self.__ui3 = ui3.UI_3()
        self.setupUi(self)
        # self.set_label2(self)

    # textlabel의 내용을 사용자 인풋으로 가져가기.
    def set_label2(self, a_name):
        print(a_name)
        # a_name = '멍멍'
        self.label__animal_name.setText(f'{a_name}.txt')




#
# if __name__ == '__main__':
#     app = QtWidgets.QApplication(sys.argv)
#     ui2 = UI_2()
#     ui2.show()
#     app.exec_()
