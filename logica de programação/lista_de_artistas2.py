artistas = ["Billie Eilish", "Lana Del Rey", "Melanie Martinez", "Taylor Swift"]


def novo_artista(novo): #cria uma função
    artistas.append(novo) #coloca no final da lista um valor
    print("\n O Artista: ",novo," foi inserido na lista.") #imprime o que foi inserido
    print("\n A lista nova ficou assim:",artistas) #imprime a lista completa
    
    
def sub_artista(antigo, novo): #recebe os parametros de artista antigo e novo
    indice = artistas.index(antigo) #busca o valor do antigo artista antigo na lista e devolvo a sua posição
    artistas[indice] = novo #substituo o valor do antigo artista pelo novo
    print("\n O Artista: ",antigo," foi substituido pelo novo artista,",novo) #imprimo o antigo e o novo
    print("\n A nova lista é: ",artistas)
    
def lista_atual():    
    print("\n A nova lista é: ",artistas)
    
def contagem():
    cont = len(artistas)
    print("\n O número de artistas em sua lista é de: ", cont)

def remover(nome):
    artistas.remove(nome)
    print("\n O artista", nome, "foi removido")

def sair():
    exit

    
print("------- SISTEMA DE AGENDAMENTO DE SHOWS! ----------")
while True:
    print("MENU:")
    print("1.INSERIR NOVO ARTISTAS NA LISTA")
    print("2.SUBSTITUIR ARTISTA DA LISTA")
    print("3.LISTA ATUAL")
    print("4.QUANTIDADE")
    print("5.REMOVER")
    print("6.SAIR")
    
    
    menu = int(input("O que você deseja fazer?"))
    
    if menu == 1:
        #insere o novo artista no final da lista 
        novo = input("Insira o nome do novo artista: ")
        novo_artista(novo)
        
    elif menu == 2:
        antigo = input("Insira o nome do artista que será removido: ")
        novo = input("Insira o nome do artista que será o inserido no lugar: ")
        #subistitui o nome do novo artista
        sub_artista(antigo,novo)
            
    elif menu == 3:
        lista_atual()
    
    elif menu == 4:
        contagem()

    elif menu == 5:
        nome = input("Qual artista deseja remover: ")
        remover(nome)

    elif menu == 6:
        sair()
        
    else:
        print("O código não é válido!")