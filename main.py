import sys
from random import randint

from Ui import Ui_MainWindow
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QApplication, QMainWindow


class My_Circle(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.do_paint = False
        self.initUI()

    def initUI(self):
        self.ui.btn.clicked.connect(self.click)

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
        r, g, b = randint(0, 255), randint(0, 255), randint(0, 255)
        d = randint(1, 200)
        qp.setBrush(QColor(r, g, b))
        qp.drawEllipse(400, 150, d, d)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = My_Circle()
    ex.show()
    sys.exit(app.exec())
