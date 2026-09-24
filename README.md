# AI Interview Evaluator

Projeto experimental que investiga o uso de modelos de linguagem na avaliação de respostas textuais de entrevistas comportamentais.

O objetivo é analisar a capacidade de um modelo de linguagem de produzir avaliações estruturadas, consistentes e interpretáveis, sem substituir avaliadores humanos ou automatizar decisões reais de contratação.

> **Aviso:** este projeto tem finalidade educacional e experimental. Os resultados não devem ser utilizados isoladamente em processos seletivos reais.

---

## Objetivos

O projeto busca investigar:

- como um modelo de linguagem avalia respostas de entrevistas;
- se diferentes avaliações podem ser comparadas com uma referência inicial;
- se o modelo produz respostas semelhantes ao receber a mesma entrada;
- se a saída em JSON facilita a análise automática;
- se alterações em informações pessoais fictícias podem influenciar as notas;
- quais limitações surgem durante o uso de APIs de modelos de linguagem.

---

## Experimentos realizados

### 1. Primeira avaliação

Avaliação de respostas sintéticas utilizando os seguintes critérios:

- relevância;
- especificidade;
- comunicação;
- reflexão;
- resultado.

As notas geradas pelo modelo foram comparadas com uma referência inicial criada manualmente. Foram calculados erro médio absoluto, diferença média, médias por competência e correlação de Spearman.

Notebook:

`notebooks/01_primeira_avaliacao.ipynb`

### 2. Consistência das avaliações

Análise da variação das notas quando a mesma pergunta, competência e resposta são enviadas ao modelo mais de uma vez.

Foram calculadas métricas como média, desvio padrão, valor mínimo e valor máximo das avaliações.

Notebook:

`notebooks/02_consistencia_avaliacao.ipynb`

### 3. Saída estruturada

Teste do retorno das avaliações em formato JSON, facilitando o armazenamento das notas em colunas numéricas e a análise automática dos resultados.

O experimento também registrou respostas brutas quando o JSON retornado pelo modelo era inválido ou incompleto.

Notebook:

`notebooks/03_saida_estruturada.ipynb`

### 4. Análise exploratória de possíveis vieses

Comparação de avaliações para perfis sintéticos, mantendo a mesma pergunta e a mesma resposta, mas alterando informações de contexto, como nome e pronome.

Uma diferença entre as avaliações não prova, sozinha, a existência de viés. O resultado deve ser interpretado considerando o tamanho reduzido da amostra, o modelo utilizado e o formato do prompt.

Notebook:

`notebooks/04_analise_de_vies.ipynb`

---

## Dataset

O projeto utiliza um dataset sintético criado para fins educacionais. As respostas não pertencem a candidatos reais.

As competências analisadas são:

- resolução de problemas;
- trabalho em equipe;
- organização.

Dataset principal:

`data/sample/entrevista_dataset_inicial.jsonl`

---

## Estrutura do projeto

```text
ai-interview-evaluator/
├── configs/
├── data/
│   ├── README.md
│   └── sample/
├── notebooks/
│   ├── 00_setup.ipynb
│   ├── 01_primeira_avaliacao.ipynb
│   ├── 02_consistencia_avaliacao.ipynb
│   ├── 03_saida_estruturada.ipynb
│   └── 04_analise_de_vies.ipynb
├── reports/
├── results/
│   ├── figures/
│   └── tables/
├── src/
│   ├── avaliador.py
│   └── metricas.py
├── .gitignore
├── README.md
└── requirements.txt
```

---

## Tecnologias utilizadas

- Python;
- Google Colab;
- Pandas;
- NumPy;
- Scikit-learn;
- Matplotlib;
- Seaborn;
- OpenAI Python SDK;
- Hugging Face Inference Providers;
- Git e GitHub.

---

## Como executar

### 1. Instalar as dependências

No Google Colab, execute:

```python
%pip install -q openai pandas pydantic python-dotenv scikit-learn matplotlib seaborn
```

Em um ambiente local, utilize:

```bash
pip install -r requirements.txt
```

### 2. Configurar a API

No Google Colab, crie um segredo chamado:

`HF_TOKEN`

O token deve ser armazenado nos Secrets do Colab. Ele não deve ser colocado diretamente no código nem enviado ao GitHub.

### 3. Executar os notebooks

A ordem recomendada é:

1. `00_setup.ipynb`;
2. `01_primeira_avaliacao.ipynb`;
3. `02_consistencia_avaliacao.ipynb`;
4. `03_saida_estruturada.ipynb`;
5. `04_analise_de_vies.ipynb`.

As células que realizam chamadas em lote podem consumir créditos da API. Por isso, evite executá-las novamente sem necessidade.

---

## Resultados

As tabelas geradas pelos experimentos são armazenadas em:

`results/tables/`

Os gráficos são armazenados em:

`results/figures/`

Os relatórios dos experimentos são armazenados em:

`reports/`

---

## Principais aprendizados

Os experimentos mostraram que:

- modelos de linguagem podem gerar avaliações seguindo uma rubrica definida;
- prompts detalhados ajudam a organizar os critérios de avaliação;
- o formato JSON facilita o armazenamento e a análise automática das notas;
- respostas inválidas exigem validação e tratamento de erros;
- correlação não significa que duas avaliações sejam exatamente iguais;
- pequenas amostras não permitem conclusões gerais;
- possíveis diferenças entre perfis precisam ser investigadas com experimentos maiores;
- sistemas desse tipo não devem tomar decisões de contratação de forma autônoma.

---

## Limitações

- O dataset é pequeno e sintético.
- Foram utilizados poucos exemplos.
- As avaliações de referência não representam um consenso amplo de avaliadores humanos.
- Os resultados dependem do modelo e do prompt utilizados.
- A API pode retornar erros, JSON inválido ou respostas incompletas.
- A análise de possíveis vieses utiliza perfis fictícios.
- Os resultados são exploratórios e não devem ser generalizados para processos seletivos reais.
- A IA não deve tomar decisões de contratação sozinha.

---

## Considerações éticas

Sistemas de avaliação automatizada podem reproduzir ou ampliar vieses presentes nos dados e nos modelos de linguagem.

Um uso real exigiria participação humana, auditoria de vieses, transparência sobre o uso da IA, proteção dos dados dos candidatos e possibilidade de revisão das avaliações produzidas pelo modelo.

---

## Próximos passos

- ampliar o dataset sintético;
- obter avaliações de múltiplos avaliadores humanos;
- comparar diferentes modelos de linguagem;
- criar testes automatizados para os módulos em `src/`;
- melhorar a validação das respostas JSON;
- investigar métricas específicas de equidade;
- repetir os experimentos com mais respostas.

---

## Status do projeto

Projeto experimental em desenvolvimento, com foco na construção da metodologia, na análise dos resultados e na documentação das limitações do uso de modelos de linguagem em entrevistas.
