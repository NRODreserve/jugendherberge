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

    # Any code you write here will run before the form opens.
    
    print(anvil.server.call("get_jugendherbergen"))
    jugendherbergen = anvil.server.call('get_jugendherbergen', "name, JID")
    self.drop_down_1.items = jugendherbergen

    print(anvil.server.call("get_preiskategorie_for_jugendherbergen"))
    self.drop_down_2.items = anvil.server.call('get_preiskategorie_for_jugendherbergen', "name, PID")

  
    jid_to_name = {jid: name for name, jid in jugendherbergen}

    print(anvil.server.call("get_zimmer_for_jugendherbergen"))
    self.listezimmer = [(zimmernummer, bettenanzahl, preis_pro_nacht, gebucht, JID, ZID) for zimmernummer, bettenanzahl, preis_pro_nacht, gebucht, JID, ZID in anvil.server.call('get_zimmer_for_jugendherbergen')]

    liste = []
    
    for i in self.listezimmer:
     jugendherberge_name = jid_to_name.get(i[5], "Unknown")
     status = "Verfügbar" if not i[4] else "Gebucht"
     liste.append(f"Zimmernummer: {i[1]}, Bettenanzahl: {i[2]}, Preis: {i[3]}€, Jugendherberge: {jugendherberge_name}, Verfügbarkeitsstatus: {status}")
      
    
    self.drop_down_3.items = liste 