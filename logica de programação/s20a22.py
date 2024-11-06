def mostrar_menu (): 
    print("Menu:") 
    print("1. Opção A") 
    print("2. Opção B") 
    print("3. Sair")
def processar_escolha(escolha): 
    if escolha == "1": 
        return True 
    
    elif escolha == "2":
        return True 
    
    elif escolha == "3":
        return False
    else:
        print("Opção inválida. Tente novamente.")
        return True 
def executar_menu(): 
    continuar = True 
    while continuar: 
        mostrar_menu() 
        escolha = input("Escolha uma opção: ") 
        continuar = processar_escolha(escolha)
executar_menu()