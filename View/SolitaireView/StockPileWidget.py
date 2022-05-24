from PyQt5.QtWidgets import QApplication, QPushButton, QHBoxLayout
from PyQt5.QtCore import Qt
from UseCases.General.DefaultDeck import DefaultDeck
from View.EmptyDeckWidget import EmptyDeckWidget
from UseCases.SolitaireLogic.stockPile import StockPile
import sys


class StockPileWidget(QPushButton):
    def __init__(self, deck, parent=None):
        super(StockPileWidget, self).__init__(parent)
        self.StockPile = deck
        self.Layout = QHBoxLayout(self)

        self.EmptyDeckWidget = EmptyDeckWidget(self.StockPile, False, False, self)
        self.EmptyDeckWidget.clicked.connect(self.clicked)
        self.Layout.addWidget(self.EmptyDeckWidget)

        self.Layout.setContentsMargins(0, 0, 0, 0)
        self.setMinimumSize(self.EmptyDeckWidget.minimumSize())
        self.setMaximumSize(self.EmptyDeckWidget.maximumSize())

        self.setLayout(self.Layout)

    def show(self) -> None:
        self.EmptyDeckWidget.show()
        super(StockPileWidget, self).show()

    def refresh(self):
        self.EmptyDeckWidget.refresh()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    deck = DefaultDeck()
    deck.makeDefaultSequence()
    window = StockPileWidget(deck)
    window.show()
    sys.exit(app.exec())