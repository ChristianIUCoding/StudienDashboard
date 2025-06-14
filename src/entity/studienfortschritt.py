class Studienfortschritt:
    """
    Verwaltet den Fortschritt eines Semesters (z.B. abgeschlossene Module).
    """

    def __init__(self):
        """
        Initialisiert mit null abgeschlossenen Modulen.
        """
        self.abgeschlossene_module = 0

    def aktualisieren(self):
        """
        Erhoeht die Anzahl der abgeschlossenen Module.
        """
        self.abgeschlossene_module += 1
