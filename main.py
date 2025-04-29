import sys
from random import random, Random, randint

from PyQt6.QtWidgets import QDialog, QApplication, QInputDialog, QFileDialog

from layout import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.liczby = []
        self.ui.wczytajButton.clicked.connect(self.wczytaj)
        self.ui.generujButton.clicked.connect(self.generuj)

        self.show()

    def generuj(self):
        n,ok = QInputDialog.getText(self, "", "Wprowadź liczbę n")
        if ok:
            liczba = [randint(0,100) for i in range(int(n))]

        self.ui.liczbaEdit.setText(str(len(self.liczby)))
        self.ui.liczbyEdit.setText(str(self.liczby))
        self.uzupelnij()

    def wczytaj(self):
        sciezka, _ = QFileDialog.getOpenFileName(self, 'Wczytaj plik', '.', 'Text files (*.csv)')
        if sciezka:
            with open(sciezka, 'r') as plik:
                zawartosc = plik.read()
                elementy = zawartosc.split(';')
                self.liczby = [int(element) for element in elementy]
                self.ui.liczbyEdit.setText(str(self.liczby))
        self.ui.liczbaEdit.setText(str(len(self.liczby)))
        self.uzupelnij()

    def srednia_arytmetyczna(self):
        return sum(self.liczby) / len(self.liczby)

    def srednia_geometryczna(self):
        iloczyn = 1
        for liczby in self.liczby:
            iloczyn *= liczby
        return iloczyn ** (1 / len(self.liczby)) #pierwiastek n-tego stopnia jako a do 1/n

    def uzupelnij(self):
        self.ui.arytmetycznaEdit.setText(f'{self.srednia_arytmetyczna():.2f}')
        self.ui.geometrycznaEdit.setText(f'{self.srednia_geometryczna():.2f}')
        self.ui.medianaEdit.setText(f'{self.mediana():.2f}')
        self.ui.dominantaEdit.setText(str(self.dominanta()))

    def mediana(self):
        dlugosc = len(self.liczby)
        liczby_posortowane = sorted(self.liczby)
        if dlugosc % 2 == 1: #nieparzysta
            return liczby_posortowane[dlugosc // 2]
        else:
            return (liczby_posortowane[dlugosc // 2 - 1] + liczby_posortowane[dlugosc // 2]) / 2

    def dominanta(self):
        wystapienia = {}
        for liczba in self.liczby:
            if liczba not in wystapienia.keys():
                wystapienia[liczba] = 1
            else:
                wystapienia[liczba] += 1

        max = 0
        max_argument = 0
        for klucz, wartosc in wystapienia.items(): #zwraca klucz wartosci
            if wartosc > max:
                max = wartosc
                max_argument = klucz

        return max_argument

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyForm()
    sys.exit(app.exec())