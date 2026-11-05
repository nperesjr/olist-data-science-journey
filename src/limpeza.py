from pathlib import Path
import pandas as pd


def carregar_tabelas(pasta="../data"):
    """Carrega os 9 CSVs da Olist num dicionário, com nomes curtos."""
    tabelas = {}
    for arquivo in sorted(Path(pasta).glob("*.csv")):
        nome = (
            arquivo.stem.replace("olist_", "")
            .replace("_dataset", "")
            .replace("product_category_name_translation", "category_translation")
        )
        tabelas[nome] = pd.read_csv(arquivo)
    return tabelas

def preencher_categoria(produtos):
    """Preenche a categoria vazia com 'sem_categoria'."""
    produtos = produtos.copy()
    produtos["product_category_name"] = produtos["product_category_name"].fillna("sem_categoria")
    return produtos

def remover_duplicadas(tabela):
    """Remove linhas que são cópia exata de outra."""
    return tabela.drop_duplicates()