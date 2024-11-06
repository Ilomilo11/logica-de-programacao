#Bar Paraiso do Zé

#preenchimento de estoque
estoque = [10, 20, 15, 50, 20]

#função de venda
def atualizar(produto, tipo, quantidade):
    if tipo == "adicionar":
        
        estoque.append(quantidade)
    elif 0 <= produto < len(estoque):
        if tipo == "vender":
            if estoque[produto] >= quantidade:
                estoque[produto] -= quantidade
                print(f"Foram vendidos: {quantidade} unidades do produto {produto}")
            else:
                print("Produto em falta no estoque")
        elif tipo == "repor":
            estoque[produto] += quantidade
            print(f"foram adicionadas {quantidade} unidades do produto {produto}")


def main():
    tipo = input("O que deseja fazer?: ")
    if tipo == "adicionar":
        tipo = input("O que deseja fazer?: ")
        quantidade = int(input("Qual a quantidade?: "))
        atualizar(produto, tipo, quantidade)
        print("estoque atual")
        print(estoque)

    else:
        produto = int(input("Qual é o produto?: "))
        quantidade = int(input("Qual a quantidade?: "))
        atualizar(produto, tipo, quantidade)
        print("estoque atual")
        print(estoque)

while True:
    main()