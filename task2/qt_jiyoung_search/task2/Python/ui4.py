import sys
from PySide2 import QtWidgets
from task2.Qt import animal_farm_4_ui
import ui1
import ui3

class UI_4(QtWidgets.QWidget, animal_farm_4_ui.Ui_Form):
    def __init__(self, parent=None):
        super(UI_4, self).__init__(parent)
        self.__ui3 = ui3.UI_3()
        self.setupUi(self)
        self.animal_delete_ok_btn.clicked.connect(self.delete_info_and_close)

    def set_ui2_label(self, mixname):
        print(mixname)
        self.animal_delete_note.setTitle(mixname)

    def delete_info_and_close(self):
        self.animal_delete_btn.setPlainText("동물 한마리가 멸종되었습니다.")
        self.close()

    def show_ui(self):
        self.show()

    def hide_ui(self):
        self.hide()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui4 = UI_4()
    ui4.show()
    app.exec_()
