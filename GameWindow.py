from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QToolBar, QStatusBar, QAction, QLCDNumber, QLabel
from PyQt5.QtCore import QTimer
from View.SolitaireView.Solitaire import SolitaireWidget
import math
import sys


class GameWindow(QMainWindow):
    def __init__(self, parent=None):
        super(GameWindow, self).__init__(parent)

        self.SolitaireWidget = SolitaireWidget(self)
        self.GameFunctions = QToolBar(self)
        self.StatusBar = QStatusBar(self)
        self.TimerWidget = QLCDNumber(5)

        self.Step = QLabel("Step: 0", self)

        self.Timer = QTimer(self)
        self.Timer.timeout.connect(self.setTime)
        self.time = 0

        undoAction = QAction("&Undo", self)
        redoAction = QAction("&Redo", self)
        undoAction.triggered.connect(self.SolitaireWidget.GamePlay.undoStep)
        undoAction.triggered.connect(self.SolitaireWidget.refresh)
        redoAction.triggered.connect(self.SolitaireWidget.GamePlay.redoStep)
        redoAction.triggered.connect(self.SolitaireWidget.refresh)

        self.SolitaireWidget.signals.gameEnd.connect(self.WinWindow)
        self.SolitaireWidget.signals.stepped.connect(self.setStep)

        self.GameFunctions.addAction(undoAction)
        self.GameFunctions.addAction(redoAction)

        self.StatusBar.addWidget(self.TimerWidget)
        self.StatusBar.addWidget(self.Step)

        self.addToolBar(self.GameFunctions)
        self.setStatusBar(self.StatusBar)

        self.setCentralWidget(self.SolitaireWidget)

        self.Timer.start(1000)

        self.setWindowTitle("Solitaire")
        self.setMaximumSize(self.SolitaireWidget.maximumSize())

    def setStep(self):
        self.Step.setText(f"Step: {self.SolitaireWidget.GamePlay.stepIndex}")

    def setTime(self):
        self.time += 1
        self.TimerWidget.display(self.secondsToDefaultTime(self.time))

    def secondsToDefaultTime(self, seconds):
        minutes = math.floor(seconds/60)
        return f"{minutes}:{seconds-minutes*60}"

    def WinWindow(self):
        self.Timer.stop()
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setText(f"Congratulation!\n You completed all foundation piles!")
        msg_box.setWindowTitle("WON")
        msg_box.setStandardButtons(QMessageBox.Ok)
        sys.exit(msg_box.exec_())
    
    def show(self) -> None:
        self.centralWidget().show()
        super(GameWindow, self).show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GameWindow()
    window.show()
    sys.exit(app.exec_())