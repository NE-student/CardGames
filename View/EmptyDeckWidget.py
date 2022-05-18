from Infrastructure.DataAccess.FilePath import blankPileUi
from UseCases.General.StartedDeck import StartedDeck, EmptyDeck
from View.CardWidget import CardWidget
from PyQt5.QtWidgets import QApplication, QPushButton, QVBoxLayout
from PyQt5 import uic
import sys


class EmptyDeckWidget(QPushButton):
    def __init__(self, deck, mouseTracking=True,parent=None):
        super(EmptyDeckWidget, self).__init__(parent)
        self.Layout = QVBoxLayout(self)
        self.ui = uic.loadUi(blankPileUi)
        self.LastCard = CardWidget(deck[-1], mouseTracking)
        self.LastCard.clicked.connect(self.clicked)
        self.deck = deck

        self.Layout.addWidget(self.ui)
        self.Layout.addWidget(self.LastCard)

        self.Layout.setContentsMargins(0, 0, 0, 0)
        self.setMinimumSize(self.ui.minimumSize())
        self.setMaximumSize(self.ui.maximumSize())
        self.setLayout(self.Layout)


    def mouseMoveEvent(self, e) -> None:
        self.LastCard.mouseMoveEvent(e)
        super(EmptyDeckWidget, self).mouseMoveEvent(e)

    def refresh(self):
        self.LastCard.setCard(self.deck[-1])

    def show(self) -> None:
        if self.deck.isEmpty():
            self.ui.show()
            self.LastCard.hide()
        else:
            self.refresh()
            self.ui.hide()
            self.LastCard.show()
        super(EmptyDeckWidget, self).show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    deck = EmptyDeck()
    #deck.makeRandomSequence()
    window = EmptyDeckWidget(deck)
    window.show()
    sys.exit(app.exec())