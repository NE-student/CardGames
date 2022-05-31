from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5 import uic
from View.SolitaireView.snwWidget import StockAndWasteWidget
from View.SolitaireView.TableauWidget import TableauWidget
from View.EmptyDeckWidget import EmptyDeckWidget
from UseCases.SolitaireLogic.SolitaireGamePlay import SolitaireGamePlay, SolitaireZone
from Infrastructure.DataAccess.FilePath import solitaireUi


class Signals(QObject):
    gameEnd = pyqtSignal()
    stepped = pyqtSignal()


class SolitaireWidget(QWidget):
    def __init__(self, parent=None):
        super(SolitaireWidget, self).__init__(parent)

        self.ui = uic.loadUi(solitaireUi)
        self.GameZone = SolitaireZone()
        self.GamePlay = SolitaireGamePlay(self.GameZone)

        self.signals = Signals()

        self.snw = StockAndWasteWidget(self.GameZone.StockPile, self.GameZone.WastePile)
        self.snw.StockPileWidget.clicked.connect(self.StockPileWidgetclicked)

        self.TableauWidget = TableauWidget(self.GameZone.ColumnsOfTableau, self)
        self.TableauWidget.dropCardconnect(self.dropCardToColumnOfTableau)

        self.FoundationPileWidgets = [EmptyDeckWidget(pile, True) for pile in self.GameZone.FoundationPiles]

        for pile in self.FoundationPileWidgets:
            self.ui.Top.addWidget(pile)
            pile.signals.dropCard.connect(self.dropCardToFoundationPile)

        self.ui.Top.addWidget(self.snw)
        self.ui.Bottom.addWidget(self.TableauWidget)

        self.setLayout(self.ui.layout())

        self.setMinimumSize(self.ui.minimumSize())
        self.setMaximumSize(self.ui.maximumSize())

    def StockPileWidgetclicked(self):
        if self.GameZone.StockPile.isEmpty():
            self.GamePlay.SendToStockPileFromWastePile()
        else:
            self.GamePlay.SendToWastePileFromStockPile()
        self.refresh()

    def dropCardToFoundationPile(self, receiver, rank, mark):
        card, sender = self.GamePlay.findCard(rank, mark)
        if sender in self.GameZone.FoundationPiles:
            self.GamePlay.SendToFoundationPileFromFoundationPile(receiver.index, sender.index, card)
        elif sender in self.GameZone.ColumnsOfTableau:
            self.GamePlay.SendToFoundationPileFromColumnOfTableau(receiver.index, sender.index, card)
        elif sender is self.GameZone.WastePile:
            self.GamePlay.SendToFoundationPileFromWastePile(receiver.index)
        self.refresh()
        if self.GamePlay.isWin():
            self.signals.gameEnd.emit()

    def dropCardToColumnOfTableau(self, receiver, rank, mark):
        card, sender = self.GamePlay.findCard(rank, mark)
        if sender in self.GameZone.FoundationPiles:
            self.GamePlay.SendToColumnOfTableauFromFoundationPile(receiver.index, sender.index, card)
        elif sender in self.GameZone.ColumnsOfTableau:
            self.GamePlay.SendToColumnOfTableauFromColumnOfTableau(receiver.index, sender.index, card)
        elif sender is self.GameZone.WastePile:
            self.GamePlay.SendToColumnOfTableauFromWastePile(receiver.index)

        self.refresh()

    def refresh(self):
        self.signals.stepped.emit()
        for index, pile in enumerate(self.FoundationPileWidgets):
            pile.refresh(self.GameZone.FoundationPiles[index])
        self.snw.refresh(self.GameZone.StockPile, self.GameZone.WastePile)
        self.TableauWidget.refresh(self.GameZone.ColumnsOfTableau)
        self.show()


    def show(self) -> None:
        for pile in self.FoundationPileWidgets:
            pile.show()
        self.TableauWidget.show()
        self.snw.show()
        super(SolitaireWidget, self).show()
