# Jogo da Forca
def opcoes():
    print('\n============== JOGO DA FORCA ==============')
    print('Escolha uma opção:\n')
    opcao = -1

    while opcao != 0:
        opcao = int(input('1 - Nova Partida;\n0 - Sair do Jogo;\n===================\n'))
        if opcao == 1:
            jogar()
        elif opcao == 0:
            print('Obrigado!')
        else:
            print('Escolha somente 1 ou 0!\n')

def jogar():
    print('==============\nJogo da Forca\n==============\n')

    palavraSecreta = 'cereja'
    acertou = False
    enforcou = False
    erros = 0
    letrasAcertadas = ['_', '_', '_', '_', '_', '_']
    letrasUsadas = ''

    while not acertou and not enforcou:
        print(letrasAcertadas)
        if letrasUsadas != '':
            print('Letras Usadas: {}'.format(letrasUsadas))
        chute = input(str('Digite uma letra: '))
        letrasUsadas += chute + ' '

        if chute in palavraSecreta:
            posicao = 0
            for letra in palavraSecreta:
                if chute.lower() == letra.lower():
                    letrasAcertadas[posicao] = letra
                posicao += 1
            acertou = '_' not in letrasAcertadas  # '_' não está contido em LetrasAcertadas
        else:
            erros += 1
            print('Errou!\nErros: {} de {}\n'.format(erros, '7'))
            if erros == 7:
                enforcou = True
        # print(letrasAcertadas)
    if acertou:  # verificando se  acertou é True
        print('\nGanhou!\nParabéns!\n')
    else:
        print('Perdeu!\nA palavra correta era: {}\n'.format(palavraSecreta))
    print('FIM DE JOGO\n===============')


opcoes()


