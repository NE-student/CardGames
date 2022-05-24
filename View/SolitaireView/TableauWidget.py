from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout
from UseCases.SolitaireLogic.Tableau import Tableau
from View.SolitaireView.columnOfTableauWidget import ColumnOfTableauWidget


class TableauWidget(QWidget):
    def __init__(self, Tableau, parent=None):
        super(TableauWidget, self).__init__(parent)
        self.Tableau = Tableau
        self.columns = [ColumnOfTableauWidget(self.Tableau.columns[i], self) for i in range(len(self.Tableau.columns))]

        self.setLayout(QHBoxLayout(self))
        for column in self.columns:
            self.layout().addWidget(column)

    def refresh(self):
        for column in self.columns:
            column.refresh()

    def dropCardconnect(self, slot):
        for column in self.columns:
            column.signals.dropCard.connect(slot)

    def show(self) -> None:
        for column in self.columns:
            column.show()
        super(TableauWidget, self).show()
