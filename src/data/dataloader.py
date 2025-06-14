import json
from src.entity.studiengang import Studiengang

class DataLoader:
    """
    Verantwortlich fuer das Speichern und Laden von Studiengangsdaten in JSON-Dateien.
    Ermoeglicht die Persistenz der Studiengangsstruktur ueber einfache Serialisierung.
    """

    @staticmethod
    def speichern(studiengang: Studiengang, pfad: str):
        """
        Speichert einen Studiengang als strukturierte JSON-Datei.
        :param studiengang: Das Studiengang-Objekt, das gespeichert werden soll.
        :param pfad: Pfad zur Zieldatei auf dem Dateisystem.
        """
        data = {
            "name": studiengang.name,
            "semester": [
                {
                    "nummer": sem.nummer,
                    "module": [
                        {
                            "name": mod.name,
                            "note": mod.pruefungsleistung.note,
                            "abgabetermin": str(mod.abgabetermin.datum),
                            "beschreibung": mod.abgabetermin.beschreibung
                        } for mod in sem.module
                    ]
                } for sem in studiengang.semester
            ]
        }

        with open(pfad, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    @staticmethod
    def laden(pfad: str) -> dict:
        """
        Laedt ein Studiengang-Datenobjekt aus einer JSON-Datei.
        :param pfad: Pfad zur JSON-Datei.
        :return: Ein Dictionary mit deserialisierten Daten.
        """
        with open(pfad, "r", encoding="utf-8") as f:
            return json.load(f)
