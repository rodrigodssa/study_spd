import random
def jogo_adivinhacao():
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    max_tentativas = 10
    while tentativas < max_tentativas:
        palpite = int(input("Digite seu palpite: "))
        tentativas += 1
        if palpite < numero_secreto:
            print("Muito baixo!")
        elif palpite > numero_secreto:
            print("Muito alto!")
        else:
            print(f"Parabéns! Você acertou em {tentativas} tentativas.")
            return
        print(f"Você atingiu o número máximo de tentativas. O número era {numero_secreto}.")

jogo_adivinhacao()

