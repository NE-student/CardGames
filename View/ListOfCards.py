from View.CardWidget import CardWidget
from View.OpenGLEffects import BackGround
from UseCases.General.StartDeck import StartDeck
from PyQt5.QtWidgets import QApplication, QWidget, QScrollArea, QGridLayout
from PyQt5.QtCore import QSize
import sys


class ListOfCards(QWidget):
    def __init__(self, deck, custom_card_view=None, parent=None):
        super().__init__(parent)
        self.setLayout(QGridLayout(self))
        self.area = QScrollArea(self)
        self.area.setGeometry(self.geometry())
        self.columns = 3

        self.viewCards(deck, custom_card_view)

        self.layout().addWidget(self.area)
        self.setMinimumSize(QSize(self.columns * 157, 170))


    def viewCards(self, deck, custom_card_view):
        mw = QWidget()
        layout = QGridLayout()
        mw.setLayout(layout)
        i = 0
        j = 0
        for card in deck.getCards():
            if j % self.columns == 0:
                i += 1
            if custom_card_view is None:
                w = CardWidget(card)
            else:
                w = custom_card_view(CardWidget(card))
            layout.addWidget(w, i, j % self.columns)
            j += 1

        self.area.setWidget(mw)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    deck = StartDeck()
    window = ListOfCards(deck, BackGround)
    window.show()
    sys.exit(app.exec())