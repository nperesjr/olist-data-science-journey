# Relatório de qualidade dos dados

Raio-x dos dados brutos da Olist: o que está vazio, duplicado ou inconsistente, e o que decidi fazer com cada problema.

## Valores vazios

| Tabela | Coluna(s) | Quantidade | É erro? | Decisão |
|---|---|---|---|---|
| order_reviews | `review_comment_title`, `review_comment_message` | 87.656 e 58.247 | Não. O cliente deu nota, mas não escreveu comentário. | Manter. |
| orders | datas de aprovação, envio e entrega | 160, 1.783 e 2.965 | Na maioria, não: pedidos cancelados ou não entregues ainda não têm essas datas. | Manter. |
| orders | mesmas datas, só em pedidos `delivered` | 14, 2 e 8 | Sim. Pedido entregue sem data registrada. | Manter com aviso. Ficam fora das análises de prazo. |
| products | categoria, tamanho do nome e da descrição, fotos | 610 (os mesmos produtos) | Sim. Cadastro incompleto. | Preencher a categoria com `sem_categoria`, para não sumirem das análises por categoria. Reportar ao time de cadastro. |
| products | peso e medidas | 2 | Sim. | Manter com aviso. Não há fonte confiável para preencher. Ficam fora de análises que usem peso ou tamanho. |

## Observações

- As colunas `product_name_lenght` e `product_description_lenght` têm erro de grafia no próprio dataset ("lenght" em vez de "length").

## Duplicados

### Linhas inteiras repetidas

| Tabela | Quantidade | É erro? | Decisão |
|---|---|---|---|
| geolocation | 261.831 (26% da tabela) | Não é informação errada, só repetição: o mesmo ponto (CEP, latitude, longitude, cidade e estado) aparece mais de uma vez. | Remover as cópias. Nada se perde. |
| demais tabelas | 0 | | |

### Repetições que não são cópia exata

- `order_reviews`: alguns pedidos têm mais de uma avaliação (encontrado no Ticket 1). Antes de analisar notas por pedido, decidir qual avaliação usar.
- `geolocation`: mesmo sem cópias, cada prefixo de CEP tem vários pontos diferentes. Para ligar com clientes e vendedores, será preciso escolher um ponto por CEP.

## Datas impossíveis ou suspeitas

O caminho esperado de um pedido é: compra → aprovação → entrega à transportadora → entrega ao cliente.

| Teste | Quantidade | Avaliação | Decisão |
|---|---|---|---|
| Entrega ao cliente antes da compra | 0 | Nenhum caso. | Nada a fazer. |
| Entrega à transportadora antes da compra | 166 | Impossível. Provável erro de registro. | Manter com aviso. Não afeta o cálculo de atraso, que usa a entrega ao cliente. |
| Entrega à transportadora antes da aprovação do pagamento | 1.359 | Suspeito, mas pode ser prática do negócio. | Confirmar com o time de operações se vendedores podem despachar antes da aprovação (ex.: clientes especiais). Manter até a resposta. |

## Funções de limpeza

As decisões acima viraram funções em `src/limpeza.py`, usadas pelos notebooks:

- `carregar_tabelas()`: carrega os 9 CSVs com nomes curtos.
- `preencher_categoria(produtos)`: preenche os 610 produtos sem categoria com `sem_categoria`.
- `remover_duplicadas(tabela)`: remove linhas repetidas (na `geolocation`, de 1.000.163 para 738.332 linhas).