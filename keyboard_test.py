import sys

from PyQt5.QtWidgets import QApplication

from PyQt5.QtWidgets import QVBoxLayout

from PyQt5.QtWidgets import QWidget

from keyboard_full.WKeyboard import LineEdit
from keyboard_full.WKeyboard import WKeyboard


class MainWindow(QWidget):

    def __init__(self):

        super(MainWindow, self).__init__()

        self.layout = QVBoxLayout()

        self.setLayout(self.layout)

        self.text_edit = LineEdit(self)

        self.layout.addWidget(self.text_edit)

        self.kb = WKeyboard()

        self.kb.set_receiver(self.text_edit)



    def closeEvent(self, QCloseEvent):

        self.kb.close()

        super(MainWindow, self).closeEvent(QCloseEvent)



if __name__ == "__main__":

    app = QApplication(sys.argv)

    mw = MainWindow()

    mw.show()

    sys.exit(app.exec())