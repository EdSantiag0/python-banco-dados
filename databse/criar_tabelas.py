from binascii import Error

from databse.conexao import conectar

def criar_tabela_produtos():

  conexao = conectar()
  cursor = conexao.cursor()

  try:  

    cursor.execute("""
      CREATE TABLE IF NOT EXISTS produtos (
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  nome TEXT NOT NULL,
                  preco REAL NOT NULL,
                  estoque INTEGER NOT NULL  
      )                            
    """)
    conexao.commit()
    print("Tabela 'produtos' criada com sucesso!")
  except Error as e:
    print(f"Erro ao criar tabela: {e}")
  finally: 
    cursor.close()
    conexao.close()