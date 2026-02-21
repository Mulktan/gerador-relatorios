"""
Módulo para leitura e processamento de arquivos CSV e Excel.

Google Style Docstring em Português.
"""

from typing import Tuple, List
import pandas as pd
from pandas.errors import EmptyDataError, ParserError

# Função para ler arquivo CSV ou Excel

def ler_arquivo(caminho: str) -> Tuple[List[str], List[List[str]]]:
    """Lê um arquivo CSV ou Excel e retorna colunas e linhas.

    Args:
        caminho (str): Caminho do arquivo CSV ou Excel.

    Returns:
        Tuple[List[str], List[List[str]]]: Lista de colunas e lista de linhas.

    Raises:
        FileNotFoundError: Se o arquivo não for encontrado.
        ValueError: Se o arquivo não for CSV ou Excel.
        Exception: Para outros erros de leitura.
    """
    try:
        if caminho.lower().endswith('.csv'):
            df = pd.read_csv(caminho)
        elif caminho.lower().endswith('.xlsx'):
            df = pd.read_excel(caminho, engine='openpyxl')
        else:
            raise ValueError('Arquivo deve ser CSV ou Excel (.xlsx)')
        colunas = df.columns.tolist()
        linhas = df.values.tolist()
        return colunas, linhas
    except FileNotFoundError as e:
        print(f"Arquivo não encontrado: {e}")
        raise
    except (EmptyDataError, ParserError) as e:
        print(f"Erro ao ler arquivo: {e}")
        raise
    except Exception as e:
        print(f"Erro inesperado: {e}")
        raise
