from Usuario.menuUsuario import menu_usuarios  
def main():
    while True:
        print("1-CRUD Usuário")
        print("2-CRUD Vendedor")
        print("3-CRUD Produto")
        print("4-CRUD Favoritos")
        print("S-Sair")
        
        key = input("Digite a opção desejada: ")

        if key == '1':
            menu_usuarios()  
        elif key == '2':
            print("Menu do Vendedor")        
            
        elif key == '3':
            print("Menu do Produto")        
           
        elif key == '4':
            print("Menu de Favoritos")
           
        elif key.upper() == 'S':
            print("Tchau Prof...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
