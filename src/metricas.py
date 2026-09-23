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

def adicionar_nota_geral_manual(
    comparacao,
    colunas_manuais
):
    """
    Calcula a média das notas manuais dos critérios.
    """

    comparacao = comparacao.copy()

    comparacao["nota_geral_manual"] = (
        comparacao[colunas_manuais]
        .mean(axis=1)
    )

    return comparacao


def adicionar_diferencas(
    comparacao,
    coluna_ia="nota_geral",
    coluna_referencia="nota_geral_manual"
):
    """
    Calcula a diferença entre as notas da IA e da referência.
    """

    comparacao = comparacao.copy()

    comparacao["diferenca_ia_referencia"] = (
        comparacao[coluna_ia]
        - comparacao[coluna_referencia]
    )

    comparacao["erro_absoluto"] = (
        comparacao["diferenca_ia_referencia"].abs()
    )

    return comparacao


def calcular_correlacao_spearman(
    comparacao,
    coluna_ia="nota_geral",
    coluna_referencia="nota_geral_manual"
):
    """
    Calcula a correlação de Spearman entre IA e referência.
    """

    dados = comparacao[
        [coluna_ia, coluna_referencia]
    ].dropna()

    return dados[coluna_ia].corr(
        dados[coluna_referencia],
        method="spearman"
    )

