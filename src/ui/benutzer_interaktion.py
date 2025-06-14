from .dashboard_renderer import DashboardRenderer

class BenutzerInteraktion:
    """
    Textbasierte Benutzerschnittstelle fuer die Navigation im Dashboard.
    Ruft Eingaben vom Nutzer ab und leitet sie an den Controller weiter.
    """

    def __init__(self, controller):
        """
        Initialisiert die Benutzeroberflaeche mit einem gegebenen Controller.

        :param controller: Instanz des DashboardControllers
        """
        self.controller = controller

    def start(self):
        """
        Startet das System mit Beispiel-Daten und oeffnet das Hauptmenue.
        """
        self.controller.beispiel_daten_erstellen()
        self.menue()

    def menue(self):
        """
        Zeigt das Hauptmenue an und verarbeitet Nutzereingaben.
        """
        while True:
            print("\n--- Studien-Dashboard ---")
            print("1. Studiengang anzeigen")
            print("0. Beenden")

            auswahl = input("Auswahl: ")

            if auswahl == "1":
                renderer = DashboardRenderer()
                renderer.render(self.controller.gib_studiengang())
            elif auswahl == "0":
                print("Programm beendet.")
                break
            else:
                print("Ungueltige Eingabe.")
