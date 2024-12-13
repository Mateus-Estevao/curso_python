def calcular_pontos(valor_compra):
    if valor_compra > 1000:
        pontos = valor_compra * 0.2
    elif valor_compra > 500:
        pontos = valor_compra * 0.1
    else:
        pontos = valor_compra * 0.05
    return pontos

# Valores de compra
compras = {
    "Lucas": 1200,
    "Helena": 500,
    "Manuela": 750
}

# Calcular e imprimir os pontos
for nome, valor in compras.items():
    pontos = calcular_pontos(valor)
    print(f"{nome} acumulou {pontos} pontos.")
