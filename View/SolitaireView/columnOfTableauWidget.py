from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout
from UseCases.SolitaireLogic.columnOfTableau import ColumnOfTableau
from PyQt5.QtCore import QObject, pyqtSignal
from Entities.Deck import Deck
from View.EmptyStackWidget import EmptyStackWidget
import sys

class Signals(QObject):
    dropCard = pyqtSignal(Deck, str, int)

class ColumnOfTableauWidget(QWidget):
    def __init__(self, ColumnOfTableau, parent=None):
        super(ColumnOfTableauWidget, self).__init__(parent)

        self.ColumnOfTableau = ColumnOfTableau

        self.signals = Signals()

        self.EmptyStackWidget = EmptyStackWidget(self.ColumnOfTableau, self)
        self.EmptyStackWidget.signals.dropCard.connect(self.dropCard)
        self.setLayout(QHBoxLayout(self))
        self.layout().addWidget(self.EmptyStackWidget)
        self.layout().setContentsMargins(0, 0, 0, 0)

        self.setAcceptDrops(True)

    def dropCard(self, rank, mark):
        self.signals.dropCard.emit(self.ColumnOfTableau, rank, mark)

    def refresh(self):
        self.EmptyStackWidget.refresh()

    def dragEnterEvent(self, a0) -> None:
        a0.accept()

    def dropEvent(self, a0) -> None:
        a0.accept()

    def show(self) -> None:
        self.EmptyStackWidget.show()
        super(ColumnOfTableauWidget, self).show()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = ColumnOfTableauWidget()
    window.show()
    sys.exit(app.exec())