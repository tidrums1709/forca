import random

from modelos.lista import obtem_lista


def inicia_game(lista_palavras):
    imprime_boas_vindas()
    palavra_escolhida = random.choice(lista_palavras).strip().upper()
    letras_acertadadas = monta_forca(palavra_escolhida)

    acertou = False
    errou = False
    erros = 0
    chutes = []

    while not acertou and not errou:
        chute = input("Qual letra deseja chutar? ").strip().upper()

        if chute not in chutes:
            chutes.append(chute)
            if chute in palavra_escolhida:
                marca_chute_correto(chute, letras_acertadadas, palavra_escolhida)
            else:
                erros += 1
                desenha_forca(erros)

            errou = erros == 7
            acertou = "_" not in letras_acertadadas
            print(letras_acertadadas)
        else:
            print("A letra {} já foi escolhida, tente outra letra.".format(chute))
    if acertou:
        imprime_mensagem_vencedor()
    if errou:
        imprime_mensagem_perdedor(palavra_escolhida)

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def imprime_mensagem_vencedor():
    print("Você ganhou!!!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def imprime_mensagem_perdedor(palavra_escolhida):
    print("Puxa, você foi enforcado!")
    print("Você perdeu a palavra secreta era {}!!!".format(palavra_escolhida))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def marca_chute_correto(chute, letras_acertadadas, palavra_escolhida):
    index = 0
    for letra in palavra_escolhida:
        if chute == letra:
            letras_acertadadas[index] = letra
        index += 1


def imprime_boas_vindas():
    print("***BEM VINDO AO JOGO DA FORCA****")


def monta_forca(palavra_escolhida):
    letras_acertadadas = ["_" for letra in palavra_escolhida]
    return letras_acertadadas


if __name__ == '__main__':
    lista_palavras = obtem_lista()
    inicia_game(lista_palavras)
