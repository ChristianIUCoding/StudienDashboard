from src.controller.dashboard_controller import DashboardController
from src.ui.benutzer_interaktion import BenutzerInteraktion

def main():
    """
    Einstiegspunkt der Anwendung.
    Initialisiert Controller und UI.
    """
    controller = DashboardController()
    ui = BenutzerInteraktion(controller)
    ui.start()

if __name__ == "__main__":
    main()
