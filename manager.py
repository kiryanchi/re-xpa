import sys
import os
import logging
import openpyxl
import openpyxl_image_loader
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QMainWindow, QTabBar, QTabWidget, QScrollArea, QTableWidget, QHeaderView, QAbstractItemView
from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5 import QtCore

# logging 설정
logging.basicConfig(
        level = logging.INFO,
        datefmt = '%Y/%m/%d %I:%M:%S %p',
        format = "%(asctime)s [%(levelname)s] - %(message)s "
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
managerUI = uic.loadUiType('UI/manager.ui')[0]

class SheetInnerTableWidget(QTableWidget):
    def __init__(self):
        super().__init__(5, 1)
        self.setAcceptDrops(True)
        self.setAlternatingRowColors(True)
        self.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.insertRow(self.rowCount())


class ManagerMainWindow(QMainWindow, managerUI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    
        self.addSheet_pushButton.clicked.connect(self.addSheet_pushButtonClicked)
        self.removeSheet_pushButton.clicked.connect(self.removeSheet_pushButtonClicked)
        self.addCell_pushButton.clicked.connect(self.addCell_pushButtonClicked)
        self.removeCell_pushButton.clicked.connect(self.removeCell_pushButtonClicked)

        self.open_action.triggered.connect(self.open_actiontriggered)
        self.save_action.triggered.connect(self.save_actiontriggered)
        self.saveas_action.triggered.connect(self.saveas_actiontriggered)

        self.undo_action.triggered.connect(self.undo_actiontriggered)
        self.redo_action.triggered.connect(self.redo_actiontriggered)
        self.copy_action.triggered.connect(self.copy_actiontriggered)
        self.paste_action.triggered.connect(self.paste_actiontriggered)
        self.delete_action.triggered.connect(self.delete_actiontriggered)


    @pyqtSlot()
    def addSheet_pushButtonClicked(self):
        self._addSheet_('새 탭')

    @pyqtSlot()
    def removeSheet_pushButtonClicked(self):
        self._removeSheet_()

    @pyqtSlot()
    def addCell_pushButtonClicked(self):
        self._addCell_()

    @pyqtSlot()
    def removeCell_pushButtonClicked(self):
        self._removeCell_()

    @pyqtSlot()
    def open_actiontriggered(self):
        fileName = QFileDialog.getOpenFileName(self, 'xlsx file', './', 'Excel Files(*.xlsx)')
        logging.info(fileName[0])
        self.fileName_label.setText(fileName[0].split('/')[-1])


    def _addSheet_(self, text):
        self.sheetList_tabWidget.addTab(SheetInnerTableWidget(), text + f'{self.sheetList_tabWidget.count()}')

    def _addCell_(self):
        pass

    def _removeSheet_(self):
        self.sheetList_tabWidget.removeTab(self.sheetList_tabWidget.currentIndex())

    def _removeCell(self):
        pass

    def _openExcel(self):
        fileName = QFileDialog.getOpenFileName(self, 'xlsx file', './', 'Excel Files(*.xlsx)')
        logging.info(fileName[0])
        self.fileName_label.setText(fileName[0].split('/')[-1])

    @pyqtSlot()
    def save_actiontriggered(self):
        pass

    @pyqtSlot()
    def saveas_actiontriggered(self):
        pass
    
    @pyqtSlot()
    def undo_actiontriggered(self):
        pass

    @pyqtSlot()
    def redo_actiontriggered(self):
        pass

    @pyqtSlot()
    def copy_actiontriggered(self):
        pass
    
    @pyqtSlot()
    def paste_actiontriggered(self):
        pass

    @pyqtSlot()
    def delete_actiontriggered(self):
        pass


class WindowController:
    """
    창을 변환하는 컨트롤러
    다음 창에 필요한 정보를 넘겨주거나 창을 띄우고 없애는 역할
    """
    def __init__(self):
        self.test = "test"
        pass

    def showManagerMainWindow(self):
        self.managerMainWindow = ManagerMainWindow()
        self.managerMainWindow.show()

#    def showXpaMainWindow(self):
#        self.xpaMainWindow = XpaMainWindow()
#        self.xpaMainWindow.switch_window.connect(self.showWorkSpaceWindow)
#        self.xpaMainWindow.show()
#
#    def showWorkSpaceWindow(self, xpaInfo):
#        self.workSpaceWindow = WorkSpaceWindow(xpaInfo)
#        self.xpaMainWindow.close()
#        self.workSpaceWindow.show()



def main():
    app = QApplication(sys.argv)
    windowController = WindowController()
    windowController.showManagerMainWindow()
    app.exec_()


if __name__ == '__main__':
    main()
