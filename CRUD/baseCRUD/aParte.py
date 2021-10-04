import datetime
import random
import sqlite3

con = sqlite3.connect("bancoDados.db")  # conecta ao banco de dados
cursor = con.cursor()  # cria o ponteiro do banco de dados


def createTable(nome):
    """
    parametro: nome da tabela
    funçao: cria tabela
    return: nome da tabela
    """
    cursor.execute(
        f"create table if not exists {nome}(id integer primary key autoincrement not null, date text, prod_name text, valor real)")
    print(f"tabela {nome} criada com sucesso!")
    return nome


def data_insertMannually(funcao):
    nome_table = funcao
    cursor.execute(f"insert into {nome_table} values(10, '24/07/1998', 'teclado', 90)")
    print("Dados inseridos com sucesso!")
    con.commit()
    cursor.close()
    con.close()


def data_insertAuto(funcao):
    nome_table = funcao
    cursor.execute(f"insert into {nome_table} values(?,?,?,?)",
                   (11, datetime.datetime.now(), 'teclado', random.randint(1, 100)))
    print("Dados inseridos com sucesso!")
    con.commit()
    cursor.close()
    con.close()


def leitura(nome):
    cursor.execute('select * from {nome}'.format(nome=nome))
    for linhas in cursor.fetchall():
        #print(linhas[0])
        print(linhas)
    cursor.execute(f"select * from {nome} where valor > 60") # query(consulta) com restrição
    for linhas in cursor.fetchall():
        print(linhas)

nome = "produtos"
#createTable(nome)
#data_insertAuto(createTable(nome))
leitura(nome)
