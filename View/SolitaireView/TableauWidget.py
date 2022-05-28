from PyQt5.QtWidgets import QWidget, QHBoxLayout
from View.EmptyStackWidget import EmptyStackWidget


class TableauWidget(QWidget):
    def __init__(self, Tableau, parent=None):
        super(TableauWidget, self).__init__(parent)
        self.columns = [EmptyStackWidget(Tableau[i], self) for i in range(len(Tableau))]

        self.setLayout(QHBoxLayout(self))
        for column in self.columns:
            self.layout().addWidget(column)

        self.layout().setSpacing(3)
        self.layout().setContentsMargins(0, 0, 0, 0)

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
