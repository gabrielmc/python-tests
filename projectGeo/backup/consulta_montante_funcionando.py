# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 22:08:40 2021
@author: cadfj, gabrielmuniz
"""

import geopandas as gpd
import matplotlib.pyplot as plt

# conexão com o banco ('tipo do banco://user:password@host:port/db')
User = str(input('Nome usuário: '))
Password = str(input('Senha: '))
Host = str(input('Host: '))
Porta = int(input('Porta: '))
db = str(input('Banco de Dados: '))
engine = db.create_engine(f'postgresql://{User}:{Password}@{Host}:{Porta}/{db}')
# engine = db.create_engine('postgresql://postgres:postgres@localhost:5432/otto')
con = engine.connect()

# criando os inputs (variáveis), para o usuário inserir as coordendas de interesse
long = input("insira longitude (graus decimais):")
lat = input("insira latitude(graus decimais):")

# consultando o banco através da função read_postgis
sql_query = f'select * from public.fn_contribuicao_montante ({long},{lat});'
consulta_otto = gpd.read_postgis(sql=sql_query,con=con)
consulta_otto.head()

# visualizando resultados
consulta_otto.head().plot(figsize=(16, 14), facecolor='white', edgecolor='black')
plt.title(f'Consulta Montante (Coordenadas{long},{lat})')
plt.show()
