from View.CardWidget import CardWidget
from UseCases.General.DefaultCard import DefaultCard
from View.OpenGLEffects import BackGround
from UseCases.General.StartedDeck import StartedDeck
from PyQt5.QtWidgets import QApplication, QWidget, QScrollArea, QGridLayout
from PyQt5.QtCore import QSize
import sys


class StackWidget(QWidget):
    def __init__(self, deck, custom_card_view=None, parent=None):
        super(StackWidget, self).__init__(parent)
        self.deck = deck
        self.createStack()

        card = CardWidget(DefaultCard())
        self.setMinimumSize(card.minimumSize())
        card.deleteLater()

    def createStack(self):
        for i in range(len(self.deck) - 1, -1, -1):
            card = CardWidget(self.deck[i], self)
            card.show()


    def hideChildren(self):
        for child in self.children():
            child.hide()

    def showChildren(self):
        for child in self.children():
            child.show()

    def alignmentCenter(self):
        for child in self.children():
            geometry = child.geometry()
            geometry.setX(int((self.width()-geometry.width())/2))
            child.setGeometry(geometry)


    def offsetResize(self):
        y = 0
        for child in self.children():
            geometry = child.geometry()
            geometry.setY(y)
            child.setGeometry(geometry)
            y += int((self.height() + 40 - geometry.height()) / (len(self.deck)))

    def resizeChild(self):
        for child in self.children():
            geometry = child.geometry()
            geometry.setWidth(int(self.width()))
            geometry.setHeight(int(self.height() / (self.height() / len(self.deck))))
            geometry.setHeight(self.height())
            child.setGeometry(geometry)

    def resizeEvent(self, a0) -> None:
        self.alignmentCenter()
        self.resizeChild()
        self.offsetResize()
        super(StackWidget, self).resizeEvent(a0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    deck = StartedDeck()
    deck.makeRandomSequence()
    window = StackWidget(deck)
    window.show()
    sys.exit(app.exec())