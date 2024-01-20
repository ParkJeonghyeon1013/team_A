
import sys
import pathlib

from PySide2 import QtWidgets

import importlib
import ui2

from task2.Qt import animal_farm_1_ui

importlib.reload(animal_farm_1_ui)


class Main(QtWidgets.QWidget, animal_farm_1_ui.Ui_Form_main):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.__ui2 = ui2.UI_2()
        self.setupUi(self)
        self._signal_func()

# TODO line edit에 적은 문자열을 Search 버튼 누르면
    def _signal_func(self):
        self.toolButton__main_select_path.clicked.connect(self.set_label)
        self.pushButton__main_animal_search.clicked.connect(self.get_info)

    def get_info(self):
        self.get_anim_name()
        self.get_anim_sound()

        self.__ui2.show()



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
