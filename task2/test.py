import sys
from PySide2.QtWidgets import QWidget, QApplication, QMessageBox, QPushButton, QVBoxLayout


class MyForm(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        button = QPushButton("Open MessageBox")
        button.clicked.connect(self.showMessageBox)
        main_layout = QVBoxLayout()
        main_layout.addWidget(button)
        self.setLayout(main_layout)

    def showMessageBox(self):
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Title of MessageBox")
        msgBox.setText("Contents of MessageBox")
        msgBox.setInformativeText("InformativeText")
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Discard | QMessageBox.Cancel)
        msgBox.setDefaultButton(QMessageBox.Ok)

        result = msgBox.exec()
        if result == QMessageBox.Ok:
            print("OK")
        elif result == QMessageBox.Cancel:
            print("Cancel")
        elif result == QMessageBox.Discard:
            print("Discard")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MyForm()
    form.show()
    app.exec_()