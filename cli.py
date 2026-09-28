from models import get_all_products, get_product_by_id, create_product, update_product, delete_product

menu_choice = 0
while menu_choice != 6:
    print("1. Get all products")
    print("2. Get product by ID")
    print("3. Add a product")
    print("4. Update a product")
    print("5. Delete a product")
    print("6. Exit")
    menu_choice = int(input("Enter your choice: "))
    if menu_choice == 1:
        myresult = get_all_products()
        
        if myresult:
            for product in myresult:
                print(product)
        else:
             print("No products found")
    elif menu_choice == 2:
        product_id = int(input("Enter product ID: "))
        product = get_product_by_id(product_id)
        if product:
            print(product)
        else:
            print("Product not found")

    elif menu_choice == 3:
        name = input("Enter product name: ")
        category = input("Enter product category: ")
        price = float(input("Enter product price: "))
        stock = int(input("Enter product stock: "))
        brand = input("Enter product brand: ")
        new_id = create_product(name, category, price, stock, brand)
        print(f"Product added with ID: {new_id}")

    elif menu_choice == 4:
        product_id = int(input("Enter product ID to update: "))
        product = get_product_by_id(product_id)
        if product:
            print(f"Current product details: {product}")
            name = input("Enter new product name: ")
            category = input("Enter new product category: ")
            price = float(input("Enter new product price: "))
            stock = int(input("Enter new product stock: "))
            brand = input("Enter new product brand: ")
            rows_updated = update_product(product_id, name, category, price, stock, brand)
            if rows_updated > 0:
                print("Product updated successfully")
                updated_product = get_product_by_id(product_id)
                print(f"Updated product details: {updated_product}")
            else:
                print("Failed to update product")
        else:
            print("Product not found")

    elif menu_choice == 5:
        product_id = int(input("Enter product ID to delete: "))
        product = get_product_by_id(product_id)
        if product:
            print(f"Product found: {product}")
            confirm = input("Are you sure you want to delete this product? (yes/no): ")
            if confirm.lower() == "yes":
                rows_deleted = delete_product(product_id)
                if rows_deleted > 0:
                    print("Product deleted successfully")
                else:
                    print("Failed to delete product")
            else:
                print("Deletion cancelled")
        else:
            print("Product not found")
        

    elif menu_choice == 6:
        print("Exiting...")