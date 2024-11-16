import anvil.server
import sqlite3
from anvil.files import data_files

# Verbindung zur SQLite-Datenbank herstellen
@anvil.server.callable
def get_jugendherbergen(rows="*"):
    conn = sqlite3.connect(data_files['jugendherbergen_verwaltung.db'])
    cursor = conn.cursor()
    res = list(cursor.execute(f"SELECT {rows} FROM jugendherbergen"))
    return res

@anvil.server.callable
def get_preiskategorie_for_jugendherbergen(rows="*"):
    conn = sqlite3.connect(data_files['jugendherbergen_verwaltung.db'])
    cursor = conn.cursor()
    res = list(cursor.execute(f"SELECT {rows} FROM preiskategorie"))
    return res

@anvil.server.callable
def get_zimmer_for_jugendherbergen(rows="*"):
    conn = sqlite3.connect(data_files['jugendherbergen_verwaltung.db'])
    cursor = conn.cursor()
    res = list(cursor.execute(f"SELECT {rows} FROM zimmer"))
    return res
