#!/usr/bin/env python

from die import * 
import sys
import crapsResources_rc
from PyQt5 import QtGui, uic
from PyQt5.QtWidgets import QMainWindow, QApplication


class Craps(QMainWindow):
    """A game of Craps."""
    die1 = die2 = None

    def __init__(self, parent=None):
        """Build a game with two dice."""

        super().__init__(parent)
        uic.loadUi("Craps.ui", self)

        self.die1 = Die()
        self.die2 = Die()
        self.firstRoll = True
        self.numberOfWins = 0

        self.rollButton.clicked.connect(self.rollButtonClickedHandler)

    def __str__(self):
        """String representation for Craps.
        """

        return "Die1: %s\nDie2: %s" % (self.die1, self.die2)

    def updateUI(self):
        self.die1View.setPixmap(QtGui.QPixmap(":/" + str(self.die1.getValue())))
        self.die2View.setPixmap(QtGui.QPixmap(":/" + str(self.die2.getValue())))
        self.winsCountValueUI.setText(str(self.numberOfWins))

    # Player asked for another roll of the dice.
    def rollButtonClickedHandler(self):
        print("Roll button clicked")
        self.updateUI()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    crapsApp = Craps()
    crapsApp.updateUI()
    crapsApp.show()
    sys.exit(app.exec_())
