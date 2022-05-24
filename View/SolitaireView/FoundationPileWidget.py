from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout
from PyQt5.QtCore import QObject, pyqtSignal
from Entities.Deck import Deck
from View.EmptyDeckWidget import EmptyDeckWidget
from UseCases.General.DefaultCard import DefaultCard

class Signals(QObject):
    dropCard = pyqtSignal(Deck, str, int)

class FoundationPileWidget(QWidget):
    def __init__(self, FoundationPile, parent=None):
        super(FoundationPileWidget, self).__init__(parent)
        self.setLayout(QHBoxLayout(self))

        self.signals = Signals()

        self.FoundationPile = FoundationPile
        self.EmptyDeckWidget = EmptyDeckWidget(self.FoundationPile, True, parent=self)
        self.EmptyDeckWidget.signals.dropCard.connect(self.dropCard)
        self.layout().addWidget(self.EmptyDeckWidget)
        self.layout().setContentsMargins(0, 0, 0, 0)

    def dropCard(self, rank, mark):
        self.signals.dropCard.emit(self.FoundationPile, rank, mark)

    def refresh(self):
        self.EmptyDeckWidget.refresh()

    def show(self) -> None:
        self.refresh()
        self.EmptyDeckWidget.show()
        super(FoundationPileWidget, self).show()
