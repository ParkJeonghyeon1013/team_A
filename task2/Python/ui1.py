
import sys
import os
import pathlib

from PySide2 import QtWidgets

import importlib
import ui2
import ui3

from task1.save_search_animal import SearchAndSave
from task2.Qt import animal_farm_1_ui, animal_farm_2_ui, animal_farm_3_ui

importlib.reload(animal_farm_1_ui)


class Main(QtWidgets.QWidget, SearchAndSave, animal_farm_1_ui.Ui_Form_main, animal_farm_2_ui.Ui_Form_2):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)

        self.__ui2 = ui2.UI_2()
        self.__ui3 = ui3.UI_3()
        self.setupUi(self)
        self._signal_func()

# TODO line edit에 적은 문자열을 Search 버튼 누르면
    def _signal_func(self):
        self.toolButton__main_select_path.clicked.connect(self.set_path_label)
        self.pushButton__main_animal_search.clicked.connect(self.get_info)
        # self.QtWidgets.QFileDialog.fileSelected(self.)


    def get_info(self):
        a = self.get_anim_name()
        self.get_anim_sound()
        self.show_ui2()
        self.set_ui2_label(a)

    def set_ui2_label(self, a_name: str):
        print(a_name)
        self.__ui2.set_label2(a_name)




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

    # animList.txt 제외한 디렉토리에 있는 파일명 리스트로 받기
    def get_files_Path(self, fpath: pathlib.Path) -> list:
        dir_name_list = list()
        for i in fpath.glob('*.txt'):
            i = i.as_posix()
            temp = i.replace(fpath.as_posix(), '')
            # file_animName = file_animName.lstrip('/').rstrip('.txt')
            temp = temp.lstrip('/')
            file_anim_name, exr = os.path.splitext(temp)
            dir_name_list.append(file_anim_name)
        return dir_name_list

    #  내용 받는 함수
    def make_file_list(self, fpath: pathlib.Path) -> list:
        file_list = list()
        file_name_list = self.get_files_Path(fpath)
        path_list = list(fpath.glob('*.txt'))

        for num in range(len(path_list)):
            if file_name_list[num] == 'animList':
                continue
            with open(path_list[num].as_posix(), 'r', encoding='UTF8') as f:
                sound = f.readline()
            file_list.append([file_name_list[num], sound])
        print(file_list)
        return file_list

    # animList.txt 안에 file_list 저장
    def write_fileName_to_animList(self, fpath: pathlib.Path) -> None:
        animList_path = pathlib.Path(f'{fpath}/animList.txt')
        dir_list = self.make_file_list(fpath)
        with open(animList_path.as_posix(), 'w', encoding='UTF8') as f:
            for i in range(len(dir_list)):
                f.write(f'{dir_list[i][0]} / {dir_list[i][1]}\n')

    def get_anim_sound(self):
        a_sound = self.lineEdit__main_animal_sound.text()
        # print(a_sound)
        return a_sound

    def set_dir(self) -> pathlib.Path:
        files = QtWidgets.QFileDialog.getExistingDirectory(
            self,
            'Get directory',
            '~/'
        )
        # self.label__path.text(files)
        fpath = files
        fpath = pathlib.Path(fpath)
        return fpath

        # self.label__path.setText(fpath)

    def dir_to_str(self, fpath: pathlib.Path) -> str:
        fpath = fpath.as_posix()
        print(fpath)
        return fpath

    def set_path_label(self) -> None:
        fpath = self.set_dir()
        str_path = self.dir_to_str(fpath)
        self.label__path.setText(str_path)
        self.write_fileName_to_animList(fpath)






if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    cus = Main()
    cus.show()
    sys.exit(app.exec_())
