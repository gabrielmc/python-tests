import mysql
from MysqlConn.conn import criar_conexao, fechar_conexao

"""
Estudar como concatenar paramentros em MySql
#valores_tuple = {id}
#valores_tuple = {'id': int(id)}  int() / float()
#valores_tuple = (id, value1, value2)
"""
def insert(con, obj):
    try:
        statement = con.cursor()
        sql = """INSERT INTO sys.Carga (nome, carga, data, status) values (%s, %s, %s, %s)"""
        valores_tuple = (obj["nome"], obj["carga"], obj["data"], 1)
        statement.execute(sql, valores_tuple)
        return statement.rowcount == 1
    except mysql.connector.errors.InterfaceError as ex:
        con.rollback()
        return ex.msg
    finally:
        con.commit()
        statement.close()

def selectById(con, id):
    try:
        statement = con.cursor()
        sql = """SELECT * FROM sys.Carga WHERE id = """+id+" AND status = 1"
        statement.execute(sql)
        record = statement.fetchone()
        return record
    except mysql.connector.errors.InterfaceError as ex:
        con.rollback()
        return ex.msg
    finally:
        con.commit()
        statement.close()

def deleteById(con, id):
    try:
        statement = con.cursor()
        sql = """UPDATE sys.Carga SET status = False WHERE id = """+id
        statement.execute(sql)
        statement.close()
        return statement.rowcount == 1
    except mysql.connector.errors.InterfaceError as ex:
        con.rollback()
        return ex.msg
    finally:
        con.commit()
        statement.close()

def selectAll(con):
    try:
        statement = con.cursor()
        sql = """SELECT * FROM sys.Carga WHERE status = 1"""
        statement.execute(sql)
        recordset = statement.fetchall()
        return recordset
    except mysql.connector.errors.InterfaceError as ex:
        con.rollback()
        return ex.msg
    finally:
        con.commit()
        statement.close()

def update(con, id, obj):
    try:
        statement = con.cursor()
        sql = """UPDATE sys.Carga SET nome = %s, carga = %s, data = %s WHERE id = %s """
        valores = (obj["nome"], obj["carga"], obj["data"], id)
        statement.execute(sql, valores)
        return statement.rowcount == 1
    except mysql.connector.errors.InterfaceError as ex:
        con.rollback()
        return ex.msg
    finally:
        con.commit()
        statement.close()

def closeConn(con):
    fechar_conexao(con)

def init():
    connect = criar_conexao("localhost", "root", "123456", "sys")
    return connect


if __name__ == "__init__":
    init()