"""PySide2 WebEngine QtQuick 2 Example"""

import os
from PySide2.QtCore import QUrl
from PySide2.QtQml import QQmlApplicationEngine
from PySide2.QtWidgets import QApplication
from PySide2.QtWebEngine import QtWebEngine

def main():
    app = QApplication([])
    QtWebEngine.initialize()
    engine = QQmlApplicationEngine()
    qml_file_path = os.path.join(os.path.dirname(__file__), 'browser.qml')
    qml_url = QUrl.fromLocalFile(os.path.abspath(qml_file_path))
    engine.load(qml_url)
    app.exec_()

if __name__ == '__main__':
    main()
