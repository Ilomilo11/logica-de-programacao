#reservar cadeira de cinema

def reservar(sala, fileira, assento, tipo):
    if tipo == "reservar":
        if sala[fileira-1][assento-1] == 0:
            sala[fileira-1][assento-1] = 1
            print(f"Você reservou um lugar na sala, fileira {fileira}, assento {assento}")

    else:
        print("esse lugar já está reservado")

def cancelar_reserva(sala, fileira, assento, tipo):
        if tipo == "cancelar":
            if sala[fileira-1][assento-1] == 1:
                sala[fileira-1][assento-1] = 0
                print("A reserva foi cancelada")
            else:
                print("Reserva mantida")

def exibir_sala(sala):
    for fila in sala:
        print(" ".join(map(str, fila)))


sala = [[0] * 8 for fila in range(5)]

def main():
    tipo = input("O que deseja fazer: ")
    if tipo == "reservar":
        
        fileira = int(input("Qual a fileira: "))
        poltrona = int(input("Qual o assento: "))
        reservar(sala, fileira, poltrona)
        print("MAPA DA SALA: ")
        exibir_sala(sala)
    if tipo == "cancelar":
        fileira = int(input("Qual a fileira: "))
        poltrona = int(input("Qual o assento: "))
        reservar(sala, fileira, poltrona)
        print("MAPA DA SALA: ")
        exibir_sala(sala)

while True:
    main()