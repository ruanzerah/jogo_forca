import random


def carregar_arquivo_lista(arquivo):
    try:
        with open(arquivo, "rt") as arquivo:
            lista = arquivo.read().splitlines()
    except FileNotFoundError:
        print("Arquivo nao encontrado")
    else:
        return lista
    finally:
        arquivo.close()

def criar_forca(lista_secreta, num_tentativas=5):
    global pontuacao
    palavra_secreta = random.choice(lista_secreta)
    palavra_secreta = palavra_secreta.lower()
    palavra_mask = list('_'*len(palavra_secreta))
    print(f'Você tem {num_tentativas} tentativas')
    print(f"Palavra secreta: {palavra_mask}")
    letras_utilizadas = []
    while True:
        letra_escolhida = input("Digite uma letra: ")
        if (letra_escolhida == palavra_secreta) and len(letras_utilizadas) < len(palavra_secreta)/2:
            pontuacao += 999
            print(f"JACKPOT! você agora tem {pontuacao} pontos")
            print(f'Você descobriu a palavra: {palavra_secreta}')
            break
        letras_utilizadas.append(letra_escolhida)
        if len(letra_escolhida) > 1:
            num_tentativas -= 1
            print(f'Você tem {num_tentativas} tentativas restantes...')
            continue
        if letra_escolhida not in palavra_secreta:
            num_tentativas -= 1
            print(f'Você tem {num_tentativas} tentativas restantes...')
        for i in range(0, len(palavra_secreta)):
            if palavra_secreta[i] == letra_escolhida.lower():
                palavra_mask[i] = palavra_secreta[i]
                pontuacao += 10
        print(f'Letras utilizadas: {letras_utilizadas}')
        print(f"Palavra secreta: {palavra_mask}")
        if ''.join(palavra_mask) == palavra_secreta:
            pontuacao += 100
            print(f'Você descobriu a palavra: {palavra_secreta}')
            break
        if num_tentativas == 0:
            print('Acabaram suas tentativas')
            break

pontuacao = 0
print("Bem vindo ao jogo da Forca")
print('1 - Jogar')
print('2 - Ver Pontos')
print('3 - Sair')

while True:
    entrada = int(input("Digite o numero do oque deseja fazer: "))
    match entrada:
        case 1:
            tentativas = int(input("Digite a quantidade de tentativas: "))
            criar_forca(carregar_arquivo_lista("lista_palavras.txt"), tentativas)
        case 2:
            print(f'Você tem {pontuacao} pontos')
        case 3:
            break
        case _:
            print("Opções disponiveis: ")
            print('1 - Jogar')
            print('2 - Ver Pontos')
            print('3 - Sair')
            continue