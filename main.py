import sys
from random import randint

from PyQt6 import uic
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QApplication, QMainWindow


class My_Circle(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)
        self.do_paint = False
        self.initUI()

    def initUI(self):
        self.btn.clicked.connect(self.click)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()
        self.do_paint = False

    def click(self):
        self.do_paint = True
        self.update()

    def draw(self, qp):
        d = randint(1, 200)
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(400, 150, d, d)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = My_Circle()
    ex.show()
    sys.exit(app.exec())
