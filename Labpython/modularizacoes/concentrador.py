from importador import operador as operador
#from .. (Sobe mais um nivel do arquivo atual)

preco = 1800
list_preco = [250, 300, 500]

imposto = operador.calcular_imposto(preco)
print(imposto)

impoto2 = operador.calcular_imposto_lam(preco)
print(impoto2)

impostos = list(map(operador.calcular_imposto_lam, list_preco))
print(impostos)