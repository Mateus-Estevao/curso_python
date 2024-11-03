primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor > segundo_valor:
    print(f'O primeiro valor é {primeiro_valor}, maior que o segundo.')
elif primeiro_valor == segundo_valor:
    print('Os valores informados são iguais.')
else:
    print(f'O segundo valor é {segundo_valor}, maior que o segundo.')