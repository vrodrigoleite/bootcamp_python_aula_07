import csv



def ler_csv(nome_arquivo: str) -> list[dict]:

    """A função lê um arquivo csv e retorna uma lista de dicionários."""

    dados = []

    with open(nome_arquivo, mode='r', encoding= 'utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            dados.append(linha)

    return dados

def filtrar_produtos_nao_entregues(lista: list[dict]) -> list[dict]:
    
    """Função que filtra produtos não entregues ao cliente"""

    lista_produtos_filtrados = []

    for produto in lista:
        if produto.get('entrega') == 'False':
            lista_produtos_filtrados.append(produto)

    return lista_produtos_filtrados

def somar_valores_produtos(lista: list[dict]) -> int:
    
    """Soma os valores de todos os produtos que não foram entregues."""

    total = 0

    for produto in lista:
        if produto.get('entrega') == 'False':
            total += int(produto.get('price', 0))

    return total
