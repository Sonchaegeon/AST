from kiwoom.kiwoom import *

import sys
from PyQt5.QtWidgets import *


class UI_class():
    def __init__(self):
        print('UI class')

        self.app = QApplication(sys.argv)

        Kiwoom()

        self.app.exec_()
