import mysql.connector

def criar_conexao():
    return mysql.connector.connect(host='localhost', user='root', password='123456', database='sys')

def fechar_conexao(con):
    return con.close()
