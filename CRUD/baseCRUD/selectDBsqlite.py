import sqlite3

con = sqlite3.connect('bancoDados.db')
cur = con.cursor()


cur.execute("select * from produtos")
cur.execute("select * from produtos where preco > 30")
