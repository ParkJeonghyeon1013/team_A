# $HOME/Users/ijiyeong/Desktop/pyqt/houdini_api_with_qt
# 파일 위치 경로

import sys
import json
import pathlib

from PySide2 import QtWidgets, QtGui,QtCore

import importlib # 다른 모듈을 동적으로 다시 로드 하는데 사용

import hou

import custom_ui

importlib.reload(custom_ui)
# custom_ui 모듈을 다시 로드한다.
# 이렇게 하면 모듈이 변경될때 해당사항이 즉시 적용된다.


def deco_axis(axis): # deco func를 반환한다.
    def deco_func(func): # 데코레이터에 전달된 함수를 감싸는 wrapper 함수를 반환한다.
        def wrapper(self,val): # 이함수는 데코레이팅 된 함수의 동작을 확장한다.
            #print(val)
            #print(axis)
            pass
        return wrapper
    return deco_func

class Name:
    class Box:
        size = 'name_box_size'
    class Circle:
        radius = 'name_circle_rad'
        rotatey = 'name_circle_roty'
        division = 'name_circle_div'

    class Height:
        object = 'name_height_obj'
        handle = 'name_handle_obj'

class Entity:
    def __init__(self) -> None:
        self.__data = {
            Name.Box.size: [3.5,1.5,1.01],
            Name.Circle.radius:[5.25 , 5.25],
            Name.Circle.rotatey : 0,
            Name.Circle.division: 50,
            Name.Height.object : 20,
            Name.Height.handle : 3


        }
    @property
    def data(self) -> dict:
        return self.__data

    @data.setter
    def data(self, data:dict) -> None:
        if not isinstance(data, dict):
            return
        self.__data =data


