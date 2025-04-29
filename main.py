import sys
from random import random, Random, randint

from PyQt6.QtWidgets import QDialog, QApplication, QInputDialog, QFileDialog

from layout import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.wczytajButton.clicked.connect(self.wczytaj)
        self.ui.generujButton.clicked.connect(self.generuj)

        self.show()

    def generuj(self):
        n,ok = QInputDialog.getText(self, "", "Wprowadź liczbę n")
        if ok:
            liczba = [randint(0,100) for i in range(int(n))]

        self.ui.liczbaEdit.setText(str(n))
        self.ui.liczbyEdit.setText(str(liczba))

    def wczytaj(self):
        sciezka, _ = QFileDialog.getOpenFileName(self, 'Wczytaj plik', '.', 'Text files (*.csv)')
        with open(sciezka, 'r') as plik:
            self.ui.liczbyEdit.setPlainText(plik.read())



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyForm()
    sys.exit(app.exec())