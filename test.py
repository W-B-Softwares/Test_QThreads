

from PyQt5.QtCore import QThread
import sys
import time

from PyQt5.QtWidgets import QMainWindow, QApplication


class MyThread(QThread):
    def __init__(self, target=None):
        super().__init__()
        self.target = target
    
    def run(self):
        if self.target:
            self.target()

# GUI FILE
class MainWindow(QMainWindow): # <--  from main import MainWindow
    def __init__(self):
        QMainWindow.__init__(self)
        
        self.setWindowTitle("Test QThreads")

        UIFunctions.uiDefinitions(self)

        self.show()


class UIFunctions(MainWindow):

    def uiDefinitions(self):
        UIFunctions.test_func_01(self)
        UIFunctions.test_func_02(self)

    def test_func_01(self):
        def test_th():
            time.sleep(2)
            print("Test 1")
        
        t = MyThread(target=test_th)
        t.start()

    def test_func_02(self):
        print("Test 2")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Windows')
    window = MainWindow()
    app.exec_()
    
