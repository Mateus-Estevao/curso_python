""" Calculadora com while"""

while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite um operador (+,-,/,*): ')
    
    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numero_validos = True
    except:
        numero_validos = None

    if numero_validos is None:
        print('Uns dos numeros digitados é invalido.')
        continue

    operadores_permitidos = '+-/*'

    if operadores_permitidos not in operadores_permitidos:
        print('Operador inválido.')
        continue
    print(num_1_float + num_2_float)
    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    print('Realizando o calculo...Confira o resultado abaixo:')

    if operador == '+':
        print(num_1_float + num_2_float)
    elif operador == '-':
        print(num_1_float - num_2_float)
    elif operador == '*':
        print(num_1_float * num_2_float)
    elif operador == '/':
        print(num_1_float / num_2_float)

    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break