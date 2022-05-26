from PyQt5.QtWidgets import QApplication, QWidget, QScrollArea, QGridLayout
from PyQt5.QtCore import pyqtSignal, QObject
from View.CardWidget import CardWidget
from UseCases.General.DefaultCard import DefaultCard
from UseCases.General.DefaultDeck import DefaultDeck
from View.OpenGLEffects import BackGround

import sys

class Signals(QObject):
    popCard = pyqtSignal()

class StackWidget(QWidget):
    def __init__(self, deck, parent=None):
        super(StackWidget, self).__init__(parent)
        self.deck = deck
        self.cardWidgets = []

        self.refresh()

        self.Signals = Signals()

        card = CardWidget(DefaultCard())
        self.setMinimumSize(card.minimumSize())
        card.deleteLater()

    def refresh(self):
        self.hideCards()
        if len(self.cardWidgets) < len(self.deck):
            self.deleteCards()
            self.cardWidgets.clear()
            for i in range(len(self.deck)):
                card = self.addCardWidget(self.deck[i])
                card.signals.popCard.connect(self.popCard)
        if len(self.cardWidgets) > len(self.deck):
            while len(self.cardWidgets) > len(self.deck):
                item = self.cardWidgets.pop(-1)
                item.hide()
                item.deleteLater()

        self.showCards()
        if not self.deck.isEmpty():
            self.alignmentCenter()
            self.resizeCards()
            self.offsetResize()


    def addCardWidget(self, card):
        self.cardWidgets.append(CardWidget(card, parent=self))
        return self.cardWidgets[-1]

    def popCard(self):
        self.deck.pop(-1)
        self.Signals.popCard.emit()

    def hideCards(self):
        for child in self.cardWidgets:
            child.hide()

    def deleteCards(self):
        for child in self.cardWidgets:
            child.deleteLater()

    def showCards(self):
        for child in self.cardWidgets:
            child.show()

    def resizeCards(self):
        for child in self.cardWidgets:
            geometry = child.geometry()
            geometry.setWidth(int(self.width()))
            geometry.setHeight(int(self.height() / (self.height()/len(self.deck))))
            geometry.setHeight(self.height())
            child.setGeometry(geometry)

    def alignmentCenter(self):
        for child in self.cardWidgets:
            geometry = child.geometry()
            geometry.setX(int((self.width()-geometry.width())/2))
            child.setGeometry(geometry)

    def offsetResize(self):
        y = 0
        for child in self.cardWidgets:
            geometry = child.geometry()
            geometry.setY(y)
            child.setGeometry(geometry)
            y += int((self.height() + 40 - geometry.height()) / (len(self.deck)))

    def resizeEvent(self, a0) -> None:
        if not self.deck.isEmpty():
            self.alignmentCenter()
            self.resizeCards()
            self.offsetResize()
        super(StackWidget, self).resizeEvent(a0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    deck = DefaultDeck()
    deck.makeDefaultSequence()
    deck.makeRandomSequence()
    window = StackWidget(deck)
    window.show()
    sys.exit(app.exec())