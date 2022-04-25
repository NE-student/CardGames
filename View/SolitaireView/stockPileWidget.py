from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic
from Infrastructure.FilePath import stockPileUi
from UseCases.SolitaireLogic.stockPile import StockPile

class StockPileWidget(QWidget):
    def __init__(self, parent=None):
        super(StockPileWidget, self).__init__(parent)

        self.deck = None
        self.ui = uic.loadUi(stockPileUi)

    def setCards(self, cards):
        self.deck = StockPile(cards)

