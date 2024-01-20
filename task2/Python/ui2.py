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
    def __init__(self, parent = None):
        super(UI_2, self).__init__(parent)

        self.__ui3 = ui3.UI_3()
        self.setupUi(self)
        # self._signal_func()
        self.set_label2(self)

    def __del__(self):
        pass

    # def _signal_func(self):
    #     self.pushButton__delete_file.clicked.connect(self.delete_file)
    #     self.pushButton__change_content.clicked.connect(self.change_file)



    # textlabel의 내용을 사용자 인풋으로 가져가기.
    def set_label2(self, a_name):
        self.label__animal_name.setText(f'{a_name}.txt')



    # TODO:
    #  파일 삭제
    def delete_file(self, fpath: pathlib.Path):
        print(fpath)
        fpath.unlink()
        print('\n삭제 버튼')

    # TODO:파일 내용 변경
    def change_file(self, fpath:pathlib.Path, animal_sound: str):
        print(fpath, animal_sound)
        with open(fpath.as_posix(), 'w', encoding='UTF8') as f:
            f.write(animal_sound)
        print('\n수정 버튼')



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui2 = UI_2()
    ui2.show()
    app.exec_()
