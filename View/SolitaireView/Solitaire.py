from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic
from View.SolitaireView.snwWidget import StockAndWasteWidget
from View.SolitaireView.TableauWidget import TableauWidget
from View.SolitaireView.FoundationPileWidget import FoundationPileWidget
from UseCases.SolitaireLogic.Solitaire import Solitaire
from Infrastructure.DataAccess.FilePath import solitaireUi


import sys


class SolitaireWidget(QWidget):
    def __init__(self, parent=None):
        super(SolitaireWidget, self).__init__(parent)

        self.Solitaire = Solitaire()
        self.Solitaire.start()

        self.snw = StockAndWasteWidget(self.Solitaire.stock, self.Solitaire.waste)
        self.TableauWidget = TableauWidget(self.Solitaire.tableau, self)
        self.FoundationPileWidgets = [FoundationPileWidget(pile) for pile in self.Solitaire.foundationPiles]

        self.ui = uic.loadUi(solitaireUi)

        for pile in self.FoundationPileWidgets:
            self.ui.Top.addWidget(pile)
            pile.signals.dropCard.connect(self.dropCard)
        self.TableauWidget.dropCardconnect(self.dropCard)


        self.ui.Top.addWidget(self.snw)
        self.ui.Bottom.addWidget(self.TableauWidget)

        self.setLayout(self.ui.layout())

        self.setMinimumSize(self.ui.minimumSize())

    def dropCard(self, receiver, rank, mark):
        card, sender = self.Solitaire.RelationShip.findCard(self.Solitaire, rank, mark)
        self.Solitaire.RelationShip.sendCard(card, receiver, sender)
        self.refresh()

    def refresh(self):
        for pile in self.FoundationPileWidgets:
            pile.refresh()
        self.snw.refresh()
        self.TableauWidget.refresh()
        self.show()


    def show(self) -> None:
        for pile in self.FoundationPileWidgets:
            pile.show()
        self.TableauWidget.show()
        self.snw.show()
        super(SolitaireWidget, self).show()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SolitaireWidget()
    window.show()
    sys.exit(app.exec())