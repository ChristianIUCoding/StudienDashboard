from .semester import Semester

class Studiengang:
    """
    Repraesentiert einen Studiengang mit mehreren Semestern.
    """

    def __init__(self, name: str):
        """
        Erstellt einen neuen Studiengang.
        :param name: Name des Studiengangs
        """
        self.name = name
        self.semester = []

    def semester_hinzufuegen(self, semester: Semester):
        """
        Fuegt ein Semester zum Studiengang hinzu.
        :param semester: Semester-Objekt
        """
        self.semester.append(semester)
