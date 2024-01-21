import os
import sys
from PySide2 import QtWidgets,QtCore
from PySide2.QtCore import Signal
import importlib
from task2.Qt import animal_farm_2_ui,animal_farm_4_ui
sys.path.append('/task2/Qt')
importlib.reload(animal_farm_2_ui)
import ui1
import ui3
import ui4

class UI_2(QtWidgets.QWidget, animal_farm_2_ui.Ui_Form_2):
    ui4_requested = QtCore.Signal()
    def __init__(self, inst=None, parent=None, directory_path=None):
        super(UI_2, self).__init__(parent)
        self.setupUi(self)

        self.__p = inst

        self.__ui3 = ui3.UI_3()
        self.__ui4 = ui4.UI_4()
        self.pushButton__delete_file.clicked.connect(self.delete_file)
        self.directory_path = directory_path

    def delete_file(self):
        directory_path = self.__p.label__path.text()  # ui1의 경로 정보를 가져옵니다.
        file_name = '{0}/{1}.txt'.format(
            directory_path, self.label__animal_name.text().split('/')[0].strip()
        )

        print('-0--------------------------------')
        print(file_name)
        print('-0--------------------------------')

        ui1.delete_file(file_name)
        # self.ui4_requested.emit()

    def get_parent_directory_path(self):
        # parent_widget = self.parent()
        # while parent_widget:
        #     if hasattr(parent_widget, 'label__path'):
        #         return parent_widget.label__path.text()
            # parent_widget = parent_widget.parent()
        # return ""
        return self.__p.label__path.text()
    #
    def set_ui2_label(self, mixname):
        print(mixname)
        self.label__animal_name.setText(mixname)

    def delete_info(self):
        print("동물 한마리가 멸종되었습니다.")

    def show_ui(self):
        self.show()

    def show_ui4(self):
        self.__ui4.show_ui()

    def hide_ui(self):
        self.hide()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()  # 메인 윈도우 생성
    ui2 = UI_2(main_window)  # UI_2 클래스 생성 시 메인 윈도우를 부모로 설정
    ui2.show()
    app.exec_()