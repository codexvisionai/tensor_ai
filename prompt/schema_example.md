# 📂 Ma'lumotlar bazasi strukturasi

## users
- id: integer, primary key
- full_name: text

## orders
- id: integer, primary key
- user_id: foreign key → users.id
- created_at: timestamp

## products
- id: integer, primary key
- name: text
- price: numeric

## order_items
- id: integer
- order_id: foreign key → orders.id
- product_id: foreign key → products.id
- quantity: integer
