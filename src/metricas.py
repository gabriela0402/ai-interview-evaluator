import re
import numpy as np


def extrair_nota(texto, criterio):
    """
    Extrai uma nota de 1 a 5 de um texto.

    Exemplo esperado:
        Relevância: 4
    """

    padrao = rf"{criterio}\s*:\s*([1-5](?:[.,]\d+)?)"
    resultado = re.search(
        padrao,
        texto,
        flags=re.IGNORECASE
    )

    if resultado:
        valor = resultado.group(1).replace(",", ".")
        return float(valor)

    return np.nan


def extrair_avaliacao(texto):
    """
    Extrai as notas dos critérios de uma avaliação textual.
    """

    return {
        "nota_relevancia": extrair_nota(
            texto,
            "Relevância"
        ),
        "nota_especificidade": extrair_nota(
            texto,
            "Especificidade"
        ),
        "nota_comunicacao": extrair_nota(
            texto,
            "Comunicação"
        ),
        "nota_reflexao": extrair_nota(
            texto,
            "Reflexão"
        ),
        "nota_resultado": extrair_nota(
            texto,
            "Resultado"
        ),
        "nota_geral": extrair_nota(
            texto,
            "Nota geral"
        )
    }
