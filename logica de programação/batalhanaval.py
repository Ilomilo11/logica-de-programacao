tabuleiro = [['~'] * 10 for i in range(10)]

def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro :
        print(" ".join(linha))
    print()

def posicionar_navio(tabuleiro, linha_inicial, coluna_inicial, tamanho, orientacao):
    if orientacao == 'horizontal':
        for i in range(tamanho):
            tabuleiro[linha_inicial][coluna_inicial * i] = '#'
    elif orientacao == 'vertical':
        for i in range(tamanho):
            tabuleiro[linha_inicial * i][coluna_inicial] = '#'

def dar_tiro(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == '#':
        tabuleiro[linha][coluna] = 'X'
        print("Que tiro foi esse?!")
        return True
    elif tabuleiro[linha][coluna] == '~':
        tabuleiro[linha][coluna] = 'O'
        print("Errou seu merda!!")
        return False
    else:
        print("voce ja atirou aqui")

def jogo():
    tamanho = 10
    tabuleiro_jogador1 = [['~'] * tamanho for _ in range(tamanho)]
    tabuleiro_jogador2 = [['~'] * tamanho for _ in range(tamanho)]

    posicionar_navio(tabuleiro_jogador1, 1, 4, 3, 'vertical')
    posicionar_navio(tabuleiro_jogador2, 3, 2, 6, 'horizontal')

    while True:
        print("Jogador 1 atirando:")
        imprimir_tabuleiro(tabuleiro_jogador2)

        x = int(input("Jogador 1 escolha a linha de tiro (0,9): "))
        y = int(input("Jogador 1 escolha a coluna de tiro (0,9): "))
        dar_tiro(tabuleiro_jogador2,x,y)

        if all(cell !='#' for row in tabuleiro_jogador2 for cell in row):
            print("Jogador 1 ganhou!")
            break

        print("Jogador 2 atirando:")
        imprimir_tabuleiro(tabuleiro_jogador1)

        x = int(input("Jogador 2 escolha a linha de tiro (0,9): "))
        y = int(input("Jogador 2 escolha a coluna de tiro (0,9): "))
        dar_tiro(tabuleiro_jogador1,x,y)

        if all(cell !='#' for row in tabuleiro_jogador1 for cell in row):
            print("Jogador 2 ganhou!")
            break