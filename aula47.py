import os


palavra_secreta = 'perfume'
letras_acertadas = ''
numero_tentativas= 0

while True: 
    
    letra_digitada = input('Digite uma letra: ')
    numero_tentativas += 1
    
    
    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada
        
    palavra_formatada = ''        
    for letra_secreta in palavra_secreta: 
        if letra_secreta in letras_acertadas:
            palavra_formatada += letra_secreta
        else: 
            palavra_formatada += '*'
    print('palavra_formatada: ' + palavra_formatada)
    
    if palavra_formatada == palavra_secreta:
        os.system('clear')
        print('VOCE GANHOU! PARABÉNS!')
        print(f'A palavra era {palavra_secreta}')
        print(f'Voce tentou {numero_tentativas} vezes.')
        
        break
    


