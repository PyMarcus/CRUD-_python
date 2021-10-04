import sqlite3  # importa o sqlite

# cria a conexão com o banco de dados, se não existir, é criado
# o sqlite segue a lógica de arquivos
con = sqlite3.connect('bancoDados.db')  # apenas conecta
print(type(con))

#criar um cursor:
#cursor permite percorrer toods os registros no banco de dados
cur = con.cursor() #cria a ferramenta que irá percorr o banco

#criar instrução sql
sql_create = 'create table cursos'\
    '(id integer primary key ,'\
    'titulo varchar(100),'\
    'categria varchar(140))'

#executar a instrução no cursor
cur.execute(sql_create)
