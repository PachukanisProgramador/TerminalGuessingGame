print('=================================\nBem-vindo ao jogo de adivinhação!\n=================================')
numero_secreto = 42

looping = True

while looping:
    chute = int(input('Digite o número que você acredita ser idêntico ao número secreto: '))

    if numero_secreto == chute:
        print('Número digitado : {}\nNúmero secreto: {}\n Você acertou! Parabéns!'.format(chute, numero_secreto))

        resposta = int(input('Fim do jogo!\n\nJogar novamente?\n1. Sim\n2. Não\n'))
        if resposta != 1:
            looping = False
    elif numero_secreto > chute:
        print('Que pena, você errou!\n {} é menor que o número secreto'.format(chute))
    elif numero_secreto < chute:
        print('Que pena, você errou!\n {} é maior que o número secreto'.format(chute))