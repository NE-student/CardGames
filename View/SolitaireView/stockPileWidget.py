from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic
from Infrastructure.DataAccess.FilePath import stockPileUi
from UseCases.SolitaireLogic.stockPile import StockPile
from View.SolitaireView.DeckView import DeckViewAllCards
from UseCases.General.BlankDeck import BlankDeck
from UseCases.General.StartDeck import StartDeck
import sys


class StockPileWidget(QWidget):
    def __init__(self, parent=None):
        super(StockPileWidget, self).__init__(parent)

        deck = StockPile(BlankDeck().getCards())
        self.deckView = DeckViewAllCards(deck)
        self.deckView.hide()
        self.ui = uic.loadUi(stockPileUi)
        self.ui.layout().addWidget(self.deckView)
        #self.ui.layout().setAlignment(Qt.AlignCenter)

        self.setLayout(self.ui.layout())
        self.setMinimumSize(self.ui.Reload.minimumSize())
        self.setMaximumSize(self.ui.Reload.maximumSize())

    def setCards(self, cards):
        self.deckView.setDeck(StockPile(cards))
        self.deckView.show()
        self.ui.Reload.hide()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    deck = StartDeck()
    deck.makeRandomSequence()
    deck.toggleDeck()
    window = StockPileWidget()
    window.setCards(deck.getCards())
    #deck.makeRandomSequence()
    #deck.toggleDeck()
    #window.setDeck(deck)
    window.show()
    sys.exit(app.exec())


