from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout
from View.EmptyStackWidget import EmptyStackWidget


class TableauWidget(QWidget):
    def __init__(self, Columns, parent=None):
        super(TableauWidget, self).__init__(parent)
        Tableau = Columns
        self.columns = [EmptyStackWidget(Tableau[i], self) for i in range(len(Tableau))]

        self.setLayout(QHBoxLayout(self))
        for column in self.columns:
            self.layout().addWidget(column)

    def refresh(self, columns):
        for index, column in enumerate(self.columns):
            columns[index].showLastCard()
            column.refresh(columns[index])

    def dropCardconnect(self, slot):
        for column in self.columns:
            column.signals.dropCard.connect(slot)

    def show(self) -> None:
        for column in self.columns:
            column.show()
        super(TableauWidget, self).show()
