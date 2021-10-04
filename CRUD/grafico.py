import sqlite3
import matplotlib.pyplot as plt

# conexão
conn = sqlite3.connect("dsa.db")
# cursor
c = conn.cursor()


def create_table():
    # create the table
    c.execute("create table if not exists produtos(id integer primary key autoincrement not null, date text," \
              "prod_name text, valor real)")


def data_insertMannually():
    # insert datas
    c.execute(f"insert into produtos values(10, '24/07/1998', 'teclado', 90)")
    print("Dados inseridos com sucesso!")
    conn.commit()


def read():
    # read data
    c.execute('select * from produtos')
    for linhas in c.fetchall():
        # print(linhas[0])
        print(linhas)
    c.execute(f"select * from produtos where valor > 60")  # query(consulta) com restrição
    for linhas in c.fetchall():
        print(linhas)


def update():
    # update data
    c.execute("update produtos set valor = 70.00 where valor > 80")
    conn.commit()


def remove_data():
    # delete data
    c.execute("delete from produtos where id = 1")


def close():
    # close connections

    c.close()
    conn.close()
def graph():
    #generate the graph
    c.execute("select id, valor from produtos")
    ids = []
    valores = []
    for linha in c.fetchall():
        ids.append(linha[0])
        valores.append(linha[1])
    plt.bar(ids, valores) #(x, y)
    plt.show()


if __name__ == '__main__':
    create_table()
    # data_insertMannually()
    read()
    graph()
    close()
