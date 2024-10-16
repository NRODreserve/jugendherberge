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

    self.drop_down_1.items = [("Satteins", 0), ("Mordor", 1)]
    print(anvil.server.call("say_hello", "sauron"))
    print(anvil.server.call("get_jugendherbergen"))

    self.drop_down_1.items = anvil.server.call('get_jugendherbergen', "name, JID")