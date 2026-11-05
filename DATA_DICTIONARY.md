# Dicionário de dados

Fonte: [Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) (Kaggle).
Período: 2016 a 2018. Licença: CC BY-NC-SA 4.0.

## Visão geral

> Nos notebooks, os nomes das tabelas foram encurtados: o prefixo `olist_` e o sufixo `_dataset` foram removidos, e `product_category_name_translation` virou `category_translation`.

| Tabela               | Linhas  | O que cada linha representa | Chave         |
| -------------------- | ------- | --------------------------- | ------------- |
| customers            | 99441   | Um cliente                  | `customer_id` |
| geolocation          | 1000163 | Um zip code prefix          | `geolocation_zip_code_prefix`|
| order_items          | 112650  | Um item do pedido           | `order_id`               |
| order_payments       | 103886  | Um pagamento do pedido      | `order_id`               |
| order_reviews        | 99224   | Uma avaliação do pedido     | `order_id`               |
| orders               | 99441   | Um pedido                   | `order_id`    |
| products             | 32951   | Um produto                  | `product_id`  |
| sellers              | 3095    | Um vendedor                 | `sellers_id`  |
| category_translation | 71      | Uma categoria de produto                            | `product_category_name`              |


## Como as tabelas se ligam

## Como as tabelas se ligam

A tabela `orders` é o centro: quase tudo se liga a ela pelo `order_id`.

- `orders` → `customers` pelo `customer_id`
- `order_items` → `orders` pelo `order_id`
- `order_payments` → `orders` pelo `order_id`
- `order_reviews` → `orders` pelo `order_id`
- `order_items` → `products` pelo `product_id`
- `order_items` → `sellers` pelo `seller_id`
- `products` → `category_translation` pelo `product_category_name`
- `customers` → `geolocation` pelo prefixo do CEP (`customer_zip_code_prefix` = `geolocation_zip_code_prefix`)
- `sellers` → `geolocation` pelo prefixo do CEP (`seller_zip_code_prefix` = `geolocation_zip_code_prefix`)

## Tabelas

### orders

Um pedido feito no marketplace. É a tabela central: quase todas as outras se ligam a ela.

| Coluna | Tipo | Descrição | Observações |
|---|---|---|---|
| `order_id` | texto | Identificador do pedido | Chave. Único por linha. |
| `customer_id` | texto | Código do cliente gerado para cada pedido | Chave. Um por pedido; liga com `orders`. NÃO identifica a pessoa. |
| `order_status` | texto | Situação do pedido | Valores: delivered, shipped, canceled... |
| `order_purchase_timestamp` | data | Momento da compra | Lido como texto; converter para data. |
| `order_approved_at` | data | Pedido Aprovado | STR; separar entre data e hora. |
| `order_delivered_carrier_date` | data | Entrega a transportadora | STR; separar entre data e hora. |
| `order_delivered_customer_date` | data | Entrega ao cliente | Vazio em pedidos não entregues. |
| `order_estimated_delivery_date` | data | Prazo prometido | Base do cálculo de atraso. |

## Problemas encontrados

- `customers.customer_zip_code_prefix`: lido como número, perde o zero da frente (09790 virou 9790).

- 775 pedidos em `orders` não têm itens em `order_items`. A maioria tem status
  `unavailable` (603) ou `canceled` (164), o que é esperado. Alguns poucos têm
  status `created`, `invoiced` ou `shipped` sem nenhum item: provável
  inconsistência nos dados.
- Alguns pedidos têm mais de uma avaliação em `order_reviews`.
- Existe 1 pedido sem pagamento em `order_payments`.
- Para contar clientes, use `customer_unique_id` (96.096 pessoas), não `customer_id` (99.441, um por pedido).