from Infrastructure.DataAccess.FilePath import blankPileUi
from UseCases.General.DefaultDeck import DefaultDeck
from View.StackWidget import StackWidget
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5 import uic
import sys

class Signals(QObject):
    dropCard = pyqtSignal(str, int)

class EmptyStackWidget(QWidget):
    def __init__(self, deck, mouseTracking=True,parent=None):
        super(EmptyStackWidget, self).__init__(parent)
        self.Layout = QVBoxLayout(self)
        self.ui = uic.loadUi(blankPileUi)
        self.StackWidget = StackWidget(deck, self)
        self.deck = deck

        self.signals = Signals()

        self.Layout.addWidget(self.ui)
        self.Layout.addWidget(self.StackWidget)

        self.Layout.setContentsMargins(0, 0, 0, 0)
        self.setMinimumSize(self.ui.minimumSize())
        self.setLayout(self.Layout)

        self.setAcceptDrops(True)

    def dragEnterEvent(self, a0) -> None:
        a0.accept()

    def dropEvent(self, a0) -> None:
        self.signals.dropCard.emit(a0.mimeData().text().split("/")[0], int(a0.mimeData().text().split("/")[1]))
        a0.accept()

    def refresh(self):
        if not self.deck.isEmpty():
            self.StackWidget.refresh()


    def show(self) -> None:
        if self.deck.isEmpty():
            self.ui.show()
            self.StackWidget.hide()
        else:
            self.ui.hide()
            self.StackWidget.show()
        super(EmptyStackWidget, self).show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    deck = DefaultDeck()
    deck.makeDefaultSequence()
    deck.makeRandomSequence()
    window = EmptyStackWidget(deck)
    window.show()
    sys.exit(app.exec())