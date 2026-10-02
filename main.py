from livros import cadastrar_livro, listar_livros, excluir_livros



while True:
    print("\n===== BIBLIOTECA =====")
    print("1 - Cadastrar livro")
    print("2 - Listar livros")
    print("3 - Excluir livro")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_livro()

    elif opcao == "2":
        listar_livros()

    elif opcao == "3":
        excluir_livros()

    elif opcao == "4":
        print("Saindo...")
        break

    else:
        print("Opção inválida!" ) 