from UseCases.General.StartedDeck import StartedDeck
from PyQt5.QtWidgets import QApplication, QPushButton, QHBoxLayout
from UseCases.General.EmptyDeck import EmptyDeck
from View.EmptyDeckWidget import EmptyDeckWidget
from UseCases.SolitaireLogic.wastePile import WastePile
import sys


class WastePileWidget(QPushButton):
    def __init__(self, deck, parent=None):
        super(WastePileWidget, self).__init__(parent)
        self.WastePile = WastePile()
        self.Layout = QHBoxLayout(self)

        self.WastePile.appendCards(deck.getCards())
        self.EmptyDeckWidget = EmptyDeckWidget(self.WastePile)
        self.Layout.addWidget(self.EmptyDeckWidget)

        self.Layout.setContentsMargins(0, 0, 0, 0)
        self.setMinimumSize(self.EmptyDeckWidget.minimumSize())
        self.setMaximumSize(self.EmptyDeckWidget.maximumSize())

        self.setLayout(self.Layout)

    def show(self) -> None:
        self.EmptyDeckWidget.show()
        super(WastePileWidget, self).show()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    deck = StartedDeck()
    window = WastePileWidget(deck)
    window.show()
    sys.exit(app.exec())