from banco import conectar

def criar_tabela_produtos():

  conexao = conectar()
  cursor = conexao.cursor()

  cursor.execute("""
     CREATE TABLE IF NOT EXISTS produtos (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 nome TEXT NOT NULL,
                 preco REAL NOT NULL,
                 estoque INTEGER NOT NULL  
    )                            
""")
  
  conexao.commit()

  cursor.close()
  conexao.close()