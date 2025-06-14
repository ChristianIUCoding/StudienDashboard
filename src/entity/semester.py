from .modul import Modul
from .arbeitsaufwand import Arbeitsaufwand
from .studienfortschritt import Studienfortschritt

class Semester:
    """
    Repraesentiert ein Studiensemester mit Modulen und Arbeitsaufwand.
    """

    def __init__(self, nummer: int):
        """
        Erstellt ein neues Semester.
        :param nummer: Semesternummer (z.?B. 1, 2, 3 ...)
        """
        self.nummer = nummer
        self.module = []
        self.arbeitsaufwand = []
        self.fortschritt = Studienfortschritt()

    def modul_hinzufuegen(self, modul: Modul):
        """
        Fuegt ein Modul zum Semester hinzu und aktualisiert den Fortschritt.
        :param modul: Modul-Objekt
        """
        self.module.append(modul)
        self.fortschritt.aktualisieren()
