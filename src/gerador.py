"""
Script principal do gerador de relatórios.

Google Style Docstring em Português.
"""

import sys
from typing import Optional
from leitor_csv import ler_arquivo
from template_html import gerar_html
import os

# Função principal

def main() -> None:
    """Executa o gerador de relatórios via linha de comando.

    Uso:
        python src/gerador.py <caminho_arquivo> <titulo_relatorio>
    """
    try:
        if len(sys.argv) != 3:
            print("Uso: python src/gerador.py <caminho_arquivo> <titulo_relatorio>")
            sys.exit(1)
        caminho_arquivo = sys.argv[1]
        titulo_relatorio = sys.argv[2]
        colunas, linhas = ler_arquivo(caminho_arquivo)
        total_registros = len(linhas)
        caminho_template = os.path.join(os.path.dirname(__file__), '../templates/relatorio.html')
        caminho_saida = os.path.join(os.path.dirname(__file__), '../saida/relatorio.html')
        gerar_html(
            titulo=titulo_relatorio,
            colunas=colunas,
            linhas=linhas,
            total_registros=total_registros,
            caminho_template=caminho_template,
            caminho_saida=caminho_saida
        )
        print(f"Relatório gerado com sucesso em: {caminho_saida}")
    except Exception as e:
        print(f"Erro: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
