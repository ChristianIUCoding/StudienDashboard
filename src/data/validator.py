from datetime import datetime

class Validator:
    """
    Diese Klasse enthaelt Hilfsmethoden zur Validierung von Benutzereingaben
    wie Noten und Datumsangaben.
    """

    @staticmethod
    def ist_gueltige_note(note: str) -> bool:
        """
        Prueft, ob die eingegebene Note gueltig ist.
        Gueltige Noten liegen im Bereich von 1.0 bis 5.0 (inklusive).
        :param note: Die eingegebene Note als String.
        :return: True, wenn die Note gueltig ist, sonst False.
        """
        try:
            wert = float(note)
            return 1.0 <= wert <= 5.0
        except ValueError:
            return False

    @staticmethod
    def ist_gueltiges_datum(datum_str: str) -> bool:
        """
        Prueft, ob ein String ein gueltiges Datum im Format 'YYYY-MM-DD' darstellt.
        :param datum_str: Das Datum als String.
        :return: True, wenn gueltig, sonst False.
        """
        try:
            datetime.strptime(datum_str, "%Y-%m-%d")
            return True
        except ValueError:
            return False
