
import sys
import pathlib

from PySide2 import QtWidgets

import importlib
import ui2
import ui3

from task2.Qt import animal_farm_1_ui, animal_farm_2_ui, animal_farm_3_ui

importlib.reload(animal_farm_1_ui)


class Main(QtWidgets.QWidget, animal_farm_1_ui.Ui_Form_main, animal_farm_2_ui.Ui_Form_2):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.__ui2 = ui2.UI_2()
        self.__ui3 = ui3.UI_3()
        self.setupUi(self)
        self._signal_func()

# TODO line edit에 적은 문자열을 Search 버튼 누르면
    def _signal_func(self):
        self.toolButton__main_select_path.clicked.connect(self.set_label)
        self.pushButton__main_animal_search.clicked.connect(self.get_info)

    def get_info(self):
        a = self.get_anim_name()
        self.get_anim_sound()
        self.show_ui2()
        print(a)
        self.set_label(a)

    def set_label(self, a_name):
        # self.__ui2.set_label2(a_name)
        self.label__animal_name.setText(f'{a_name}.txt')

        # # a_name
        # a_name = self.get_anim_name()
        # self.__ui2.set_label(a_name)
        # self.__ui2.label__animal_name.setText(f'{a_name}.txt')


    def show_ui2(self):
        self.__ui2.show()

    def show_ui3(self):
        self.__ui3.show()


    def get_anim_name(self):
        a_name = self.lineEdit__main_animal_name.text()
        # print(a_name)
        return a_name

    def get_anim_sound(self):
        a_sound = self.lineEdit__main_animal_sound.text()
        # print(a_sound)
        return a_sound

    def set_dir(self) -> pathlib.Path:
        files = QtWidgets.QFileDialog.getOpenFileName(
            self,
            'Open File',
            '~/',
            'TEXT (*.txt)'
        )
        fpath = files[0]
        fpath = pathlib.Path(fpath)
        return fpath

        # self.label__path.setText(fpath)

    def dir_to_str(self, fpath: pathlib.Path)-> str:
        fpath = fpath.as_posix()
        return fpath

    def set_label(self):
        fpath = self.dir_to_str(self.set_dir())
        self.label__path.setText(fpath)






if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    cus = Main()
    cus.show()
    sys.exit(app.exec_())
