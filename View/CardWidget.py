from UseCases.General.DefaultCard import DefaultCard
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic, QtGui
from Infrastructure.FilePath import cardUi, imgTypesCard
import sys


class CardWidget(QWidget):
    def __init__(self, card, parent=None):
        super().__init__(parent)

        self.card = card

        self.ui = uic.loadUi(cardUi)
        self.grade_lbl = self.ui.Grade
        self.image_lbl = self.ui.Img

        self.setLayout(self.ui.layout())
        self.grade_lbl.setText(self.card.rank)
        self.image_lbl.setPixmap(QtGui.QPixmap.fromImage(QtGui.QImage(imgTypesCard[self.card.mark.value])))

        self.setStyleSheet("background:#fff;")
        self.setMinimumSize(self.ui.minimumSize())
        self.setMaximumSize(self.ui.maximumSize())

    def flip(self):
        if self.isFace:
            self.grade_lbl.hide()
            self.image_lbl.hide()
        else:
            self.grade_lbl.show()
            self.image_lbl.show()
        self.card.flip()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    testCard = DefaultCard()
    window = CardWidget(testCard)
    window.show()
    sys.exit(app.exec())



