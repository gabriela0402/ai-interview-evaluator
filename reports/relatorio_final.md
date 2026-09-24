# AI Interview Evaluator

## 1. Visão geral

Este projeto investiga o uso de modelos de linguagem para avaliar respostas
textuais de entrevistas comportamentais.

O objetivo não é substituir avaliadores humanos nem automatizar decisões de
contratação, mas analisar experimentalmente aspectos como qualidade das
avaliações, consistência, organização das respostas e possíveis diferenças entre
perfis sintéticos.

## 2. Dataset

Os experimentos utilizaram um dataset sintético com respostas relacionadas às
seguintes competências:

- resolução de problemas;
- trabalho em equipe;
- organização.

O dataset foi criado para fins educacionais e não contém respostas reais de
candidatos.

## 3. Experimento 1 — Primeira avaliação

### Objetivo

Avaliar as respostas usando uma rubrica com os critérios:

- relevância;
- especificidade;
- comunicação;
- reflexão;
- resultado.

### Resultados

Foram processadas 9 respostas. 7 foram avaliadas com sucesso e 2 não foram
processadas porque os créditos gratuitos da API foram esgotados.

As avaliações da IA foram comparadas com uma referência inicial criada
manualmente.

As métricas calculadas foram:

- erro médio absoluto;
- diferença média;
- correlação de Spearman;
- médias por competência.

### Limitações

A referência utilizada não representa um consenso entre avaliadores humanos.
Além disso, o dataset é pequeno e sintético.

### Arquivos relacionados

- [Relatório do primeiro experimento](relatorio_primeiro_experimento.md)
- [Comparação entre IA e referência](../results/tables/comparacao_ia_referencia.csv)
- [Gráfico IA versus referência](../results/figures/grafico_ia_vs_referencia.png)

## 4. Experimento 2 — Consistência

### Objetivo

Investigar se o modelo produz avaliações semelhantes quando recebe a mesma
pergunta, competência e resposta mais de uma vez.

### Resultados

A mesma resposta foi submetida ao modelo em múltiplas repetições. Foram
calculadas a média, o desvio padrão, o valor mínimo e o valor máximo das notas.

Um desvio padrão próximo de zero indica pouca variação entre as repetições.
Entretanto, o experimento utilizou apenas uma resposta e poucas execuções, não
sendo suficiente para afirmar que o modelo é consistente em geral.

### Arquivos relacionados

- [Relatório de consistência](relatorio_consistencia.md)
- [Resultados de consistência](../results/tables/resultados_consistencia.csv)
- [Resumo de consistência](../results/tables/resumo_consistencia.csv)
- [Gráfico de consistência](../results/figures/grafico_consistencia_nota_geral.png)

## 5. Experimento 3 — Saída estruturada

### Objetivo

Testar se o modelo consegue retornar as avaliações em formato JSON válido.

### Resultados

A saída estruturada permitiu armazenar diretamente as notas em colunas
numéricas, evitando a extração por expressões regulares utilizada no primeiro
experimento.

Algumas respostas, porém, retornaram JSON incompleto ou inválido. Também ocorreu
erro de autenticação em uma das chamadas. Esses casos foram registrados como
falhas e não foram incluídos nas médias das avaliações válidas.

### Conclusão parcial

O formato JSON facilita a análise automática, mas ainda exige validação,
tratamento de erros e registro da resposta bruta do modelo.

### Arquivos relacionados

- [Relatório de saída estruturada](relatorio_saida_estruturada.md)
- [Resultados finais](../results/tables/resultados_saida_estruturada_final.csv)
- [Resumo estatístico](../results/tables/resumo_estatistico_saida_estruturada.csv)
- [Resumo geral](../results/tables/resumo_geral_saida_estruturada.csv)
- [Gráfico das métricas](../results/figures/grafico_metricas_por_criterio.png)

## 6. Experimento 4 — Análise exploratória de possíveis vieses

### Objetivo

Investigar se alterações em informações pessoais fictícias podem modificar a
avaliação da mesma resposta.

A pergunta, a competência e o conteúdo da resposta foram mantidos iguais,
enquanto informações de contexto do perfil foram alteradas.

### Resultados

A diferença entre a maior e a menor nota foi calculada para cada critério.

Uma diferença observada não prova, sozinha, a existência de viés. O resultado
pode ser influenciado pelo tamanho reduzido da amostra, pelo modelo utilizado,
pelo prompt e pela quantidade de repetições.

### Limitações

Este experimento utilizou perfis sintéticos e uma amostra pequena. Portanto, os
resultados são exploratórios e não devem ser generalizados para situações reais
de recrutamento.

### Arquivos relacionados

- [Resultados da análise de viés](../results/tables/resultados_analise_vies.csv)
- [Resumo da análise de viés](../results/tables/resumo_analise_vies.csv)
- [Gráfico de variação entre perfis](../results/figures/grafico_variacao_entre_perfis.png)

## 7. Principais aprendizados

Os experimentos mostraram que:

1. modelos de linguagem podem produzir avaliações estruturadas de respostas;
2. prompts detalhados ajudam a definir critérios de avaliação;
3. a saída em JSON facilita a análise automática;
4. respostas inválidas e erros de API precisam ser tratados;
5. pequenas amostras não permitem conclusões gerais;
6. correlação não significa igualdade entre as notas;
7. possíveis diferenças entre perfis devem ser investigadas com experimentos maiores;
8. sistemas desse tipo não devem tomar decisões de contratação sozinhos.

## 8. Limitações gerais do projeto

- Dataset pequeno e sintético.
- Poucas respostas avaliadas.
- Uso de apenas um modelo principal.
- Referências manuais não validadas por um grupo amplo de avaliadores.
- Limitações de créditos e disponibilidade da API.
- Possibilidade de respostas JSON inválidas.
- Resultados exploratórios, sem validade para decisões reais.
- Ausência de uma avaliação estatística com uma amostra grande.

## 9. Próximos passos

- Expandir o dataset com dados sintéticos mais variados.
- Utilizar avaliações de múltiplas pessoas como referência.
- Comparar diferentes modelos de linguagem.
- Repetir os experimentos com mais respostas.
- Melhorar a validação de JSON.
- Criar testes automatizados para os módulos em `src/`.
- Investigar métricas específicas de justiça e equidade.
- Criar uma interface apenas para demonstração, sem decisão automática.

## 10. Conclusão

O projeto demonstrou um fluxo experimental completo para avaliar respostas de
entrevistas com modelos de linguagem.

A principal conclusão é que a IA pode auxiliar na organização e análise
preliminar das respostas, mas os resultados dependem do modelo, do prompt, dos
dados e do método de avaliação.

Por isso, qualquer aplicação real exigiria validação humana, auditoria de
vieses, transparência e controles rigorosos antes de ser utilizada.
