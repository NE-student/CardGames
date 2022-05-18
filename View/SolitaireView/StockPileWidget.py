from UseCases.General.StartedDeck import StartedDeck
from PyQt5.QtWidgets import QApplication, QPushButton, QHBoxLayout
from PyQt5.QtCore import Qt
from UseCases.General.EmptyDeck import EmptyDeck
from View.EmptyDeckWidget import EmptyDeckWidget
from UseCases.SolitaireLogic.stockPile import StockPile
import sys


class StockPileWidget(QPushButton):
    def __init__(self, deck, parent=None):
        super(StockPileWidget, self).__init__(parent)
        self.StockPile = StockPile()
        self.Layout = QHBoxLayout(self)

        self.StockPile.appendCards(deck.getCards())
        self.EmptyDeckWidget = EmptyDeckWidget(self.StockPile, False)
        self.EmptyDeckWidget.clicked.connect(self.clicked)
        self.Layout.addWidget(self.EmptyDeckWidget)

        self.Layout.setContentsMargins(0, 0, 0, 0)
        self.setMinimumSize(self.EmptyDeckWidget.minimumSize())
        self.setMaximumSize(self.EmptyDeckWidget.maximumSize())


        self.setLayout(self.Layout)

    def show(self) -> None:
        self.EmptyDeckWidget.show()
        super(StockPileWidget, self).show()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    deck = EmptyDeck()
    window = StockPileWidget(deck)
    window.show()
    sys.exit(app.exec())