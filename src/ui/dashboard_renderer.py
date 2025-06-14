class DashboardRenderer:
    """
    Konsolenausgabe zur Darstellung von Studieninhalten.
    Zeigt Semester, Module, Noten und Abgabetermine.
    """

    def render(self, studiengang):
        print(f"\nStudiengang: {studiengang.name}")
        for semester in studiengang.semester:
            print(f"  Semester {semester.nummer}:")
            for modul in semester.module:
                print(f"    Modul: {modul.name}, Note: {modul.pruefungsleistung.note}")
                modul.abgabetermin.anzeigen()
