from .pruefungsleistung import Pruefungsleistung
from .abgabetermin import Abgabetermin

class Modul:
    """
    Repraesentiert ein Studienmodul mit Pruefungsleistung und Abgabetermin.
    """

    def __init__(self, name: str, pruefungsleistung: Pruefungsleistung, abgabetermin: Abgabetermin):
        """
        Erstellt ein neues Modul.
        :param name: Modulname
        :param pruefungsleistung: Pruefungsleistungs-Objekt
        :param abgabetermin: Abgabetermin-Objekt
        """
        self.name = name
        self.pruefungsleistung = pruefungsleistung
        self.abgabetermin = abgabetermin
