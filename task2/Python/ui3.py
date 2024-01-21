import sys

from PySide2 import QtWidgets

import importlib


sys.path.append('/task2/Qt')

# import animal_farm_3_ui
from task2.Qt import animal_farm_3_ui

importlib.reload(animal_farm_3_ui)

class UI_3(QtWidgets.QWidget, animal_farm_3_ui.Ui_Form):
    def __init__(self, fpath, a_sound, parent = None):
        super(UI_3, self).__init__(parent)

        self.__fpath = fpath
        self.__a_sound = a_sound

        self.setupUi(self)
        # self.set_label3()

    @property
    def fpath(self):
        fpath = self.__fpath
        return fpath

    @property
    def a_sound(self):
        a_sound = self.__a_sound
        return a_sound



    # textlabel의 내용을 사용자 인풋으로 가져가기.
    def set_label3(self):
        self.label__animal_name.setText(f'{self.a_sound}.txt')



    # savefile 구현
    def save_animal_file(self):
        with open(self.fpath, 'w', encoding='UTF8') as f:
            f.write(self.a_sound)



    # list 안에 든 내용 읽어오기
    def write_animlist_in_(self):
        lst = ['0','a','f']
        self.textBrowser_animlist_view.setText(str(lst))



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui3 = UI_3()
    ui3.show()
    app.exec_()
