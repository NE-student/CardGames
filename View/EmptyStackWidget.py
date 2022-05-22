from Infrastructure.DataAccess.FilePath import blankPileUi
from UseCases.General.StartedDeck import StartedDeck, EmptyDeck
from View.StackWidget import StackWidget
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt5 import uic
import sys


class EmptyStackWidget(QWidget):
    def __init__(self, deck, mouseTracking=True,parent=None):
        super(EmptyStackWidget, self).__init__(parent)
        self.Layout = QVBoxLayout(self)
        self.ui = uic.loadUi(blankPileUi)
        self.StackWidget = StackWidget(deck, self)
        self.deck = deck

        self.Layout.addWidget(self.ui)
        self.Layout.addWidget(self.StackWidget)

        self.Layout.setContentsMargins(0, 0, 0, 0)
        self.setMinimumSize(self.ui.minimumSize())
        self.setLayout(self.Layout)


    def mouseMoveEvent(self, e) -> None:
        self.StackWidget.mouseMoveEvent(e)
        super(EmptyStackWidget, self).mouseMoveEvent(e)


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
    deck = EmptyDeck()
    #deck.makeRandomSequence()
    window = EmptyStackWidget(deck)
    window.show()
    sys.exit(app.exec())