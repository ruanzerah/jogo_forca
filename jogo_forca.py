import random

print("Bem vindo ao jogo da Forca")

palavras_secretas = ["Turismo", "Programacao", "Rodovia"]

def criar_forca(lista_secreta, tentativas):
    palavra_secreta = random.choice(lista_secreta)
    palavra_secreta = palavra_secreta.lower()
    palavra_mask = list('_'*len(palavra_secreta))
    print(f'Você tem {tentativas} tentativas')
    print(f"Palavra secreta: {palavra_mask}")
    letras_utilizadas = []
    while True:
        letra_escolhida = input("Digite uma letra: ")
        letras_utilizadas.append(letra_escolhida)
        if letra_escolhida == palavra_secreta:
            print(f'Você descobriu a palavra: {palavra_secreta}')
            break
        if len(letra_escolhida) > 1:
            tentativas -= 1
            print(f'Você tem {tentativas} tentativas restantes...')
            continue
        if letra_escolhida not in palavra_secreta:
            tentativas -= 1
            print(f'Você tem {tentativas} tentativas restantes...')
        for i in range(0, len(palavra_secreta)):
            if palavra_secreta[i] == letra_escolhida.lower():
                palavra_mask[i] = palavra_secreta[i]
        print(f'Letras utilizadas: {letras_utilizadas}')
        print(f"Palavra secreta: {palavra_mask}")
        if ''.join(palavra_mask) == palavra_secreta:
            print(f'Você descobriu a palavra: {palavra_secreta}')
            break
        if tentativas == 0:
            print('Acabaram suas tentativas')
            break

criar_forca(palavras_secretas,3)