class Pruefungsleistung:
    """
    Repraesentiert eine Pruefungsleistung mit Note.
    """

    def __init__(self, titel: str, note: float):
        """
        Erstellt eine neue Pruefungsleistung.
        :param titel: Titel der Leistung (z.?B. Klausur, Projekt)
        :param note: Note (z.?B. 1.3)
        """
        self.titel = titel
        self.note = note
