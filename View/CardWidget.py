from UseCases.General.DefaultCard import DefaultCard
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic, QtGui
from Infrastructure.DataAccess.FilePath import cardUi, imgTypesCard, backCardUi
import sys


class CardWidget(QWidget):
    def __init__(self, card=None, parent=None):
        super().__init__(parent)

        self.ui = uic.loadUi(cardUi)
        self.grade_lbl = self.ui.Grade
        self.image_lbl = self.ui.Img

        self.setCard(card)

        self.bg = Background(self.ui.layout().parent())
        self.ui.layout().addWidget(self.bg)

        self.setLayout(self.ui.layout())

        self.setMinimumSize(self.ui.minimumSize())
        self.setMaximumSize(self.ui.maximumSize())

    def setCard(self, card):
        self.card = card
        if self.card is not None:
            self.grade_lbl.setText(self.card.rank)
            self.image_lbl.setPixmap(QtGui.QPixmap.fromImage(QtGui.QImage(imgTypesCard[self.card.mark.value])))

    def showBackSide(self):
        self.ui.frame.hide()
        self.bg.show()

    def showFrontSide(self):
        self.ui.frame.show()
        self.bg.hide()

    def show(self) -> None:
        if self.card is None:
            self.showFrontSide()
        elif self.card.isStatsVisible:
            self.showFrontSide()
        else:
            self.showBackSide()
        super().show()

    def flip(self):
        self.card.flip()


class Background(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = uic.loadUi(backCardUi)
        self.setLayout(self.ui.layout())
        self.setMinimumSize(self.ui.minimumSize())
        self.setMaximumSize(self.ui.maximumSize())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    testCard = DefaultCard()
    window = CardWidget()

    #window = Background()
    window.show()
    sys.exit(app.exec())



