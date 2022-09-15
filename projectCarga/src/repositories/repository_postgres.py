from projectCarga.src.configs.postgres.post_conn import *

def insert(con, obj):
    try:
        statement = con.cursor()
        sql = """INSERT INTO dbaseTest.carga (nome, carga, data, status) values (%s, %s, %s, %s)"""
        valores_tuple = (obj["nome"], obj["carga"], obj["data"], 1)
        statement.execute(sql, valores_tuple)
        return statement.rowcount == 1
        return {"sql": sql, "valores": valores_tuple}
    except psycopg2.DatabaseError as ex:
        con.rollback()
        return ex.msg
    finally:
        con.commit()
        statement.close()

def selectAll(con):
    try:
        statement = con.cursor()
        sql = """SELECT * FROM dbaseTest.carga WHERE status = 1"""
        statement.execute(sql)
        recordset = statement.fetchall()
        return recordset
    except psycopg2.DatabaseError as ex:
        con.rollback()
        return ex.msg
    finally:
        con.commit()
        statement.close()

def selectById(con, id):
    try:
        statement = con.cursor()
        sql = """SELECT * FROM dbaseTest.carga WHERE id = """+id+" AND status = 1"
        statement.execute(sql)
        record = statement.fetchone()
        return record
    except psycopg2.DatabaseError as ex:
        con.rollback()
        return ex.msg
    finally:
        con.commit()
        statement.close()

def deleteById(con, id):
    try:
        statement = con.cursor()
        sql = """UPDATE dbaseTest.carga SET status = False WHERE id = """+id
        statement.execute(sql)
        statement.close()
        return statement.rowcount == 1
    except psycopg2.DatabaseError as ex:
        con.rollback()
        return ex.msg
    finally:
        con.commit()
        statement.close()

def update(con, id, obj):
    try:
        statement = con.cursor()
        sql = """UPDATE dbaseTest.carga SET nome = %s, carga = %s, data = %s WHERE id = %s """
        valores = (obj["nome"], obj["carga"], obj["data"], id)
        statement.execute(sql, valores)
        return statement.rowcount == 1
    except psycopg2.DatabaseError as ex:
        con.rollback()
        return ex.msg
    finally:
        con.commit()
        statement.close()

def closeConn(con):
    fechar_conexao(con)


def init():
    return criar_conexao()


if __name__ == "__init__":
    init()