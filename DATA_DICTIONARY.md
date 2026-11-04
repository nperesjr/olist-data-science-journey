# Dicionário de dados

Fonte: [Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) (Kaggle).
Período: 2016 a 2018. Licença: CC BY-NC-SA 4.0.

## Visão geral

| Tabela | Linhas | O que cada linha representa | Chave |
|---|---|---|---|
| orders | 99.441 | Um pedido | `order_id` |
| customers | | | |
| order_items | | | |
| ... | | | |

## Como as tabelas se ligam

- `orders` → `customers` pela coluna `customer_id`
- (continue: quem liga com quem, e por qual coluna)

## Tabelas

### orders

Um pedido feito no marketplace. É a tabela central: quase todas as outras se ligam a ela.

| Coluna | Tipo | Descrição | Observações |
|---|---|---|---|
| `order_id` | texto | Identificador do pedido | Chave. Único por linha. |
| `customer_id` | texto | Código do cliente gerado para cada pedido | Chave. Um por pedido; liga com `orders`. NÃO identifica a pessoa. |
| `customer_unique_id` | texto | Identificador da pessoa | Repete quando a mesma pessoa compra mais de uma vez. Use este para contar clientes. |
| `order_status` | texto | Situação do pedido | Valores: delivered, shipped, canceled... |
| `order_purchase_timestamp` | data | Momento da compra | Lido como texto; converter para data. |
| `order_delivered_customer_date` | data | Entrega ao cliente | Vazio em pedidos não entregues. |
| `order_estimated_delivery_date` | data | Prazo prometido | Base do cálculo de atraso. |

(Faltam 2 colunas de data aqui. Complete.)

## Problemas encontrados

- `customers.customer_zip_code_prefix`: lido como número, perde o zero da frente (09790 virou 9790).

- 775 pedidos em `orders` não têm itens em `order_items`. A maioria tem status
  `unavailable` (603) ou `canceled` (164), o que é esperado. Alguns poucos têm
  status `created`, `invoiced` ou `shipped` sem nenhum item: provável
  inconsistência nos dados.
- Alguns pedidos têm mais de uma avaliação em `order_reviews`.
- Existe 1 pedido sem pagamento em `order_payments`.
- Para contar clientes, use `customer_unique_id` (96.096 pessoas), não `customer_id` (99.441, um por pedido).