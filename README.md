# Product API

This project is a Flask-based Product API connected to a MySQL database.

The API allows users to view, create, update, and delete products.

## API Endpoints

GET `/products` - Get all products.
GET `/products/<product_id>` - Get a single product by ID.
POST `/products` - Create a new product.
PUT `/products/<product_id>` - Update an existing product.
DELETE `/products/<product_id>` - Delete a product.

## Product JSON Fields

`name` - Product name.
`category` - Product category.
`price` - Product price.
`stock` - Available quantity of the product.
`brand` - Product brand.

## Status Codes

`200 OK` - The request was completed successfully.
`201 Created` - A new product was created successfully.
`400 Bad Request` - Required product data is missing or invalid.
`404 Not Found` - The requested product was not found in the database.
`500 Internal Server Error` - An unexpected error occurred on the server.

## How the API Works

`api.py` - Receives HTTP requests from the client and returns JSON responses.
`models.py` - Contains the product functions that perform database operations such as getting, creating, updating, and deleting products.
`db.py` - Creates and manages the connection to the MySQL database.