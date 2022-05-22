from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout
from PyQt5.QtCore import QSize
from PyQt5 import uic
from View.SolitaireView.snwWidget import StockAndWasteWidget
from View.SolitaireView.TableauWidget import TableauWidget
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



        self.ui = uic.loadUi(solitaireUi)
        self.ui.Top.addWidget(self.snw)
        self.ui.Bottom.addWidget(self.TableauWidget)


        self.setLayout(self.ui.layout())

        self.setMinimumSize(self.ui.minimumSize())


    def show(self) -> None:
        self.TableauWidget.show()
        self.snw.show()
        super(SolitaireWidget, self).show()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SolitaireWidget()
    window.show()
    sys.exit(app.exec())