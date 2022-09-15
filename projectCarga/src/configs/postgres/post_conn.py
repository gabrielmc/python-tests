import psycopg2

def criar_conexao():
    return psycopg2.connect(database='dbaseTest', user='postgres', password='123456', host='localhost', port='5432')

def fechar_conexao(conn):
    return conn.close()
