from View.CardWidget import CardWidget
from PyQt5.QtWidgets import QApplication, QWidget

import sys

class Area(QWidget):
    def __init__(self, parent=None):
        super(Area, self).__init__(parent)

        self.card = CardWidget(parent=self)
        self.card.setGeometry(0, 0, 120, 180)

        self.setAcceptDrops(True)

        self.setMinimumSize(400, 400)

    def dragEnterEvent(self, a0) -> None:
        a0.accept()

    def dropEvent(self, a0) -> None:
        position = a0.pos()
        self.card.move(position)
        a0.accept()

    def show(self) -> None:
        self.card.show()
        super(Area, self).show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Area()

    window.show()
    sys.exit(app.exec())
