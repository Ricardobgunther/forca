import random
palavras = ['banana', 'melancia', 'morango', 'kiwi','limao','abacaxi']
palavra = random.choice(palavras)
letras_repetidas = ''
max_tentativas = 6
nome = input("Desafiante(1) Competidor(2) \n")

print("Escolha uma dica: ")
print("(1) Dica 1")
print("(2) Dica 2")
print("(3) Dica 3")

dicas = input("Opção escolhida: ")
if dicas == "1":
    print("Dica 1: É comestível")
elif dicas == "2":
    print("Dica 2: É uma fruta")
elif dicas == "3":
    print("Dica 3: Se vira nos 30 ")
else:
    print("Você não está colaborando...")

while True:
    palavra_exibida = ''
    for letra in palavra:
        if letra in letras_repetidas:
            palavra_exibida += letra
        else:
            palavra_exibida += '_'
    print(palavra_exibida)

    letra = input('Escreva uma letra: ')

    if letra in letras_repetidas:
        print('Essa letra foi repetida.')
    else:
        letras_repetidas += letra

        if letra in palavra:
            print('Acertou!')
        else:
            print('Errou!')
            max_tentativas -= 1
            if max_tentativas == 0:
                print('Tente novamente! A palavra correta era:', palavra)
                break

    if set(palavra) == set(letras_repetidas):
        print('Você ganhou!')
        break