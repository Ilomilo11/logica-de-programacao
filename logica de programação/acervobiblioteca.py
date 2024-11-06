biblioteca = [] #vetor biblioteca

#função de adicionar livros
def add_livro(titulo, autor, genero):
    livro = {'titulo': titulo, 'autor': autor, 'genero': genero, 'disponivel': True}
    biblioteca.append(livro)
    print(f"O livro {titulo} foi adicionado com sucesso")

#função de remover um livro
def remover_livro(titulo):
    for livro in biblioteca:
        if livro['titulo'] == titulo:
            biblioteca.remove(livro)
            print(f"O livro {titulo} foi removido com sucesso!")

#remover_livro('A voz do silencio')
#print(biblioteca)

def buscar_livro(busca):
    for livro in biblioteca:
        if livro['titulo'] == busca or livro['autor'] == busca or livro['genero'] == busca:
            print("Resultados da busca:\n")
            print(f"livro: {livro['titulo']} | Autor: {livro['autor']} | Genero: {livro['genero']} - status: {livro['disponivel']}")
            return
        else:
            print("Livro não encontrado")

def listar_livro():
    if not biblioteca:
        print("Nenhum livro encontrado")
    else:
        print("Lista de livros:\n")
    for livro in biblioteca:
        if livro['disponivel'] == True:
            status = 'Disponivel'
        else:
            status = 'Indisponivel'
        
        print(f"livro: {livro['titulo']} | Autor: {livro['autor']} | Genero: {livro['genero']} - status: {status}")

def verificar_disponibilidade(titulo):
    for livro in biblioteca:
        if livro['titulo'].lower() == titulo.lower():
            if livro['disponivel']:
                print(f"Livro '{titulo}' está disponível.")
            else:
                print(f"Livro '{titulo}' está indisponível.")
            return
    print(f"Livro '{titulo}' não encontrado.")


def mostrar_menu():
    print("\n OPÇÕES DA BIBLIOTECA:")
    print("1. ADICIONAR LIVRO")
    print("2. REMOVER LIVRO")
    print("4. BUSCAR LIVRO")
    print("5. VERIFICAR DISPONIBILIDADE")
    print("6. SAIR")

while True:
    mostrar_menu()
    escolha = int(input("Escolha uma opção do menu: "))

    if escolha == 1:
        titulo = input("Digite o titulo do livro que deseja adicionar: ")
        autor = input("Digite o autor do livro que deseja adicionar: ")
        genero = input("Digite o genero do livro que deseja adicionar: ")
        add_livro(titulo, autor, genero)
    elif escolha == 2:
        titulo = input("Digite o Titulo do Livro que deseja remover: \n")
        remover_livro(titulo)
    elif escolha == 3:
        titulo = input("Digite o Titulo do Livro que deseja encontrar: \n")
        buscar_livro(titulo)
    elif escolha == 4:
        titulo = input("Listar todos os livros: \n")
        listar_livro()
    elif escolha == 5:
        titulo = input("Digite o título do livro para verificar disponibilidade:\n ")
        verificar_disponibilidade(titulo)
    elif escolha == 6:
        titulo = input("Emprestimo de livro:\n ")
        #IMPLEMENTAR ESSA FUNÇÃO
        #emprestimo_livro(titulo,autor)
    else:
        print("Fechando o Sistema...")
        break


add_livro('O terror', 'Neves', 'terror')
add_livro('O terror 2', 'Neves', 'terror')
add_livro('O terror 3', 'Neves', 'terror')
add_livro('O terror 4', 'Neves', 'terror')
listar_livro()