class Custom(QtWidgets.QWidget, custom_ui.Ui_Form__widget): # 커스텀 클래스를 정의하고 괄호안에 있는 클래스를 상속한다.
    def __init__(self, parent=None):
        super(Custom, self).__init__(parent)

        self.__entity = Entity()
        self.setupUi(self)
        self.__node = hou.node('/obj/geo1/__CTRL__')
        self.set_parms()
        self._signal_func()  #  시그널 펑크 메서드를 호출해서 UI의 시그널 슬롯연결을 설정한다.

        self.pushButton__reset.setIcon(QtGui.QIcon(':/icon/baseline_clear_black_18dp.png'))
        print(self.load_file())

    # def __del__(self):
    #     print('result:',self.entity.data)
    #

        # custom 클래스의 초기화 메서드를 정의한다. 부모 위젯을 받을 수 있도록 설정하고
        # setupUI및 _ signal_func 메서드를 호출한다.
        # 부모 위젯을 받을 수 있도록 설정하고, UI를 설정하고, Houdini 노드를 초기화하고, 시그널 함수를 호출합니다

    def _signal_func(self): # UI의 시그널-슬롯 연결을 설정하는 메서드를 정의합니다.
        self.doubleSpinBox__boxsize_x.valueChanged.connect(self.slot_boxsize_x)
        self.doubleSpinBox__boxsize_y.valueChanged.connect(self.slot_boxsize_y)
        self.doubleSpinBox__boxsize_z.valueChanged.connect(self.slot_boxsize_z)

        self.doubleSpinBox__circle_rad_x.valueChanged.connect(self.slot_circlesize_x)
        self.doubleSpinBox__circle_rad_y.valueChanged.connect(self.slot_circlesize_y)

        self.horizontalSlider__circle_rot_y.valueChanged.connect(self.slot_circle_rotate_y)

        self.verticalSlider__ysize.valueChanged.connect(self.slot_height_object_y)

        self.pushButton__reset.clicked.connect(self.set_parms)


    #@deco_axis('x') # 데코레이터를 사용하여 slot_boxsize_x 메서드에 deco_axis('x')를 적용한다.

    @property
    def entity(self):
        return self.__entity


    def set_parms(self):
        self.doubleSpinBox__boxsize_x.setValue(self.entity.data.get(Name.Box.size)[0])
        self.doubleSpinBox__boxsize_y.setValue(self.entity.data.get(Name.Box.size)[1])
        self.doubleSpinBox__boxsize_z.setValue(self.entity.data.get(Name.Box.size)[2])

        self.doubleSpinBox__circle_rad_x.setValue(self.entity.data.get(Name.Circle.radius)[0])
        self.doubleSpinBox__circle_rad_y.setValue(self.entity.data.get(Name.Circle.radius)[1])

        self.horizontalSlider__circle_rot_y.setValue(self.entity.data.get(Name.Circle.rotatey))

        self.spinBox__circle_div.setValue(self.entity.data.get(Name.Circle.division))

        self.verticalSlider__ysize.setValue(self.entity.data.get(Name.Height.object))
        self.verticalSlider__handle_height.setValue(self.entity.data.get(Name.Height.handle))

    @staticmethod
    def get_file_path() -> pathlib.Path:
        file_path = pathlib.Path.home() / 'custom_ui.json'
        return file_path

    def write_file(self):
        with open(Custom.get_file_path().as_posix(),'wt') as fp:
            json.dump(self.get_parms(),fp)

    def load_file(self) -> dict:
        try:
            with open(Custom.get_file_path().as_posix(),'rt') as fp:
                return json.load(fp)
        except FileNotFoundError as err:
            print(err)
            return {}

    def get_parms(self):
        data = {
            Name.Box.size: [
                self.doubleSpinBox__boxsize_x.value(),
                self.doubleSpinBox__boxsize_y.value(),
                self.doubleSpinBox__boxsize_z.value()
                ],
            Name.Circle.radius: [
                self.doubleSpinBox__circle_rad_x.value(),
                self.doubleSpinBox__circle_rad_y.value()
                ],
            Name.Circle.rotatey: self.horizontalSlider__circle_rot_y.value(),
            Name.Circle.division: self.spinBox__circle_div.value(),
            Name.Height.object: self.verticalSlider__ysize.value(),
            Name.Height.handle: self.verticalSlider__handle_height.value()
        }
        return data

    @property
    def ctrl_node(self):
        if (self.__node is None) or (not isinstance(self.__node, hou.SopNode)):
            raise ValueError
        return self.__node

    #ctrl_node 속성의 getter로, 노드를 가져옵니다. 노드가 없거나 hou.SopNode의 인스턴스가 아니면 ValueError를 발생시킵니다.

    @ctrl_node.setter
    def ctrl_node(self,val):
        if (val is not None) and isinstance(val,hou.SopNode):
            self.__node = val
        else:
            raise ValueError

    # ctrl_node 속성의 setter로, 노드를 설정합니다. 설정하려는 값이 None이 아니고, hou.SopNode의 인스턴스인 경우에만 값을 설정합니다.
    # 그렇지 않으면 ValueError를 발생시킵니다.
    def slot_boxsize_x(self,val):
        self.ctrl_node.parm('_box_sizex').set(val)

    def slot_boxsize_y(self,val):
        print(val)

    def slot_boxsize_z(self,val):
        print(val)

    def slot_circlesize_x(self, val):
        print(val)

    def slot_circlesize_y(self, val):
        print(val)
    def slot_circle_rotate_y(self,val):
        print(val)

    def slot_height_object_y(self, val):
        self.ctrl_node.parm('handle_height').set(val)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    cus = Custom()
    cus.show()
    sys.exit(app.exec_())


''''
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv) #QApplication 객체를 생성합니다.
    cus = Custom() #Custom 클래스의 인스턴스를 생성합니다.
    cus.show() #생성한 인스턴스를 화면에 표시합니다.
    sys.exit(app.exec_()) #어플리케이션을 실행하고, 이벤트 루프를 시작합니다. 어플리케이션의 실행이 끝날 때까지 기다립니다.
'''