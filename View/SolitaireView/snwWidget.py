from PyQt5.QtWidgets import QWidget, QHBoxLayout
from View.EmptyDeckWidget import EmptyDeckWidget


class StockAndWasteWidget(QWidget):
    def __init__(self, stock, waste, parent=None):
        super(StockAndWasteWidget, self).__init__(parent)

        self.StockPileWidget = EmptyDeckWidget(stock, False, False)
        self.WastePileWidget = EmptyDeckWidget(waste, True, False)

        self.Layout = QHBoxLayout()
        self.Layout.addWidget(self.WastePileWidget)
        self.Layout.addWidget(self.StockPileWidget)

        self.setLayout(self.Layout)

        g = self.StockPileWidget.minimumSize()
        g.setWidth(g.width()+150)
        self.setMinimumSize(g)

        self.Layout.setContentsMargins(15, 0, 0, 0)
        self.Layout.setSpacing(3)

    def show(self) -> None:
        self.StockPileWidget.show()
        self.WastePileWidget.show()
        super(StockAndWasteWidget, self).show()

    def refresh(self, stockPile, wastePile):
        self.StockPileWidget.refresh(stockPile)
        self.WastePileWidget.refresh(wastePile)
