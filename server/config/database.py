import sqlite3
from wrap_connection import transact

create_sql = """
CREATE TABLE IF NOT EXISTS ImagemTexto (
    id INTEGER PRIMARY KEY,
    imagem TEXT NOT NULL,
    texto TEXT NOT NULL
)
"""

def con():
    return sqlite3.connect("galeria.db")

@transact(con)
def criar_bd():
    cursor.execute(create_sql)
    connection.commit()
