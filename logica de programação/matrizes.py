def bingo(matriz):
    cont = 0
    for linha in matriz:
        for valor in linha:
            if valor >= 10:
                cont += 1
                if cont == 25:
                    print("BINGO!!!")

    return cont
matriz = [[5,12,15,20,],
              [15,12,22,16],
              [34,11,16,14,],
              [13,288,3,25],
              [34,11,16,14]]

resultado = bingo(matriz)
print(f"A quantidade de numero é: {resultado}")