from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout
from PyQt5.QtCore import QSize
from View.EmptyDeckWidget import EmptyDeckWidget
import sys


class StockAndWasteWidget(QWidget):
    def __init__(self, stock, waste, parent=None):
        super(StockAndWasteWidget, self).__init__(parent)

        self.StockPileWidget = EmptyDeckWidget(stock, False, False)
        self.WastePileWidget = EmptyDeckWidget(waste, True, False)

        self.Layout = QHBoxLayout()
        self.Layout.addWidget(self.WastePileWidget)
        self.Layout.addWidget(self.StockPileWidget)

        self.setLayout(self.Layout)

        self.setMinimumSize(QSize(200,160))



    def show(self) -> None:
        self.StockPileWidget.show()
        self.WastePileWidget.show()
        super(StockAndWasteWidget, self).show()

    def refresh(self, stockPile, wastePile):
        self.StockPileWidget.refresh(stockPile)
        self.WastePileWidget.refresh(wastePile)
