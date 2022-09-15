# Lambda com funções em python
# Exemplo de calcular imposto

preco = 1800
list_preco = [250, 300, 500]

def calcular_imposto(preco):
    return preco - 0.3 # 30%

print(calcular_imposto(preco))

# Em Lambda
calcular_imposto_lam = (lambda value: value * 0.3)
print(calcular_imposto_lam(preco))


# Em Lambda com lista
# list( map( função, lista ) ) 
# função = está relacionada a operação que sera aplicada a cada valor
# lista = a lista de valores atribuidos para que se faça a operação desejada
impostos = list(map(calcular_imposto_lam, list_preco))
print(impostos)