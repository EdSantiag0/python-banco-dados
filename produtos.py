from banco import conectar

def adicionar_produto(nome, preco, estoque):
  conexao = conectar()
  cursor = conexao.cursor()

  cursor.execute("""
    INSERT INTO produtos (nome, preco, estoque) VALUES (?, ?, ?)
  """, (nome, preco, estoque))

  conexao.commit()
  cursor.close()
  conexao.close()
  

def listar_produtos():
  conexao = conectar()
  cursor = conexao.cursor()

  cursor.execute(" SELECT * FROM produtos")

  produtos = cursor.fetchall()

  for produto in produtos:
      print(produto)

  cursor.close()
  conexao.close()