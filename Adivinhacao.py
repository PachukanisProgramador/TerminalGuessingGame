import this

print('=======================\nBem-vindo ao jogo de adivinhação!\n=======================')
numero_secreto = 42

looping = True
total_tentativas = 15

while total_tentativas:
    chute = int(input('Digite o número que você acredita ser idêntico ao número secreto entre 1 e 100: '))

    if chute < 1 or chute > 100:
        print('Valor inválido.', end=' ')
    else:
        acertou = numero_secreto == chute

        if acertou:
            print(f'Correto!\n{numero_secreto} é o número secreto! Parabéns!')

            this.resposta = 0
            while this.resposta != 1 or this.resposta != 2:
                this.resposta = int(input('Fim do jogo!\n\nJogar novamente?\n1. Sim\n2. Não\n'))

                if this.resposta == 2:
                    print('Obrigado por jogar!')
                    break
                elif this.resposta == 1:
                    total_tentativas = 15
                    break
                else:
                    print('Comando inválido. Digite novamente')
            if this.resposta == 2:
                break
        elif numero_secreto > chute:
            total_tentativas -= 1
            print(f'Que pena, você errou!\nO número {chute} é menor que o número secreto\n\nTentativas restantes: {total_tentativas}')

        else:
            print(f'Que pena, você errou!\nO número {chute} é maior que o número secreto\n\nTentativas restantes: {total_tentativas}')
            total_tentativas -= 1

    if total_tentativas == 0:
        resposta = int(input('Que pena, todas as suas tentativas esgotaram.\nJogar novamente? 1. Sim\n2. Não'))
        if resposta == 1:
            total_tentativas = 15
        else:
            print('Obrigado por jogar!')
            break
