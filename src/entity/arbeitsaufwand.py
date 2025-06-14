from datetime import date

class Arbeitsaufwand:
    """
    Repraesentiert einen Aufwandseintrag in Stunden.
    """

    def __init__(self, stunden: int, datum: date):
        """
        Erstellt einen Aufwandseintrag.
        :param stunden: Anzahl der Stunden
        :param datum: Datum der Aufzeichnung
        """
        self.stunden = stunden
        self.datum = datum
