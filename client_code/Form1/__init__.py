from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

class Form1(Form1Template):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Initialisierung der Daten
        jugendherbergen = anvil.server.call('get_jugendherbergen', "name, JID")
        self.jugendherbergen = {jid: name for name, jid in jugendherbergen}  # Mapping JID zu Name

        zimmer = anvil.server.call('get_zimmer_for_jugendherbergen')
        self.zimmer = [
            {
                "zimmernummer": z[0],
                "bettenanzahl": z[1],
                "preis_pro_nacht": z[2],
                "gebucht": z[3],
                "JID": z[4],
                "ZID": z[5]
            }
            for z in zimmer
        ]

        # Dropdown 1 mit Jugendherbergen füllen
        self.drop_down_1.items = [(name, jid) for jid, name in self.jugendherbergen.items()]
        self.drop_down_1.selected_value = None

        # Dropdown 3 mit Zimmer-Daten füllen
        self.update_zimmer_dropdown()

    def update_zimmer_dropdown(self):
        """Aktualisiert Dropdown_3 basierend auf der ausgewählten Jugendherberge."""
        selected_jid = self.drop_down_1.selected_value

        if selected_jid is None:
            # Alle Zimmer anzeigen, falls keine Auswahl getroffen wurde
            filtered_zimmer = self.zimmer
        else:
            # Zimmer filtern nach ausgewählter Jugendherberge
            filtered_zimmer = [z for z in self.zimmer if z["JID"] == selected_jid]

        # Dropdown_3 mit gefilterten Zimmern aktualisieren
        self.drop_down_3.items = [
            f"Zimmernummer: {z['zimmernummer']}, Bettenanzahl: {z['bettenanzahl']}, "
            f"Preis: {z['preis_pro_nacht']}€, Verfügbarkeit: {'Verfügbar' if not z['gebucht'] else 'Gebucht'}"
            for z in filtered_zimmer
        ]

    def drop_down_1_change(self, **event_args):
        """Wird aufgerufen, wenn sich die Auswahl in Dropdown_1 ändert."""
        self.update_zimmer_dropdown()
