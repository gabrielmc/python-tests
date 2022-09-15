#import request
import time

# criar um decorator para calcular o tempo de uma requisição
# wrapper(): #invólucro da ação, é uma função dentro de outra

def calcular_tempo(function):
    def wrapper():
        tempo_inicial = time.time()
        function()
        tempo_final = time.time()
        duracao = (tempo_final - tempo_inicial)
        print(f'Duração da requisição foi de {duracao} segundos')
    return wrapper


