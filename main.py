from criar_tabelas import criar_tabela_produtos
from produtos import adicionar_produto, listar_produtos

criar_tabela_produtos()

adicionar_produto("Fone de Ouvido", 25.00, 10)
adicionar_produto("Caixa de Som", 55.00, 2)

listar_produtos()