from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

class Form1(Form1Template):
    def __init__(self, **properties):
        # Form-Eigenschaften und Datenbindungen setzen.
        self.init_components(**properties)

        # Jugendherbergen abrufen und Dropdown-Elemente festlegen
        jugendherbergen_daten = anvil.server.call('get_jugendherbergen', "name, JID")
        self.drop_down_1.items = [(name, jid) for name, jid in jugendherbergen_daten]

        # Zimmerdaten laden
        self.zimmer_daten_liste = anvil.server.call(
            'get_zimmer_for_jugendherbergen', 
            "zimmernummer, bettenanzahl, preis_pro_nacht, gebucht, JID, ZID"
        )

        # Preiskategorien abrufen
        preiskategorien = anvil.server.call('get_preiskategorie_for_jugendherbergen', "name, PID")
        self.drop_down_2.items = [(name, pid) for name, pid in preiskategorien]

        # Initialisieren der Dropdown-Optionen
        self.drop_down_3.items = []
        self.drop_down_4.items = []

        self.aktualisiere_zimmer_dropdown()
        self.aktualisiere_buchungen()

    def aktualisiere_buchungen(self):
        # Buchungen abrufen und Dropdown-Elemente aktualisieren
        self.drop_down_4.items = anvil.server.call("get_buchungen")

    def aktualisiere_zimmer_dropdown(self):
        ausgewaehlte_jugendherberge = self.drop_down_1.selected_value

        if ausgewaehlte_jugendherberge:
            gefilterte_zimmer = [
                z for z in self.zimmer_daten_liste if z[4] == ausgewaehlte_jugendherberge
            ]
            
            self.drop_down_3.items = [
                f"Zimmernummer: {z[0]}, Bettenanzahl: {z[1]}, Preis: {z[2]}€, "
                f"Verfuegbarkeit: {'Verfuegbar' if not z[3] else 'Gebucht'}"
                for z in gefilterte_zimmer
            ]
        else:
            self.drop_down_3.items = []

    def drop_down_1_change(self, **event_args):
        # Aktualisieren der Zimmer, wenn eine Herberge ausgewaehlt wird
        self.aktualisiere_zimmer_dropdown()

    def button_1_click(self, **event_args):
        # Wird ausgefuehrt, wenn der Buchungs-Button angeklickt wird.
        ausgewaehlte_jugendherberge_id = self.drop_down_1.selected_value
        ausgewaehlte_preiskategorie_id = self.drop_down_2.selected_value
        ausgewaehltes_zimmer = self.drop_down_3.selected_value

        if not ausgewaehlte_jugendherberge_id or not ausgewaehlte_preiskategorie_id or not ausgewaehltes_zimmer:
            alert("Bitte waehlen Sie eine Jugendherberge, eine Preiskategorie und ein Zimmer aus!")
            return
  
        jugendherberge_name = next(
            (name for name, jid in self.drop_down_1.items if jid == ausgewaehlte_jugendherberge_id), "Unbekannt"
        )
        preiskategorie_name = next(
            (name for name, pid in self.drop_down_2.items if pid == ausgewaehlte_preiskategorie_id), "Unbekannt"
        )
  
        buchungs_details = (
            f"Jugendherberge: {jugendherberge_name}, "
            f"Preiskategorie: {preiskategorie_name}, "
            f"Zimmer: {ausgewaehltes_zimmer}"
        )
  
        # Aktualisiere die Drop-down-Liste mit der neuen Buchung
        aktuelle_buchungen = list(self.drop_down_4.items)  # Lade vorhandene Buchungen
        aktuelle_buchungen.append(buchungs_details)  # Fuege neue Buchung hinzu
        self.drop_down_4.items = aktuelle_buchungen  # Aktualisiere die Drop-down-Liste

    def datum_von_picker_change(self, **event_args):
        """Aktualisiert die Mindestdatumsauswahl fuer das Abreisedatum."""
        datum_von = self.date_picker_von.date

        if datum_von is not None:
            self.date_picker_bis.min_date = datum_von
            self.date_picker_bis.selected_date = None

    def datum_bis_picker_change(self, **event_args):
        """Wird ausgefuehrt, wenn das Abreisedatum geaendert wird."""
        pass

    def drop_down_buchungen_change(self, **event_args):
        """Wird ausgefuehrt, wenn eine Buchung ausgewaehlt wird."""
        pass

    def drop_down_preiskategorien_change(self, **event_args):
        """Wird ausgefuehrt, wenn eine Preiskategorie ausgewaehlt wird."""
        pass

    def drop_down_4_change(self, **event_args):
        """Wird ausgefuehrt, wenn ein Element ausgewaehlt wird."""
        pass
