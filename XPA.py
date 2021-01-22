import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog
from PyQt5 import uic


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
xpaMainWindowUI = uic.loadUiType('UI/main.ui')[0]

class XpaMainWindow(QWidget, xpaMainWindowUI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def loadNewXPA_pushButtonClicked(self):
        nxpaName = QFileDialog.getOpenFileName(self, 'nxpa 파일 선택', BASE_DIR, "nxpa (*.nxpa)")

        if nxpaName[0]:
            pass
        else:
            # 잘못된 파일이라고 팝업 dialog 띄우기
            pass

    def createNewXPA_pushButtonClicked(self):
        pass

    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    xpaWindow = XpaMainWindow()
    xpaWindow.show()
    app.exec_()
