# -*- coding:UTF-8 -*-
import sqlite3
import time
import datetime
import random
from GeStock_Users import *
from GeStock_HistoryIn import *

conn = sqlite3.connect("users.db")
c = conn.cursor()

def initHistoryOut():
        c.execute("CREATE TABLE IF NOT EXISTS historyOut(idCarte INTEGER, idProduit INTEGER, timestamp VARCHAR)")
    

def historyOut(idCarte, idProduit):
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H: %M:%S'))
    c.execute("INSERT INTO historyOut (idCarte, idProduit, timestamp) VALUES (?, ?, ?)",
              (idCarte, idProduit, date))
    conn.commit()
    print("Ajout dans l'historique ...")
    time.sleep(1)
