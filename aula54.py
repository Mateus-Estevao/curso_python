import os

lista= []

opcao_digitada = ''

print('Bem vindo a lista de compra')

while True:
    os.system('clear')
    opcao_digitada= input(
    'Digite  opção deseja:\n'
    '1 - Adicionar item\n'
    '2 - Remover item\n'
    '3 - Visualizar lista\n'
    '4 - Sair\n')
    
    if opcao_digitada == '1':
        os.system('clear')
        valor = input('Valor: ')
        lista.append(valor)
        

    elif opcao_digitada == '2':
        os.system('clear')
        indice_str = input('Escolha o indice que deseja remover: ')
    
        try:
            indice = int(indice_str)
            del lista[indice]
        except:
            print('Digite um indice valido')

    elif opcao_digitada == '3':
        os.system('clear')
        if len(lista) == 0:
            print('A lista esta vazia')
        else:
            for indice, item in enumerate(lista):
                print(indice, item)            
    elif opcao_digitada == '4':
        break
    
    else:
        print('Opção invalida')
     
            
