from db import mydb
mycursor = mydb.cursor()

def get_all_products():
    mycursor.execute("SELECT * FROM products")
    myresult = mycursor.fetchall()
    return myresult

def get_product_by_id(product_id):
    mycursor.execute("SELECT * FROM products WHERE id = %s", (product_id,))
    myresult = mycursor.fetchone()
    return myresult

def create_product(name, category, price, stock, brand):
    mycursor.execute("INSERT INTO products (name, category, price, stock, brand) VALUES (%s, %s, %s, %s, %s)", (name, category, price, stock, brand))
    mydb.commit()
    return mycursor.lastrowid

def update_product(product_id, name, category, price, stock, brand):
    mycursor.execute(
        "UPDATE products SET name = %s, category = %s, price = %s, stock = %s, brand = %s WHERE id = %s",
        (name, category, price, stock, brand, product_id)
    )
    mydb.commit()
    return mycursor.rowcount

def delete_product(product_id):
    mycursor.execute("DELETE FROM products WHERE id = %s", (product_id,))
    mydb.commit()
    return mycursor.rowcount
