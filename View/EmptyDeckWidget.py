from Infrastructure.DataAccess.FilePath import blankPileUi
from Entities.Deck import Deck
from View.CardWidget import CardWidget
from PyQt5.QtWidgets import QApplication, QPushButton, QVBoxLayout
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5 import uic
import sys

class Signals(QObject):
    dropCard = pyqtSignal(Deck, str, int)


class EmptyDeckWidget(QPushButton):
    def __init__(self, deck, mouseTracking=True, AcceptDrops=True, parent=None):
        super(EmptyDeckWidget, self).__init__(parent)
        self.Layout = QVBoxLayout(self)
        self.ui = uic.loadUi(blankPileUi)
        self.LastCard = CardWidget(deck[-1], mouseTracking)
        self.LastCard.clicked.connect(self.clicked)
        self.deck = deck

        self.signals = Signals()

        self.Layout.addWidget(self.ui)
        self.Layout.addWidget(self.LastCard)

        self.Layout.setContentsMargins(0, 0, 0, 0)
        self.setMinimumSize(self.ui.minimumSize())
        self.setMaximumSize(self.ui.maximumSize())
        self.setLayout(self.Layout)
        self.setAcceptDrops(AcceptDrops)

    def dragEnterEvent(self, a0) -> None:
        a0.accept()

    def dropEvent(self, a0) -> None:
        self.signals.dropCard.emit(self.deck, a0.mimeData().text().split("/")[0], int(a0.mimeData().text().split("/")[1]))
        a0.accept()

    def mouseMoveEvent(self, e) -> None:
        self.LastCard.mouseMoveEvent(e)
        super(EmptyDeckWidget, self).mouseMoveEvent(e)

    def refresh(self, deck):
        self.deck = deck
        self.LastCard.setCard(self.deck[-1])

    def show(self) -> None:
        if self.deck.isEmpty():
            self.ui.show()
            self.LastCard.hide()
        else:
            self.refresh(self.deck)
            self.ui.hide()
            self.LastCard.show()
        super(EmptyDeckWidget, self).show()

