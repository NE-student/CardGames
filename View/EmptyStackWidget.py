from Infrastructure.DataAccess.FilePath import blankPileUi
from Entities.Deck import Deck
from View.StackWidget import StackWidget
from PyQt5.QtWidgets import QWidget, QHBoxLayout
from PyQt5.QtCore import QObject, pyqtSignal, Qt
from PyQt5 import uic


class Signals(QObject):
    dropCard = pyqtSignal(Deck, str, int)


class EmptyStackWidget(QWidget):
    def __init__(self, deck, parent=None):
        super(EmptyStackWidget, self).__init__(parent)
        self.Layout = QHBoxLayout(self)
        self.ui = uic.loadUi(blankPileUi)
        self.StackWidget = StackWidget(deck, self)

        self.signals = Signals()

        self.Layout.addWidget(self.ui)
        self.Layout.addWidget(self.StackWidget)
        self.Layout.setAlignment(self.ui, Qt.AlignTop)

        self.Layout.setContentsMargins(0, 0, 0, 0)
        self.setMinimumSize(self.ui.minimumSize())
        self.setLayout(self.Layout)

        self.setAcceptDrops(True)

    def dragEnterEvent(self, a0) -> None:
        a0.accept()

    def dropEvent(self, a0) -> None:
        self.signals.dropCard.emit(self.StackWidget.deck, a0.mimeData().text().split("/")[0], int(a0.mimeData().text().split("/")[1]))
        a0.accept()

    def refresh(self, deck):
        self.StackWidget.refresh(deck)

    def show(self) -> None:
        if self.StackWidget.deck.isEmpty():
            self.ui.show()
            self.StackWidget.hide()
        else:
            self.ui.hide()
            self.StackWidget.show()
        super(EmptyStackWidget, self).show()

