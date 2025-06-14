from abc import ABC, abstractmethod
from datetime import date

class Studienereignis(ABC):
    """
    Abstrakte Basisklasse fuer alle Studienereignisse (z.?B. Abgabetermine).
    """

    def __init__(self, datum: date, beschreibung: str):
        """
        Initialisiert ein Studienereignis.
        :param datum: Datum des Ereignisses
        :param beschreibung: Beschreibung des Ereignisses
        """
        self.datum = datum
        self.beschreibung = beschreibung

    @abstractmethod
    def anzeigen(self):
        """
        Abstrakte Methode zur Darstellung des Ereignisses.
        Muss von Unterklassen implementiert werden.
        """
        pass
