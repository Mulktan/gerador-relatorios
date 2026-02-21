"""
Módulo responsável por gerar o HTML do relatório usando Jinja2.

Google Style Docstring em Português.
"""

from typing import List
from jinja2 import Environment, FileSystemLoader

# Função para renderizar o relatório HTML

def gerar_html(titulo: str, colunas: List[str], linhas: List[List[str]], total_registros: int, caminho_template: str, caminho_saida: str) -> None:
    """Gera um arquivo HTML de relatório a partir dos dados fornecidos.

    Args:
        titulo (str): Título do relatório.
        colunas (List[str]): Lista de nomes das colunas.
        linhas (List[List[str]]): Lista de linhas (cada linha é uma lista de valores).
        total_registros (int): Total de registros.
        caminho_template (str): Caminho do template HTML.
        caminho_saida (str): Caminho para salvar o HTML gerado.

    Raises:
        FileNotFoundError: Se o template não for encontrado.
        Exception: Para outros erros de renderização.
    """
    try:
        # Configura o ambiente Jinja2
        env = Environment(loader=FileSystemLoader(caminho_template.rsplit('/', 1)[0]))
        template = env.get_template(caminho_template.rsplit('/', 1)[1])
        # Renderiza o HTML
        html = template.render(
            titulo=titulo,
            colunas=colunas,
            linhas=linhas,
            total_registros=total_registros
        )
        # Salva o arquivo
        with open(caminho_saida, 'w', encoding='utf-8') as f:
            f.write(html)
    except FileNotFoundError as e:
        # Template não encontrado
        print(f"Erro: Template não encontrado - {e}")
        raise
    except Exception as e:
        # Outros erros
        print(f"Erro ao gerar HTML: {e}")
        raise
