print("*******************************")
print("Bem-vindo ao jogo de advinhação")
print("********************************")

numero_secreto = 42
tentativas = 3
rodada = 0

while rodada < tentativas:
    rodada += 1
    print("Tentativa", rodada, "de", tentativas)
    chute = input("Digite seu número: ")
    print("Você digitou: ", chute)

    numero = int(chute)
    acerto = numero == numero_secreto
    isMaior = numero > numero_secreto
    isMenor = numero < numero_secreto

    if acerto:
        print("Você acertou! =)")
        break
    else:
        if isMaior:
            print("Você errou! Seu chute foi para cima")
        elif isMenor:
            print("Você errou! Seu chute foi para baixo")

print("Fim do jogo")
