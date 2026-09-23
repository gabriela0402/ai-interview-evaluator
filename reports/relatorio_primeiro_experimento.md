
# Relatório do primeiro experimento

## Objetivo

Avaliar respostas de entrevistas comportamentais utilizando um modelo de linguagem
e comparar suas avaliações com uma referência criada manualmente.

## Dataset

Foram utilizadas 9 respostas sintéticas, distribuídas entre
resolução de problemas, trabalho em equipe e organização.

## Resultados do processamento

- Respostas processadas: 9
- Respostas avaliadas com sucesso: 7
- Respostas não avaliadas: 2
- Erro médio absoluto inicial: 1.14
- Diferença média inicial: -1.14

## Comparação com a avaliação de referência

A comparação foi feita usando as 7 respostas que possuíam
avaliação da IA e avaliação de referência.

- Correlação de Spearman: 0.99
- Erro médio absoluto entre IA e referência: 1.03
- Diferença média entre IA e referência: -1.03

A correlação de Spearman foi utilizada porque as notas estão em uma escala ordinal
de 1 a 5. Ela indica se a IA tende a ordenar as respostas de forma semelhante à
referência, mas não significa que as notas sejam exatamente iguais.

## Limitação da API

Duas respostas não puderam ser avaliadas porque os créditos gratuitos da
Hugging Face foram esgotados durante o processamento. A API retornou o erro HTTP 402.

Por isso, os resultados são parciais e devem ser interpretados apenas como uma
análise exploratória.

## Limitações metodológicas

- O dataset é pequeno e sintético.
- A avaliação de referência foi criada para este experimento e não representa um consenso amplo de avaliadores.
- Apenas um modelo foi utilizado.
- A amostra possui somente 7 respostas comparáveis.
- Os resultados não devem ser usados para decisões reais de contratação.
- A IA pode ser influenciada pelo prompt, pelo modelo e pelo formato da resposta.

## Próximos passos

- Limpar e organizar o notebook atual.
- Criar uma função para processar novas respostas sem duplicar código.
- Melhorar a saída estruturada das avaliações.
- Investigar consistência e possíveis vieses.
- Testar um modelo local ou outra cota gratuita.
