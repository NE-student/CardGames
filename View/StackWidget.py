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
        if len(self.cardWidgets) < len(self.deck):
            self.hideChildren()
            self.deleteChildren()
            self.cardWidgets.clear()
            for i in range(len(self.deck)):
                card = self.addCardWidget(self.deck[i])
                card.signals.popCard.connect(self.popCard)
                card.show()
        if len(self.cardWidgets) > len(self.deck):
            self.hideChildren()
            for index, item in enumerate(self.cardWidgets):
                if index >= len(self.cardWidgets)-1:
                    self.cardWidgets.pop(index)
                    item.hide()
                    item.deleteLater()
        self.showChildren()
        if not self.deck.isEmpty():
            self.alignmentCenter()
            self.resizeChild()
            self.offsetResize()


    def addCardWidget(self, card):
        self.cardWidgets.append(CardWidget(card, parent=self))
        return self.cardWidgets[-1]

    def popCard(self):
        self.deck.pop(-1)
        self.Signals.popCard.emit()

    def hideChildren(self):
        for child in self.cardWidgets:
            child.hide()

    def deleteChildren(self):
        for child in self.cardWidgets:
            child.deleteLater()

    def showChildren(self):
        for child in self.cardWidgets:
            child.show()

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

    def resizeChild(self):
        for child in self.cardWidgets:
            geometry = child.geometry()
            geometry.setWidth(int(self.width()))
            geometry.setHeight(int(self.height() / (self.height()/len(self.deck))))
            geometry.setHeight(self.height())
            child.setGeometry(geometry)

    def resizeEvent(self, a0) -> None:
        if not self.deck.isEmpty():
            self.alignmentCenter()
            self.resizeChild()
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