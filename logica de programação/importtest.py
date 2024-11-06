import math
import statistics
import random

def raizQuadrada(value):
    return math.sqrt(value)

def fatorial(value):
    return math.factorial(value)

def potencia(value):
    return math.pow(value, 10)

def main():
    numero = random.randint(0, 100)
    print("O numero sorteado foi: ", numero)
    print("A Raiz desse numero é: ", raizQuadrada(numero))
    print("O Fatorial desse numero é: ", fatorial(numero))
    print("A potencia (10) do numero é: ", potencia(numero))

main()