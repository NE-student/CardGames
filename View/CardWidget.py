from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt, QMimeData
from PyQt5.QtGui import QDrag
from PyQt5 import uic, QtGui
from Infrastructure.DataAccess.FilePath import cardUi, imgTypesCard, backCardUi


class CardWidget(QPushButton):
    def __init__(self, card=None, mouseTracking=True, parent=None):
        super().__init__(parent)

        self.ui = uic.loadUi(cardUi)
        self.grade_lbl = self.ui.Grade
        self.image_lbl = self.ui.Img
        self.mouseTracking = mouseTracking

        self.setCard(card)

        self.bg = Background(self.ui.layout().parent())
        self.Layout = QVBoxLayout(self)
        self.Layout.addWidget(self.ui)
        self.Layout.addWidget(self.bg)
        self.setLayout(self.Layout)

        self.Layout.setContentsMargins(0, 0, 0, 0)
        self.setMinimumSize(self.ui.minimumSize())
        self.setMaximumSize(self.ui.maximumSize())

    def mouseMoveEvent(self, e) -> None:
        if self.hasMouseTracking() and e.buttons() == Qt.LeftButton:
            mimedata = QMimeData()
            mimedata.setText(str(self.card.rank) +"/"+ str(self.card.mark.value))
            drag = QDrag(self)
            drag.setMimeData(mimedata)
            drag.setHotSpot(e.pos())
            drag.exec_(Qt.MoveAction)

    def setCard(self, card):
        self.card = card
        if self.card is not None:
            self.grade_lbl.setText(self.card.rank)
            if self.card.isRed():
                self.grade_lbl.setStyleSheet("color:#942706;")
            else:
                self.grade_lbl.setStyleSheet("color:black;")
            self.image_lbl.setPixmap(QtGui.QPixmap.fromImage(QtGui.QImage(imgTypesCard[self.card.mark.value])))

    def showBackSide(self):
        self.ui.hide()
        self.bg.show()

    def showFrontSide(self):
        self.ui.show()
        self.bg.hide()

    def show(self) -> None:
        if self.card is None:
            self.showFrontSide()
        elif self.card.isStatsVisible:
            self.showFrontSide()
        else:
            self.showBackSide()
        self.setMouseTracking(self.mouseTracking and self.card.isStatsVisible)
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
