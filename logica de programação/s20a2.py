while True:
    print("Menu: ")
    print("1. soma")
    print("2. multiplicação")
    print("3. subtração")
    print("4. sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        a = float(input("insira: "))
        b = float(input("insira: "))
        soma = a + b
        print(soma)
        pass

    elif escolha == "2":
        a = float(input("insira: "))
        b = float(input("insira: "))
        multiplicacao = a * b
        print(multiplicacao)
        pass

    elif escolha == "3":
        a = float(input("insira: "))
        b = float(input("insira: "))
        subtracao = a - b
        print(subtracao)
        pass

    elif escolha == "4":
        break

    else:
        print("Opção invalida. Tente novamente.")