import sys
from PySide2 import QtWidgets
from task2.Qt import animal_farm_2_ui, animal_farm_4_ui
import ui3
import ui4

class UI_2(QtWidgets.QWidget, animal_farm_2_ui.Ui_Form_2):
    def __init__(self, parent=None):
        super(UI_2, self).__init__(parent)
        self.__ui3 = ui3.UI_3()
        self.setupUi(self)
        self.__ui4 = ui4.UI_4()  # UI_4 클래스 인스턴스 생성

        # 새로운 코드: 삭제 버튼과 연결
        self.pushButton__delete_file.clicked.connect(self.delete_info)

    def set_ui2_label(self, mixname):
        print(mixname)
        self.label__animal_name.setText(mixname)

    def delete_info(self):
        print("동물 한마리가 멸종되었습니다.")
        self.__ui4.show_ui()  # delete 버튼을 클릭하면 UI_4를 실행

    def show_ui(self):
        self.show()

    def hide_ui(self):
        self.hide()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui2 = UI_2()
    ui2.show()
    app.exec_()
