
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

        self.__path = pathlib.Path.home()
        self.__animal_name = ''
        self.__animal_sound = ''

        # self.__ui2 = ui2.UI_2()
        # self.__ui3 = ui3.UI_3()

        self.setupUi(self)
        self._signal_func()

    def __del__(self):
        pass

    # @property
    # def ui2(self):
    #     return self.__ui2
    #
    # @property
    # def ui3(self):
    #     return self.__ui3


# TODO line edit에 적은 문자열을 Search 버튼 누르면
    def _signal_func(self):
        self.toolButton__main_select_path.clicked.connect(self.set_path_label)
        self.pushButton__main_animal_search.clicked.connect(self.get_info)


        # self.QtWidgets.QFileDialog.fileSelected(self.)


    # ui2의 시그널
    # def _signal_func2(self):
    #     txt_path = pathlib.Path(f'{self.__path.as_posix()}/{self.__animal_name}.txt')
    #     print(txt_path)
    #     self.__ui2.set_label2(self.__animal_name)
    #     self.__ui2.pushButton__delete_file.clicked.connect(self.__ui2.delete_file(txt_path))
    #     self.__ui2.pushButton__change_content.clicked.connect(self.__ui2.change_file(txt_path, self.__animal_sound))

    # ui3의 시그널
    def get_info(self) -> None:
        self.get_anim_name()
        self.get_anim_sound()
        txt_path = pathlib.Path(f'{self.__path.as_posix()}/{self.__animal_name}.txt')

        # file이 존재할 때 UI2
        if self.check_file_exist() is True:
            self.ui2 = ui2.UI_2(txt_path, self.__animal_name, self.__animal_sound)
            self.ui2.show()

            # self.__ui2.pushButton__change_content.clicked.connect(self.__ui2.delete_file(txt_path))
            # self.__ui2.pushButton__delete_file.clicked.connect(self.__ui2.change_file(txt_path, self.__animal_sound))
            # self._signal_func2()

        # file이 존재하지 않을 때 UI3
        else:
            self.ui3 = ui3.UI_3(self.__path, self.__animal_sound)
            self.ui3.show()
            self.set_ui3_label(self.__animal_name)
            print(txt_path)
            self.__ui3.save_animal_file(txt_path, self.__animal_sound)


    def set_ui3_label(self, a_name: str):
        print(a_name)
        self.__ui3.set_label3(a_name)

    def set_ui2_label(self, a_name: str):
        print(a_name)
        self.__ui2.set_label2(a_name)

        # # a_name
        # a_name = self.get_anim_name()
        # self.__ui2.set_label(a_name)
        # self.__ui2.label__animal_name.setText(f'{a_name}.txt')


    # 파일 이름이 있는지 확인해서 true / false 리턴
    def check_file_exist(self) -> bool:
        filename_lst = self.get_files_Path(self.__path)
        for file in filename_lst:
            print(file)
            print(self.__animal_name)
            if file == self.__animal_name:
                return True
            elif file == 'animList':
                continue
        return False

    # test 사용자에게 받은 값 리턴
    def push_user_input(self):
        input_lst = [self.__path, self.__animal_name, self.__animal_sound]
        return input_lst



    # TODO: 파일 내용이 똑같으면 저장하지 않고 끝내는 안내 보여줄까?


    # UI2 보여주는 method
    def show_ui2(self):
        self.__ui2.show()

    #  UI3 보여주는 method
    def show_ui3(self):
        self.__ui3.show()

    def close_ui2(self):
        self.__ui2.close()

    def close_ui3(self):
        self.__ui3.close()

    # 사용자에게 받은 animal name __animal_name에 저장하는 함수
    def get_anim_name(self):
        a_name = self.lineEdit__main_animal_name.text()
        self.__animal_name = a_name
        return a_name

    # 사용자에게 받은 animal sound를 __animal_sound에 저장하는 함수
    def get_anim_sound(self):
        a_sound = self.lineEdit__main_animal_sound.text()
        self.__animal_sound = a_sound
        return a_sound

    # Dialog를 통해 사용자에게 경로를 받아 __path 에 저장하는 함수
    def set_dir(self) -> pathlib.Path:
        files = QtWidgets.QFileDialog.getExistingDirectory(
            self,
            'Get directory',
            '~/'
        )
        # self.label__path.text(files)
        fpath = files
        fpath = pathlib.Path(fpath)
        self.__path = fpath
        return fpath


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

    #  사용자가 선택한 디렉토리 안의 txt 파일 속 내용을 리스트로 받아 리턴하는 함수
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

    # animList.txt 안에 file_list를 [[파일 이름, 내용], []] 형태로 저장
    def write_fileName_to_animList(self, fpath: pathlib.Path) -> None:
        animList_path = pathlib.Path(f'{fpath}/animList.txt')
        dir_list = self.make_file_list(fpath)
        with open(animList_path.as_posix(), 'w', encoding='UTF8') as f:
            for i in range(len(dir_list)):
                f.write(f'{dir_list[i][0]} / {dir_list[i][1]}\n')



        # self.label__path.setText(fpath)

    def dir_to_str(self, fpath: pathlib.Path) -> str:
        fpath = fpath.as_posix()
        print(fpath)
        return fpath

    def get_path(self) -> str:
        fpath = self.set_dir()
        str_path = self.dir_to_str(fpath)
        return str_path

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
