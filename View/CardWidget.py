from UseCases.General.DefaultCard import DefaultCard
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic, QtGui
from Infrastructure.DataAccess.FilePath import cardUi, imgTypesCard, backCardUi
import sys


class CardWidget(QWidget):
    def __init__(self, card, parent=None):
        super().__init__(parent)

        self.card = card

        self.ui = uic.loadUi(cardUi)
        self.grade_lbl = self.ui.Grade
        self.image_lbl = self.ui.Img
        self.bg = Background(self.ui.layout().parent())
        self.ui.layout().addWidget(self.bg)

        self.setSide()

        self.setLayout(self.ui.layout())
        self.grade_lbl.setText(self.card.rank)
        self.image_lbl.setPixmap(QtGui.QPixmap.fromImage(QtGui.QImage(imgTypesCard[self.card.mark.value])))

        self.setMinimumSize(self.ui.minimumSize())
        self.setMaximumSize(self.ui.maximumSize())

    def setSide(self):
        if not self.card.isStatsVisible:
            self.ui.frame.hide()
            self.bg.show()
        else:
            self.ui.frame.show()
            self.bg.hide()
    def flip(self):
        self.card.flip()
        self.setSide()

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
    window = CardWidget(testCard)
    window.flip()

    #window = Background()
    window.show()
    sys.exit(app.exec())



