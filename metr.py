import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QLabel, QApplication


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('metr.ui', self)
        self.setWindowTitle('Арифмометр')
        self.show()
        self.pushButton.clicked.connect(self.clickBtn1)
        self.pushButton_2.clicked.connect(self.clickBtn2)
        self.pushButton_3.clicked.connect(self.clickBtn3)

    def clickBtn1(self):
        self.a = int(self.lineEdit.text())
        self.b = int(self.lineEdit_2.text())
        self.lineEdit_3.setText(str(self.a + self.b))

    def clickBtn2(self):
        self.a = int(self.lineEdit.text())
        self.b = int(self.lineEdit_2.text())
        self.lineEdit_3.setText(str(self.a - self.b))

    def clickBtn3(self):
        self.a = int(self.lineEdit.text())
        self.b = int(self.lineEdit_2.text())
        self.lineEdit_3.setText(str(self.a * self.b))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
