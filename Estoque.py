estoque = []
while True:
    print("\n1) Cadastrar, 2) Mostrar, 3) Alterar, 0) Sair")
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
        print("----- Cadastro de Produto -----")
        produto = Produto()
        produto.cadastrar_produto()
        estoque.append(produto)
    elif opcao == 2:
        #Explorar o conteúdo do estoque
        print("----- Dados Recuperados -----")
        for id,produto in enumerate(estoque):
            print(f"----> Produto {id}")
            produto.mostrar_dados()
    elif opcao == 3:
        #Alteração pelo ID
        for id, produto in enumerate(estoque):  #Mostra todos os produtos
            print(f"----> Produto {id}: {produto.descricao}")
        id = int(input("Digite o ID do produto a ser modificado: "))
        produto = estoque[id]
        produto.atualizar_dados()
    elif opcao == 0:
        print("Programa finalizado!")
        break
    else:
        print("Opção inválida!")