from databse.conexao import conectar

# Adicionar Produto
def adicionar_produto(nome, preco, estoque):
  conexao = conectar()
  cursor = conexao.cursor()

  try:

    cursor.execute("""
      INSERT INTO produtos (nome, preco, estoque) VALUES (?, ?, ?)
    """, (nome, preco, estoque))
    
    conexao.commit()
    print("Produto adicionado com sucesso!")
  except Exception as e:
    print(f"Erro ao adicionar produto: {e}")
  finally:
    cursor.close()
    conexao.close()
  
# Atualizar Produto
def atualizar_produto(id, nome, preco, estoque):
  conexao = conectar()
  cursor = conexao.cursor()

  try:
    cursor.execute("""
      UPDATE produtos SET nome = ?, preco = ?, estoque = ? WHERE id = ?
    """, (nome, preco, estoque, id))

    if cursor.rowcount > 0:
      conexao.commit()
      print("Produto atualizado com sucesso!")
    else:
      print(f"Produto com ID {id} não encontrado.")
    
  except Exception as e:
    print(f"Erro ao atualizar produto: {e}")
  finally:
    cursor.close()
    conexao.close()

# Deletar Produto
def deletar_produto(id):
  conexao = conectar()
  cursor = conexao.cursor()

  try:
    cursor.execute("""
      DELETE FROM produtos WHERE id = ?
    """, (id,))

    if cursor.rowcount > 0:
        conexao.commit()
        print("Produto deletado com sucesso!")
    else:
        print(f"Produto com ID {id} não encontrado.")

  except Exception as e:
    print(f"Erro ao deletar produto: {e}")
  finally:

    cursor.close()
    conexao.close()

# Listar Produtos
def listar_produtos():
  conexao = conectar()
  cursor = conexao.cursor()

  try:
    cursor.execute("SELECT id, nome, preco, estoque FROM produtos")
    produtos = cursor.fetchall()

    for produto in produtos:
      print(f"ID: {produto[0]} | Nome: {produto[1]} | Preço: {produto[2]} | Estoque: {produto[3]}")  

    return produtos
  
  except Exception as e:
    print(f"Erro ao listar produtos: {e}")
  finally:
    cursor.close()
    conexao.close()