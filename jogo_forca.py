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
        if (letra_escolhida == palavra_secreta) and len(letras_utilizadas) < len(palavra_secreta)//2:
            pontuacao += 999
            print(f"JACKPOT! você agora tem {pontuacao} pontos")
            print(f'Você descobriu a palavra: {palavra_secreta}')
            break
        elif len(letras_utilizadas) >= len(palavra_secreta)//2 and len(letra_escolhida) > 1:
            print(f'Você não pode mais chutar a palavra...')
        if letra_escolhida in letras_utilizadas:
            print(f'A letra {letra_escolhida} já foi utilizada.')
            continue
        if len(letra_escolhida) > 1:
            num_tentativas -= 1
            if num_tentativas <= 0:
                print('Acabaram suas tentativas')
                print(f'A palavra era {palavra_secreta}')
                break
            print(f'Você tem {num_tentativas} tentativas restantes...')
            continue
        else:
            letras_utilizadas.append(letra_escolhida)
        if letra_escolhida not in palavra_secreta:
            num_tentativas -= 1
            if num_tentativas <= 0:
                print('Acabaram suas tentativas')
                print(f'A palavra era {palavra_secreta}')
                break
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
def carregar_jogo_existente(arquivo):
    try:
        with open(f'{arquivo}.txt', "rt") as a:
            dados = a.read().splitlines()
    except FileNotFoundError:
        print("Arquivo nao encontrado")
    else:
        dado = ''.join(dados).split(':')
        n = dado[0]
        p = int(dado[1])
        return n, p
    finally:
        a.close()
def salvar_jogo(nome, pontos):
    try:
        with open(f'{str(nome).lower()}.txt', "wt+") as a:
            a.write(f'{nome_jogador}:{pontos}\n')
    except FileNotFoundError:
        print("Arquivo nao encontrado")
    finally:
        a.close()
def arquivo_existe(arquivo):
    try:
        with open(f'{arquivo}.txt') as a:
            a.close()
            return True
    except FileNotFoundError:
        return False
def mostrar_menu():
    print("Bem vindo ao jogo da Forca")
    print('1 - Jogar')
    print('2 - Ver Pontos')
    print('3 - Sair')
    print('4 - Carregar Jogo')
pontuacao = 0
nome_jogador = None

mostrar_menu()
while True:
    entrada = int(input("Digite o numero do oque deseja fazer: "))
    match entrada:
        case 1:
            if nome_jogador:
                tentativas = int(input("Digite a quantidade de tentativas: "))
                criar_forca(carregar_arquivo_lista("lista_palavras.txt"), tentativas)
            else:
                nome_jogador = input("Digite o nome do jogador: ")
                tentativas = int(input("Digite a quantidade de tentativas: "))
                criar_forca(carregar_arquivo_lista("lista_palavras.txt"), tentativas)
        case 2:
            print(f'Você tem {pontuacao} pontos')
        case 3:
            print("Salvando o jogo...")
            salvar_jogo(nome_jogador, pontuacao)
            break
        case 4:
            nome_jogador = input("Digite o nome do jogador: ")
            if nome_jogador and arquivo_existe(nome_jogador):
                print(f"Arquivo de save encontrado para o jogador: {nome_jogador}")
                _, pontuacao = carregar_jogo_existente(nome_jogador)
            else:
                print(f"Arquivo de save não encontrado para o jogador: {nome_jogador}")
        case _:
            mostrar_menu()
            continue