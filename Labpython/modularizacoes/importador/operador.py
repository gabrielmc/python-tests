# Em function
def calcular_imposto(preco):
    return preco - 0.3 # subtrai 30% baseado em impostos

# Em Lambda
calcular_imposto_lam = (lambda value: value * 0.3)
