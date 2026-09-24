# AI Interview Evaluator

Projeto experimental que investiga o uso de modelos de linguagem na avaliação de
respostas textuais de entrevistas comportamentais.

O objetivo é analisar a capacidade de um modelo de linguagem de produzir
avaliações estruturadas, consistentes e interpretáveis, sem substituir
avaliadores humanos ou automatizar decisões reais de contratação.

> **Aviso:** este projeto tem finalidade educacional e experimental. Os resultados
> não devem ser utilizados isoladamente em processos seletivos reais.

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

As notas geradas pelo modelo foram comparadas com uma referência inicial criada
manualmente. Foram calculados erro médio absoluto, diferença média, médias por
competência e correlação de Spearman.

Notebook:

```text
notebooks/01_primeira_avaliacao.ipynb
