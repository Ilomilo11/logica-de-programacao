import math

def raiz(value):
    return math.sqrt(value)



def main():
    a = int(input("Insira o valor de a: "))
    b = int(input("Insira o valor de b: "))
    c = int(input("Insira o valor de b: "))

    delta = b**2 - 4 * a * c

    if delta < 0:
        print("Não é possivel calcular a raiz")

    elif delta == 0:
        x = -b / (2*a)
        print("a raiz possue um valor unico", x)

    else:
        x1 = ((-b + raiz(delta))/(2*a))
        x2 = ((-b - raiz(delta))/(2*a))
        print("As raizes da equação são: ", x1, " e ", x2)

main()