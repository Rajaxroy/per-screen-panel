import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQml import QQmlApplicationEngine

app = QApplication(sys.argv)

engine = QQmlApplicationEngine()
engine.load("panel/Main.qml")

if not engine.rootObjects():
    sys.exit(-1)

sys.exit(app.exec_())
