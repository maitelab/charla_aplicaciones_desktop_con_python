"""Ejemplo pyside2 con webview mostrando un reloj"""
from os import path
import os
import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QAction, QMessageBox,  QWidget, QHBoxLayout, QInputDialog, QLineEdit, QListWidgetItem,\
    QListWidget, QVBoxLayout
from PySide2.QtGui import QIcon

from PySide2.QtWebEngineWidgets import QWebEngineView
from PySide2.QtCore import QUrl
from PySide2.QtCore import QObject, Slot
from PySide2.QtWebChannel import QWebChannel

class MaiteBody(QWidget):
    """Main display body"""

    def __init__(self):
        super().__init__(None)
     
        # main horizontal view
        hlay = QHBoxLayout()

        # left pane
        e1 = QLineEdit()
        hlay.addWidget(e1, 25)

        # right pane
        self.webEngineView = QWebEngineView()
        current_path = os.getcwd()
        fileLocation = current_path + "/reloj.html"
        print(fileLocation)
        url = QUrl.fromLocalFile(fileLocation)

        self.webPage = self.webEngineView.page()

        self.webEngineView.load(url)
        self.webEngineView.show()
        hlay.addWidget(self.webEngineView, 75)

        self.setLayout(hlay)
            
class Notepad(QMainWindow):
    """Main Window to hold all other widgets and menu"""

    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 800, 800)
        self.setWindowTitle('Ejemplo reloj')

        # main view
        self.mainBody = MaiteBody()
        self.setCentralWidget(self.mainBody)

        # self.showMaximized()         
        
        self.show()

# Run program
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Notepad()
    sys.exit(app.exec_())
