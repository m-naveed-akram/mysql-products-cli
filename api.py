from flask import Flask, jsonify, request
from models import get_all_products, get_product_by_id, create_product, update_product, delete_product


app = Flask(__name__)

@app.route('/health')
def health():
    return jsonify({'message': 'API is healthy.'})

@app.route('/database-check')
def database_check():
    get_all_products()
    return jsonify({'message': 'Database connection successful and products retrieved.'})


@app.route('/products', methods=['GET'])
def products():
    try:
        products = get_all_products()
        result = []

        for product in products:
            id, name, category, price, stock, brand = product
            product_dict = {
            "id": id,
            "name": name,
            "category": category,
            "price": float(price),
            "stock": stock,
            "brand": brand
            }
            result.append(product_dict)
        return jsonify(result)
    except:
        return jsonify({'message': 'Something went wrong'}), 500

@app.route('/products/<int:product_id>', methods=['GET'])
def product_by_id(product_id):

    try:
        product = get_product_by_id(product_id)
        if product:
            id, name, category, price, stock, brand = product
            product_dict = {
                "id": id,
                "name": name,
                "category": category,
                "price": float(price),
                "stock": stock,
                "brand": brand
            }
            return jsonify(product_dict)
        else:
            return jsonify({'message': 'Product not found.'}), 404
    except:
        return jsonify({'message': 'Something went wrong'}), 500

    
@app.route('/products', methods=['POST'])
def create_product_api():

    try:
        data = request.get_json()
        name = data.get('name')
        category = data.get('category')
        price = data.get('price')
        stock = data.get('stock')
        brand = data.get('brand')
        if name is None or category is None or price is None or stock is None or brand is None:
            return jsonify({'message': 'Missing required product data'}), 400
        new_product = create_product(name, category, price, stock, brand)
        return jsonify({"id": new_product,"message": "Product created"}), 201
    except:
        return jsonify({'message': 'Something went wrong'}), 500

@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product_api(product_id):
    try:
        product = get_product_by_id(product_id)

        if not product:
                return jsonify({'message': 'Product not found.'}), 404
        data = request.get_json()
        name = data.get('name')
        category = data.get('category')
        price = data.get('price')
        stock = data.get('stock')
        brand = data.get('brand')

        if name is None or category is None or price is None or stock is None or brand is None:
                return jsonify({'message': 'Missing required product data'}), 400

        update_product(product_id, name, category, price, stock, brand)
        return jsonify({'message': 'Product updated successfully.'}), 200
    except:
        return jsonify({'message': 'Something went wrong'}), 500
    
@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product_api(product_id):
    try:
        product = get_product_by_id(product_id)
        if not product:
            return jsonify({'message': 'Product not found.'}), 404
        delete_product(product_id)
        return jsonify({'message': 'Product deleted successfully.'}), 200
    except:
        return jsonify({'message': 'Something went wrong'}), 500
