from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSignal, QObject
from View.CardWidget import CardWidget
from UseCases.General.DefaultCard import DefaultCard


class Signals(QObject):
    popCard = pyqtSignal()

class StackWidget(QWidget):
    def __init__(self, deck, parent=None):
        super(StackWidget, self).__init__(parent)
        self.deck = deck
        self.cardWidgets = []

        self.refresh(self.deck)

        self.Signals = Signals()

        card = CardWidget(DefaultCard())
        self.setMinimumSize(card.minimumSize())

        card.deleteLater()

    def refresh(self, deck):
        self.deck = deck
        self.hideCards()
        self.deleteCards()
        self.cardWidgets.clear()
        for i in range(len(self.deck)):
            self.addCardWidget(self.deck[i])

        self.showCards()
        if not self.deck.isEmpty():
            self.offsetResize()
            self.alignmentCenter()
            self.resizeCards()
            self.offsetResize()



    def addCardWidget(self, card):
        self.cardWidgets.append(CardWidget(card, parent=self))
        return self.cardWidgets[-1]

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
            geometry.setHeight(int(geometry.height()))
            child.setGeometry(geometry)

    def alignmentCenter(self):
        for child in self.cardWidgets:
            geometry = child.geometry()
            geometry.setX(int((geometry.width())/128))
            child.setGeometry(geometry)

    def offsetResize(self):
        y = 0
        for child in self.cardWidgets:
            geometry = child.geometry()
            geometry.setY(y)
            child.setGeometry(geometry)
            y += int((geometry.height() / len(self.deck)+30))

    def resizeEvent(self, a0) -> None:
        if not self.deck.isEmpty():
            self.offsetResize()
            self.alignmentCenter()
            self.resizeCards()
            self.offsetResize()
        super(StackWidget, self).resizeEvent(a0)
