Create database Product_tiki

use Product_tiki
go;

create table Product(
id int primary key,
sku nvarchar(255),
price nvarchar(255),
list_price nvarchar(255),
price_usd nvarchar(255),
discount nvarchar(255),
discount_rate nvarchar(255),
review_count nvarchar(255),
older_count nvarchar(255),
inventory_status nvarchar(255),
is_visible nvarchar(255),
stock_item_qty nvarchar(255),
stock_item_max_sale_qty nvarchar(255),
product_name nvarchar(255),
brand_id nvarchar(255),
brand_name nvarchar(255))

create table Comment(
id int primary key,
title nvarchar(255),
content nvarchar(500),
thank_count nvarchar(255),
customer_id nvarchar(255),
rating nvarchar(255),
created_at nvarchar(255),
purchased_at nvarchar(255),
FOREIGN KEY (id) REFERENCES Product(id))