import sqlite3

con = sqlite3.connect('bancoDados.db')
cur = con.cursor()


def update():
    cur.execute("update produtos set valor = 70.00 where valor = 90") # atualize configurando o valor pra 70 onde o valor for 90
    cur.execute("select * from produtos")
    con.commit()
    for i in cur.fetchall():
        print(i)
def deletar():
    cur.execute("delete from produtos where id = 10")
    cur.execute("select * from produtos")
    con.commit()
    for i in cur.fetchall():
        print(i)


update()
deletar()