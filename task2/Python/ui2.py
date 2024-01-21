import pathlib
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
    def __init__(self, fpath, a_name, a_sound, parent=None):
        super(UI_2, self).__init__(parent)

        self.__fpath = fpath
        self.__a_name = a_name
        self.__a_sound = a_sound

        # self.__ui3 = ui3.UI_3()
        self.setupUi(self)
        self.set_label2()

        # self.__ui1 = ui1.Main
        self._signal_func2()

    @property
    def fpath(self):
        fpath = self.__fpath
        return fpath
    @property
    def a_name(self):
        a_name = self.__a_name
        return a_name

    @property
    def a_sound(self):
        a_sound = self.__a_sound
        return a_sound

    def __del__(self):
        pass

    def _signal_func2(self):
        self.pushButton__delete_file.clicked.connect(self.delete_file)
        self.pushButton__change_content.clicked.connect(self.change_file)



    # textlabel의 내용을 사용자 인풋으로 가져가기.
    def set_label2(self):
        self.label__animal_name.setText(f'{self.a_name}.txt')



    # TODO: 파일 삭제
    def delete_file(self):
        print('\n삭제 버튼')
        print(self.fpath)
        self.fpath.unlink()

    # TODO:파일 내용 변경
    def change_file(self):
        print('\n수정 버튼')
        print(self.fpath, self.a_sound)
        with open(self.fpath.as_posix(), 'w', encoding='UTF8') as f:
            f.write(self.a_sound)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # # ui2 = UI_2()
    # ui2.show()
    # app.exec_()
