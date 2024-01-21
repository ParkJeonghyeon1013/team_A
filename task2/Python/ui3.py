import sys
import pathlib
from PySide2 import QtWidgets

import importlib


sys.path.append('/task2/Qt')

# import animal_farm_3_ui
from task2.Qt import animal_farm_3_ui

importlib.reload(animal_farm_3_ui)

class UI_3(QtWidgets.QWidget, animal_farm_3_ui.Ui_Form):
    def __init__(self, fpath, a_name, a_sound, parent = None):
        super(UI_3, self).__init__(parent)

        self.__fpath = fpath
        self.__a_name = a_name
        self.__a_sound = a_sound

        self.setupUi(self)
        self.set_label3()
        self.save_animal_file()
        self.set_textBrowser()
        self.update_animList()
        # self.set_label3()

    @property
    def a_name(self):
        a_name = self.__a_name
        return a_name

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
        self.label__animal_name.setText(f'{self.a_name}.txt')


    # TODO: animList 불러와서 append


    # animList 불러와서 내용 리턴 받기
    def update_animList(self) -> list:
        animlist_path = pathlib.Path(f'{self.fpath}/animList.txt')
        content_lst = []
        print(animlist_path)
        with open(animlist_path.as_posix(), 'r', encoding='UTF8') as f:
            content_lst = f.readlines()
        return content_lst

    def set_textBrowser(self):
        content_lst = self.update_animList()
        content_lst.append(f'{self.a_name} / {self.a_sound}')
        self.textBrowser_animlist_view.append('[파일명] / [내용]')
        for line in content_lst:
            self.textBrowser_animlist_view.append(line)

        # self.textBrowser_animlist_view.append(lambda x: str(x), content_lst)
        # for i in content_lst:


    # savefile 구현
    def save_animal_file(self):
        txt_path = f'{self.fpath}/{self.a_name}.txt'
        with open(txt_path, 'w', encoding='UTF8') as f:
            f.write(self.a_sound)



    # # list 안에 든 내용 읽어오기
    # def write_animlist_in_(self):
    #     lst = ['0','a','f']
    #     self.textBrowser_animlist_view.setText(str(lst))



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui3 = UI_3()
    ui3.show()
    app.exec_()
