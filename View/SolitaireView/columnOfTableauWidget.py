from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout
from UseCases.SolitaireLogic.columnOfTableau import ColumnOfTableau
from View.EmptyStackWidget import EmptyStackWidget
import sys


class ColumnOfTableauWidget(QWidget):
    def __init__(self, ColumnOfTableau, parent=None):
        super(ColumnOfTableauWidget, self).__init__(parent)

        self.ColumnOfTableau = ColumnOfTableau

        self.EmptyStackWidget = EmptyStackWidget(self.ColumnOfTableau, self)
        self.setLayout(QHBoxLayout(self))
        self.layout().addWidget(self.EmptyStackWidget)
        self.layout().setContentsMargins(0, 0, 0, 0)

    def show(self) -> None:
        self.EmptyStackWidget.show()
        super(ColumnOfTableauWidget, self).show()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = ColumnOfTableauWidget()
    window.show()
    sys.exit(app.exec())