from src.entity.studiengang import Studiengang
from src.entity.semester import Semester
from src.entity.modul import Modul
from src.entity.pruefungsleistung import Pruefungsleistung
from src.entity.abgabetermin import Abgabetermin
from datetime import date

class DashboardController:
    """
    Zentrale Steuerungseinheit des Dashboards.
    Koordiniert die Erstellung und Verwaltung von Studiengangsdaten.
    """

    def __init__(self):
        """
        Initialisiert den Controller mit einem leeren Studiengang.
        """
        self.studiengang = Studiengang("Informatik")

    def beispiel_daten_erstellen(self):
        """
        Erstellt ein vordefiniertes Beispiel-Semester mit einem Modul,
        Pruefungsleistung und Abgabetermin.
        """
        pruefung = Pruefungsleistung("Mathematik", 1.7)
        abgabe = Abgabetermin(date(2025, 7, 1), "Hausarbeit")
        modul = Modul("Mathematik", pruefung, abgabe)

        semester1 = Semester(1)
        semester1.modul_hinzufuegen(modul)

        self.studiengang.semester_hinzufuegen(semester1)

    def gib_studiengang(self) -> Studiengang:
        """
        Gibt das aktuelle Studiengangsobjekt zurueck.

        :return: Studiengang-Instanz
        """
        return self.studiengang
