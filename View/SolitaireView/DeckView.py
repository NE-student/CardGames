from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic
from Infrastructure.FilePath import stockPileUi
from UseCases.SolitaireLogic.stockPile import StockPile
from View.CardWidget import CardWidget
from UseCases.General.StartDeck import StartDeck
import sys


class DeckView(QWidget):
    def __init__(self, pile, parent=None):
        super(DeckView, self).__init__(parent)

        LastCard = pile.getCards()[-1]
        self.card = CardWidget(LastCard)
        self.card.flip()
        self.setLayout(self.card.layout())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    deck = StartDeck()
    deck.makeRandomSequence()
    window = DeckView(deck)
    window.show()
    sys.exit(app.exec())