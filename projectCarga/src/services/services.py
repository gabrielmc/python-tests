from projectCarga.src.repositories.repository_mysql import *
from mysql.connector import Error


def inserirService(obj):
    try:
        conn = init()
        return insert(conn, obj)
    except Error as er:
        return ('Error:', er.msg)
    finally:
        closeConn(conn)


def selectAllService():
    try:
        conn = init()
        return selectAll(conn)
    except Error as er:
        return ('Error:', er.msg)
    finally:
        closeConn(conn)


def selectByIdService(id):
    try:
        conn = init()
        return selectById(conn, id)
    except Error as er:
        return ('Error:', er.msg)
    finally:
        closeConn(conn)


def deleteByIdService(id):
    try:
        conn = init()
        return deleteById(conn, id)
    except Error as er:
        return ('Error:', er.msg)
    finally:
        closeConn(conn)


def updateService(id, obj):
    try:
        conn = init()
        return update(conn, id, obj)
    except Error as er:
        return ('Error:', er.msg)
    finally:
        closeConn(conn)
