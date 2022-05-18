from UseCases.General.StartedDeck import StartedDeck
from UseCases.General.EmptyDeck import EmptyDeck
from UseCases.SolitaireLogic.stockNwastePiles import StockAndWasteRelationship
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout
from PyQt5.QtCore import QSize
from View.SolitaireView.StockPileWidget import StockPileWidget
from View.SolitaireView.WastePileWidget import WastePileWidget
import sys


class StockAndWasteWidget(QWidget):
    def __init__(self, stock, waste, parent=None):
        super(StockAndWasteWidget, self).__init__(parent)

        self.StockPileWidget = StockPileWidget(stock)
        self.WastePileWidget = WastePileWidget(waste)

        self.StockPileWidget.clicked.connect(self.StockPileWidgetclicked)

        self.snw = StockAndWasteRelationship(self.StockPileWidget.StockPile, self.WastePileWidget.WastePile)

        self.Layout = QHBoxLayout()
        self.Layout.addWidget(self.WastePileWidget)
        self.Layout.addWidget(self.StockPileWidget)

        self.setLayout(self.Layout)

        self.setMinimumSize(QSize(200,160))

    def StockPileWidgetclicked(self):
        if self.StockPileWidget.StockPile.isEmpty():
            self.snw.restart()
        else:
            self.snw.flipCardFromStockPile()
        self.show()

    def show(self) -> None:
        self.StockPileWidget.show()
        self.WastePileWidget.show()
        super(StockAndWasteWidget, self).show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    deck = StartedDeck()
    deck.makeRandomSequence()
    window = StockAndWasteWidget(deck, EmptyDeck())
    window.show()
    sys.exit(app.exec())