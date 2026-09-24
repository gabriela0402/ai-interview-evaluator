# Relatório do experimento de consistência

## Objetivo

Investigar se o modelo de linguagem produz avaliações semelhantes quando recebe a mesma pergunta, competência e resposta mais de uma vez.

## Configuração

- Modelo utilizado: openai/gpt-oss-20b
- Resposta analisada: resp_001
- Quantidade de repetições: 3
- Temperatura: 0

## Resultados da nota geral

- Média da nota geral: 3.40
- Desvio padrão: 0.00
- Menor nota: 3.40
- Maior nota: 3.40

## Variação por critério

```text
                     mean  std  min  max
nota_relevancia       5.0  0.0  5.0  5.0
nota_especificidade   3.0  0.0  3.0  3.0
nota_comunicacao      4.0  0.0  4.0  4.0
nota_reflexao         2.0  0.0  2.0  2.0
nota_resultado        3.0  0.0  3.0  3.0
nota_geral            3.4  0.0  3.4  3.4
```

## Interpretação

O desvio padrão indica quanto as notas variaram entre as repetições.

Um desvio padrão próximo de zero indica que o modelo produziu notas muito semelhantes. Valores maiores indicam maior variação.

A análise é exploratória, pois utiliza uma única resposta e poucas repetições.

## Limitações

- Apenas uma resposta foi analisada.
- Foram realizadas somente 3 repetições.
- O modelo pode apresentar variações em outras respostas.
- A cota gratuita limita a quantidade de execuções.
- O resultado não permite afirmar que o modelo seja consistente em geral.
- A avaliação não deve ser usada sozinha em decisões reais de contratação.

## Próximos passos

- Repetir o experimento com mais respostas.
- Comparar a consistência entre diferentes modelos.
- Avaliar quais critérios apresentam maior variação.