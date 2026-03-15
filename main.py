from models.produtos import adicionar_produto, atualizar_produto , deletar_produto ,listar_produtos

def menu():
  while True:
    print("""
=== \033[1;32mSISTEMA DE PRODUTOS\033[0m ===
          1 - Adicionar Produto
          2 - Atualizar Produto
          3 - Listar Produtos
          4 - Deletar Produtos
          5 - Sair
          """)
    
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
      nome = input("Nome: ")
      preço = float(input("Preço: "))
      estoque = int(input("Estoque: "))
      adicionar_produto(nome, preço, estoque)

    elif opcao == "2":
      id = int(input("ID do produto a ser atualizado: "))
      nome = input("Novo nome: ")
      preço = float(input("Novo preço: "))
      estoque = int(input("Novo estoque: "))
      atualizar_produto(id, nome, preço, estoque)

    elif opcao == "3":
      listar_produtos()

    elif opcao == "4":
      id = int(input("ID do produto a ser deletado: "))
      deletar_produto(id)

    elif opcao == "5":
      print("Saindo do sistema...")
      break

    else:
      print("\033[31mOpção inválida.\033[0m")
menu()