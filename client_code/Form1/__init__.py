from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

class Form1(Form1Template):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        jugendherbergen = anvil.server.call('get_jugendherbergen', "name, JID")
        self.drop_down_1.items = [(name, jid) for name, jid in jugendherbergen]

        self.zimmer_liste = anvil.server.call('get_zimmer_for_jugendherbergen', "zimmernummer, bettenanzahl, preis_pro_nacht, gebucht, JID, ZID")

        preiskategorien = anvil.server.call('get_preiskategorie_for_jugendherbergen', "name, PID")
        self.drop_down_2.items = [(name, pid) for name, pid in preiskategorien]

        self.drop_down_3.items = []
        self.drop_down_4.items = []

        self.update_dropdown()
        self.update_buchungen()

      
    def update_buchungen(self):
      self.drop_down_4.items = anvil.server.call("get_buchungen")
  
    def update_dropdown(self):
      ausgewaehlte_jid = self.drop_down_1.selected_value
  
      if ausgewaehlte_jid:
          gefilterte_zimmer = [
              z for z in self.zimmer_liste if z[4] == ausgewaehlte_jid
          ]
          
          self.drop_down_3.items = [
              f"Zimmernummer: {z[0]}, Bettenanzahl: {z[1]}, Preis: {z[2]}€, Verfügbarkeit: {'Verfügbar' if not z[3] else 'Gebucht'}"
              for z in gefilterte_zimmer
          ]
      else:
          self.drop_down_3.items = []
  
    def drop_down_1_change(self, **event_args):
        self.update_dropdown()

    def button_1_click(self, **event_args):
        """Dieser Code wird ausgeführt, wenn der Button geklickt wird."""
        ausgewaehlte_jugendherberge = self.drop_down_1.selected_value
        ausgewaehlte_preiskategorie = self.drop_down_2.selected_value
        ausgewaehltes_zimmer = self.drop_down_3.selected_value

        if not ausgewaehlte_jugendherberge or not ausgewaehlte_preiskategorie or not ausgewaehltes_zimmer:
            alert("Bitte wählen Sie eine Jugendherberge, eine Preiskategorie und ein Zimmer aus!")
            return

        jugendherberge_name = next(
            (name for name, jid in self.drop_down_1.items if jid == ausgewaehlte_jugendherberge), "Unbekannt"
        )
        preiskategorie_name = next(
            (name for name, pid in self.drop_down_2.items if pid == ausgewaehlte_preiskategorie), "Unbekannt"
        )

        buchungs_string = (
            f"Jugendherberge: {jugendherberge_name}, "
            f"Preiskategorie: {preiskategorie_name}, "
            f"Zimmer: {ausgewaehltes_zimmer}"
        )

        start_datum = self.date_picker_1.date
        end_datum = self.date_picker_2.date
      
      
        buchungen = self.drop_down_4.items
        buchungen.append(buchungs_string)
        self.drop_down_4.items = buchungen

        weitere_user = []

        if (self.check_box_1.checked):
          weitere_user.append(self.check_box_1.text)

        if (self.check_box_2.checked):
          weitere_user.append(self.check_box_2.text)

        if (self.check_box_3.checked):
          weitere_user.append(self.check_box_3.text)
          
      
        #anvil.server.call("add_buchung", jugendherberge = jugendherberge_name, preiskategorie = preiskategorie_name, zimmer = ausgewaehltes_zimmer, start_datum = start_datum, end_datum = end_datum, weitere_user = weitere_user)

    def date_picker_1_change(self, **event_args):
        """Diese Methode wird aufgerufen, wenn das Datum im ersten DatePicker geändert wird"""
        selected_date_1 = self.date_picker_1.date

        if selected_date_1 is not None:
            self.date_picker_2.min_date = selected_date_1
            self.date_picker_2.selected_date = None

    def date_picker_2_change(self, **event_args):
        """Diese Methode wird aufgerufen, wenn das Datum im zweiten DatePicker geändert wird"""
        pass

