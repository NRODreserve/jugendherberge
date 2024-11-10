from ._anvil_designer import Form1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Fetch Jugendherbergen and set drop_down_1 items with JID.
    jugendherbergen = anvil.server.call('get_jugendherbergen', "name, JID")
    print("Jugendherbergen:", jugendherbergen)  # Debug print
    self.drop_down_1.items = [(name, jid) for name, jid in jugendherbergen]

    self.drop_down_2.items = anvil.server.call('get_preiskategorie_for_jugendherbergen', "name, PID")

    # Map JID to name for easy lookup.
    self.jid_to_name = {jid: name for name, jid in jugendherbergen}

    # Fetch all Zimmer and print for debugging.
    self.listezimmer = anvil.server.call('get_zimmer_for_jugendherbergen')
    print("Zimmer data:", self.listezimmer)  # Debug print
    
    # Set the Jugendherberge dropdown event to filter Zimmer list on change.
    self.drop_down_1.set_event_handler("change", self.update_zimmer_dropdown)

  def update_zimmer_dropdown(self, **event_args):
    # Get the selected JID from drop_down_1.
    selected_jid = self.drop_down_1.selected_value
    print("Selected JID:", selected_jid)  # Debug print

    if selected_jid is not None:
      # Filter Zimmer based on the selected JID.
      filtered_zimmer = [
        zimmer for zimmer in self.listezimmer if zimmer[4] == selected_jid
      ]
      print("Filtered Zimmer:", filtered_zimmer)  # Debug print
      
      # Format the list of Zimmer for display.
      liste = [
        f"Zimmernummer: {zimmer[0]}, Bettenanzahl: {zimmer[1]}, Preis: {zimmer[2]}€, Verfügbarkeitsstatus: {'Gebucht' if zimmer[3] else 'Verfügbar'}"
        for zimmer in filtered_zimmer
      ]
      
      self.drop_down_3.items = liste
    else:
      # Clear the Zimmer list if no Jugendherberge is selected.
      self.drop_down_3.items = []