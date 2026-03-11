from banco import conectar

# Adicionar Produto
def adicionar_produto(nome, preco, estoque):
  conexao = conectar()
  cursor = conexao.cursor()

  cursor.execute("""
    INSERT INTO produtos (nome, preco, estoque) VALUES (?, ?, ?)
  """, (nome, preco, estoque))

  conexao.commit()
  cursor.close()
  conexao.close()
  
# Atualizar Produto
def atualizar_produto(id, nome, preco, estoque):
  conexao = conectar()
  cursor = conexao.cursor()

  cursor.execute("""
    UPDATE produtos SET nome = ?, preco = ?, estoque = ? WHERE id = ?
  """, (nome, preco, estoque, id))

  conexao.commit()
  cursor.close()
  conexao.close()

#Deletar Produto
def deletar_produto(id):
  conexao = conectar()
  cursor = conexao.cursor()

  cursor.execute("""
    DELETE FROM produtos WHERE id = ?
  """, (id,))

  conexao.commit()
  cursor.close()
  conexao.close()

# Listar Produtos
def listar_produtos():
  conexao = conectar()
  cursor = conexao.cursor()

  cursor.execute(" SELECT * FROM produtos")

  produtos = cursor.fetchall()

  for produto in produtos:
      print(produto)

  cursor.close()
  conexao.close()