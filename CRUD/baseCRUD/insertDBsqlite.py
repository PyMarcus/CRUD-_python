import sqlite3

con = sqlite3.connect('bancoDados.db')
cur = con.cursor()

# cria outra sentença sql para inserir registros
sql_insert = 'insert into cursos values (?, ?, ?)' # vai receber 3 colunas de valores, por linha, a tabela curso

# dados
recset = [(1000, 'Ciência de dados', 'Data Science'),
          (1001, 'Big Data Fundamentos', 'Big Data')]

# inserir nos registros
for rec in recset:
    cur.execute(sql_insert, rec)

# contudo, embora os dados tenham sido inseridos, em um banco de dados relacional, deve-se inserir
# deve se gravá-los
con.commit() # salva as alterações



#selecionar os registros com outra sentença SQL:
sql_select = 'select * from cursos'
# seleciona e recupera os registros
cur.execute(sql_select)
dados = cur.fetchall() #buscar tudo

# exibir:
for linha in dados:
    print("Curso id: %d, Título: %s, Categoria: %s\n " % linha)

con.close() # fechar conexão para evitar que haja corrupção dos dados.
