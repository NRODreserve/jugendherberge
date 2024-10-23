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
    self.drop_down_1.items = anvil.server.call('get_jugendherbergen', "name, JID")

    #print(anvil.server.call("get_zimmer_for_jugendherbergen"))
    #self.drop_down_2.items = anvil.server.call('get_zimmer_for_jugendherbergen', "schlafplätze, ZID, JID")