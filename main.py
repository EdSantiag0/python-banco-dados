from databse.criar_tabelas import criar_tabela_produtos
from models.produtos import adicionar_produto, atualizar_produto , deletar_produto ,listar_produtos

criar_tabela_produtos()

adicionar_produto("Spinner", 10.00 , 8)

listar_produtos()