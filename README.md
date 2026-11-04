# Olist Data Science Journey

Projeto de estudo em ciência de dados e engenharia de IA/ML, usando dados reais e públicos de e-commerce brasileiro.

## Como este projeto foi estruturado

Para praticar como numa empresa de verdade, o projeto simula um time de dados dentro de um marketplace. Cada etapa é um "ticket" pedido por um departamento (Logística, Marketing, Financeiro...), com contexto de negócio, entregável e critério de pronto.

São 30 tickets em 3 níveis:
- **Júnior:** análise exploratória, limpeza de dados, estatística e primeiro modelo.
- **Pleno:** pipelines, avaliação de modelos e modelo servido como API.
- **Sênior:** produção, experimentos, LLM e decisões de arquitetura.

Estruturei assim para ver, na prática, como Python, SQL e as bibliotecas de dados que estou estudando são usados no dia a dia de uma empresa, e como esse trabalho muda do nível júnior ao sênior. Como Product Manager, já recebo pedidos de diferentes áreas e transformo em entregas; aqui faço o mesmo, só que do lado dos dados. A gamificação (tickets, níveis e code review) foi montada com apoio do Claude, que também faz o papel de Tech Lead nas revisões.

## Progresso

| Ticket | Tema | Status |
|---|---|---|
| J01 | Onboarding e dicionário de dados | ✅ |

## Dados

[Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce), publicado pela Olist no Kaggle. Cerca de 99 mil pedidos de 2016 a 2018.

Licença: CC BY-NC-SA 4.0. Os dados não estão neste repositório: para rodar o projeto, baixe pelo link acima e coloque os CSVs na pasta `data/`.

Detalhes das tabelas em [DATA_DICTIONARY.md](DATA_DICTIONARY.md).

## Estrutura

- `notebooks/`: análises, uma por ticket
- `src/`: funções reutilizáveis
- `reports/`: relatórios e gráficos
- `data/`: dados (não versionados)