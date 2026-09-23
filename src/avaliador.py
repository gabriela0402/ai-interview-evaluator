def avaliar_resposta(linha, cliente, modelo):
    """
    Avalia uma resposta de entrevista usando um modelo de linguagem.

    Parameters
    ----------
    linha : pandas.Series
        Linha do dataset contendo pergunta, competência e resposta.
    cliente : OpenAI
        Cliente configurado para acessar o modelo.
    modelo : str
        Nome do modelo utilizado.

    Returns
    -------
    str
        Avaliação textual gerada pelo modelo.
    """

    prompt = f"""
Você é um avaliador auxiliar de entrevistas de emprego.

Avalie a resposta abaixo usando uma escala de 1 a 5 para cada critério.

Critérios:

1. relevancia: a resposta responde diretamente à pergunta?
2. especificidade: apresenta detalhes concretos e evidências?
3. comunicacao: é clara, organizada e compreensível?
4. reflexao: demonstra aprendizado ou análise da situação?
5. resultado: explica as consequências ou resultados das ações?

Não avalie aparência, nome, idade, gênero, origem ou qualquer característica pessoal.
Avalie somente o conteúdo da resposta.

Pergunta:
{linha["pergunta"]}

Competência avaliada:
{linha["competencia"]}

Resposta do candidato:
{linha["resposta"]}

Responda em português usando este formato:

Relevância: [nota de 1 a 5]
Especificidade: [nota de 1 a 5]
Comunicação: [nota de 1 a 5]
Reflexão: [nota de 1 a 5]
Resultado: [nota de 1 a 5]
Nota geral: [média aproximada]
Pontos fortes: [lista breve]
Pontos a melhorar: [lista breve]
Justificativa: [explicação breve]
"""

    resultado = cliente.chat.completions.create(
        model=modelo,
        messages=[
            {
                "role": "system",
                "content": (
                    "Você é um avaliador objetivo e consistente. "
                    "Sua avaliação é apenas uma sugestão experimental."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0,
        max_tokens=500
    )

    return resultado.choices[0].message.content
