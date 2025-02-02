import re
import sys

# cpf = '842.337.620-63' \
#     .replace('.','')\
#     .replace('-','')
entrada = input('Digite um CPF: ')
cpf = re.sub(
    r'[^0-9]',
    '',
    entrada
    )

entrada_sequencial = entrada == entrada[0] * len(entrada)

if entrada_sequencial:
    print('Você enviou dados sequencias.')
    sys.exit()
 


nove_digito = cpf[:9]
contador_regresivo_1 = 10

resultado_digito_1 = 0

for digito in nove_digito:
    resultado_digito_1 += int(digito) * contador_regresivo_1
    contador_regresivo_1 -= 1

digito_1 = (resultado_digito_1 * 10 ) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0


dez_digito = nove_digito + str(digito_1)
contador_regresivo_2 = 11
resultado_digito_2 = 0

for digito in dez_digito:
    resultado_digito_2 += int(digito) * contador_regresivo_2
    contador_regresivo_2 -= 1

digito_2 = (resultado_digito_2 * 10 ) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

cpf_gerado = f'{nove_digito}{digito_1}{digito_2}'



if cpf_gerado == cpf:
    print(f'{cpf_gerado} CPF é válido')
else:
    print(f'{cpf} é invalido')







