from .studienereignis import Studienereignis

class Abgabetermin(Studienereignis):
    """
    Spezialisierte Studienereignis-Klasse fuer Abgabetermine.
    """

    def anzeigen(self):
        """
        Gibt das Abgabedatum formatiert aus.
        """
        print(f"Abgabetermin: {self.beschreibung} am {self.datum}")
