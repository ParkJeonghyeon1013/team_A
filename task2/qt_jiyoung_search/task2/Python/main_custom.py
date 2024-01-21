
import sys
import pathlib

from PySide2 import QtWidgets, QtGui, QtCore

import importlib

import animal_farm_1_ui

importlib.reload(animal_farm_1_ui)


class Main(QtWidgets.QWidget, animal_farm_1_ui.Ui_Form_main):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)

# TODO line edit에 적은 문자열을 Search 버튼 누르면
    def _signal_func(self):
        self.toolButton__main_select_path.clicked(self.set_dir)
        self.pushButton__main_animal_search.clicked(self.get_anim_name, self.get_anim_sound)

    def get_anim_name(self):
        a_name = self.lineEdit__main_animal_name.text()
        return a_name

    def get_anim_sound(self):
        a_sound = self.lineEdit__main_animal_sound.text()
        return a_sound

    def set_dir(self):
        files = QtWidgets.QFileDialog.getOpenFileName(
            self,
            'Open File',
            '~/',
            'TEXT (*.txt)'
        )
        fpath = files[0]
        fpath = pathlib.Path(fpath)
        self.label__path.setText(fpath)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    cus = Main()
    cus.show()
    sys.exit(app.exec_())
