import sys
import os
import logging
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog
from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot, pyqtSignal

# logging 설정
logging.basicConfig(
        level = logging.INFO,
        datefmt = '%Y/%m/%d %I:%M:%S %p',
        format = "%(asctime)s [%(levelname)s] - %(message)s "
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
xpaMainWindowUI = uic.loadUiType('UI/main.ui')[0]
workSpaceWindowUI = uic.loadUiType('UI/workspace.ui')[0]


class WorkSpaceWindow(QWidget, workSpaceWindowUI):
    """
    실제로 사진 작업이 이루어지는 공간
    """
    def __init__(self, xpaInfo):
        super().__init__()
        self.nxpaName, self.type, self.numSheet, self.numBlock = xpaInfo.values()

        self.setupUi(self)

        self.fileName_label.setText(self.nxpaName)

        # Sheet Buttons
        self.addSheet_pushButton.clicked.connect(self.addSheet_pushButtonClicked)
        self.removeSheet_pushButton.clicked.connect(self.removeSheet_pushButtonClicked)

        # Cell Buttons
        self.addCell_pushButton.clicked.connect(self.addCell_pushButtonClicked)
        self.removeCell_pushButton.clicked.connect(self.removeCell_pushButtonClicked)

    @pyqtSlot()
    def addSheet_pushButtonClicked(self):
        pass

    @pyqtSlot()
    def removeSheet_pushButtonClicked(self):
        pass

    @pyqtSlot()
    def addCell_pushButtonClicked(self):
        pass

    @pyqtSlot()
    def removeCell_pushButtonClicked(self):
        pass
    
class XpaMainWindow(QWidget, xpaMainWindowUI):
    """
    nxpa 파일을 만들거나 불러오는 공간
    """

    switch_window = pyqtSignal(dict)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        logging.info(f'NXPA Manager Start')

        self.loadNewXpa_pushButton.clicked.connect(self.loadNewXpa_pushButtonClicked)
        self.createNewXpa_pushButton.clicked.connect(self.createNewXpa_pushButtonClicked)

    @pyqtSlot()
    def loadNewXpa_pushButtonClicked(self):
        nxpaName, _ = QFileDialog.getOpenFileName(self, 'nxpa 파일 선택', BASE_DIR, "nxpa (*.nxpa)")

        if nxpaName:
            # 파일 불러오기:
            pass
        else:
            # 잘못된 파일이라고 팝업 dialog 띄우기
            pass
   
    @pyqtSlot()
    def createNewXpa_pushButtonClicked(self):
        logging.info(f'[createNewXpa_pushButtonClicked] Start')
        logging.info(f'[createNewXpa_pushButtonClicked] Text: {self.newXpaName_lineEdit.text()}')

        if self.newXpaName_lineEdit.text():

            xpaInfo = {}
            xpaInfo['nxpaName'] = self.newXpaName_lineEdit.text()
            xpaInfo['type'] = self.selectType_comboBox.currentText()
            xpaInfo['numSheet'] = self.numSheet_spinBox.value()
            xpaInfo['numBlock'] = self.numBlock_spinBox.value()

            self.switch_window.emit(xpaInfo)
            pass
        else:
            logging.warning(f'[createNewXpa_pushButtonClicked] No File Name')
            return

        logging.info(f'[createNewXpa_pushButtonClicked] Done')
    pass


class WindowController:
    """
    창을 변환하는 컨트롤러
    다음 창에 필요한 정보를 넘겨주거나 창을 띄우고 없애는 역할
    """
    def __init__(self):
        self.test = "test"
        pass

    def showXpaMainWindow(self):
        self.xpaMainWindow = XpaMainWindow()
        self.xpaMainWindow.switch_window.connect(self.showWorkSpaceWindow)
        self.xpaMainWindow.show()

    def showWorkSpaceWindow(self, xpaInfo):
        self.workSpaceWindow = WorkSpaceWindow(xpaInfo)
        self.xpaMainWindow.close()
        self.workSpaceWindow.show()



def main():
    app = QApplication(sys.argv)
    windowController = WindowController()
    windowController.showXpaMainWindow()
    app.exec_()


if __name__ == '__main__':
    main()
