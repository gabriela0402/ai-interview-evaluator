# Relatório do experimento de saída estruturada

## Objetivo

Investigar se o modelo consegue retornar avaliações de entrevistas em formato JSON estruturado.

## Resultados

- Respostas processadas: 9
- Respostas avaliadas com sucesso: 8
- Respostas com erro: 1
- Média da nota geral: 2.38
- Desvio padrão da nota geral: 1.30
- Erro médio absoluto: 0.88

## Formato estruturado

As avaliações bem-sucedidas foram retornadas em JSON, permitindo armazenar as notas diretamente em colunas numéricas, sem depender de extração por expressões regulares.

## Limitações

- O dataset é pequeno e sintético.
- Algumas respostas retornaram JSON inválido ou incompleto.
- Uma resposta apresentou erro de autenticação HTTP 401.
- A amostra final foi menor que o dataset original.
- Os resultados são exploratórios.
- A IA não deve ser usada sozinha em decisões reais de contratação.

## Conclusão

A saída estruturada facilita a organização e a análise das avaliações, mas ainda é necessário tratar respostas inválidas e erros da API.

## Próximos passos

- Melhorar o tratamento de JSON inválido.
- Testar o formato estruturado em mais respostas.
- Comparar modelos diferentes.
- Investigar possíveis vieses.