from etl import ler_csv, filtrar_produtos_nao_entregues, somar_valores_produtos

path_arquivo = 'vendas.csv'

produtos = ler_csv(path_arquivo)

produtos_nao_entregues = filtrar_produtos_nao_entregues(produtos)

valor_total = somar_valores_produtos(produtos_nao_entregues)

print(valor_total)