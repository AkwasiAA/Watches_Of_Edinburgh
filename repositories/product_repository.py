from db.run_sql import run_sql

from models.supplier import Supplier
from models.product import Product

import repositories.supplier_repository as supplier_repository

def save(product):
    sql = "INSERT INTO products (product_name, prod_description, quantity, purchase_price, selling_price, supplier_id) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *"
    values = [product.product_name, product.prod_description, product.quantity, product.purchase_price, product.selling_price, product.supplier.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    product.id = id
    return product

def select_all():
    products = []
    # create an sql statement to select all products

    sql = "SELECT * FROM products"
    results = run_sql(sql)
    # execute sql statement and get results
    for row in results:
        supplier = supplier_repository.select(row['supplier_id'])
        product = Product(row['product_name'], row['prod_description'], row['quantity'], row['purchase_price'], row['selling_price'], supplier, row['id'] )
        products.append(product)
    # return list of all products
    return products

def select(id):
    product = None
    sql = "SELECT * FROM products WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        supplier = supplier_repository.select(result['supplier_id'])
        product = Product(result['product_name'], result['prod_description'], result['quantity'], result['purchase_price'], result['selling_price'], supplier, result['id'] )
    return product

def delete_all():
    sql = "DELETE  FROM products"
    run_sql(sql)

def delete(id):
    sql = "DELETE  FROM products WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(product):
    sql = "UPDATE products SET (product_name, prod_description, quantity, purchase_price, selling_price, supplier_id) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [product.product_name, product.prod_description, product.quantity, product.purchase_price, product.selling_price, product.supplier.id, product.id]
    print(values)
    run_sql(sql, values)

