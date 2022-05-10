from PyQt5.QtWidgets import QApplication, QWidget
from View.CardWidget import CardWidget
from UseCases.General.StartDeck import StartDeck
import sys


class DeckView(QWidget):
    def __init__(self, deck, parent=None):
        super(DeckView, self).__init__(parent)

        LastCard = deck.getCards()[-1]
        self.card = CardWidget(LastCard)
        self.card.flip()
        self.setLayout(self.card.layout())

        self.setMinimumSize(self.card.minimumSize())
        self.setMaximumSize(self.card.maximumSize())

class DeckViewAllCards(QWidget):
    def __init__(self, deck, parent=None):
        super(DeckViewAllCards, self).__init__(parent)

        self.deck = deck
        self.cards = deck.getCards()
        self.ui()

        self.setMaximumSize(100, 16777215)
        self.setMaximumSize(100, 16777215)

    def ui(self):
        y = 0
        #x=0
        for i in range(len(self.cards) - 1, -1, -1):
            card = CardWidget(self.cards[i], self)
            geometry = card.geometry()
            geometry.setY(y)
            #geometry.setX(x)
            card.setGeometry(geometry)
            card.show()
            y += 5
            #x += random.randint(0,15)

    def clear(self):
        for child in self.children():
            child.deleteLater()

    def setDeck(self, deck):
        self.clear()
        self.deck = deck
        self.cards = deck.getCards()
        self.ui()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    deck = StartDeck()
    deck.makeRandomSequence()
    deck.toggleDeck()
    window = DeckViewAllCards(deck)
    deck.makeRandomSequence()
    deck.toggleDeck()
    window.setDeck(deck)
    window.show()
    sys.exit(app.exec())