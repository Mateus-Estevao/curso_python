# entrada = input('Digite um numero inteiro: ')

# if entrada.isdigit():
#     entrada_int = int(entrada)
#     par_impar = entrada_int % 2 == 0
#     par_impar_text = 'Impar'

#     if par_impar is True:
#         par_impar_text = 'Par'
#     print(f'O numero {entrada_int} é {par_impar_text}')
# else:
#     print('Você não digotu um numero inteiro')
#######################################################################

# horario = input('Digite a hora: ')

# try:
#     horario_int = int(horario)
#     if horario_int >= 0 and horario_int <= 11:
#         print('Bom dia')
#     elif horario_int <= 17:
#         print('Boa tarde!')
#     else:
#         print('Boa noite')
# except:
#     print('Por favor digite um numero inteiro')


###################g##################################################

nome = input('Digite seu nome: ')
tamanho_nome = len(nome)

try:
    if tamanho_nome > 0 and tamanho_nome <= 4:
        print('Seu nome é pequeno')
    elif tamanho_nome < 6 :
        print('Seu nome é normal')
    elif tamanho_nome > 6:
        print('Seu nome é grande')
except:
    pass