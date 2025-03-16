import psycopg2
import sys

def connect_to_db():
    try:
        con = psycopg2.connect(
            dbname = "product_catalog",
            user = "joseph",
            password = "joseph",
            host = "localhost",
            port = "5432"
        )
        return con
    except psycopg2.Error as e:
        print(f"Error connecting to database: {e}")
        sys.exit(1)

def add_product(name,price,category,stock):
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO products (name,price,category,stock) VALUES (%s,%s,%s,%s)", (name,price,category,stock)
    )

    conn.commit()
    print(f"Added product: {name}")
    cursor.close()
    conn.close()

def view_products():
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()

    # if not products:
    #     print("No products found.")
    # else:
    #     for product in products:
    #         print(f"ID: {product[0]}, NAME: {product[1]}, PRICE: {product[2]}, CATEGORY: {product[3]}, STOCK: {product[4]}")
    if products:
        for product in products:
            print(f"ID: {product[0]}, NAME: {product[1]}, PRICE: Ksh {product[2]}, CATEGORY: {product[3]}, STOCK: {product[4]}")
    else:
        print("No products found.")

    cursor.close()
    conn.close()

def update_product(product_id, name=None,price=None,category=None,stock=None):
    conn = connect_to_db()
    cursor = conn.cursor()
    updates = []
    params = []

    if name:
        updates.append("name = %s")
        params.append(name)
    if price:
        updates.append("price = %s")
        params.append(price)
    if category:
        updates.append("category = %s")
        params.append(category)
    if stock:
        updates.append("stock = %s")
        params.append(stock)

    if updates:
        params.append(product_id)
        query = f"UPDATE products SET {', .join(updates)'} WHERE id = %s"
        cursor.execute(query,params)
        conn.commit()
        print(f"Updated product ID {product_id}")
    else:
        print("Nothing to update.")
    cursor.close()
    conn.close()

def delete_product(product_id):
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM products WHERE id = %s", (product_id,))

    if cursor.rowcount > 0:
        conn.commit()
        print(f"Deleted product ID {product_id}")
    else:
        print(f"Product ID {product_id} not found.")
    cursor.close()
    conn.close()

def search_product(name):
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products WHERE name ILIKE %s", (f"%{name}%",))
    products =cursor.fetchall()

    if not products:
        print(f"No product found matching '{name}'")
    else:
        for product in products:
            print(f"ID: {product[0]}, Name: {product[1]}, Price: {product[2]}, Category: {product[3]}, Stock: {product[4]}")
    
    conn.close()
    cursor.close()

def main():
    while True:
        print("\nProduct Catalog Menu:")
        print("1. Add Product")
        print("2. View All Products")
        print("3. Update Product")
        print("4. Delete Product")
        print("5. Search Product")
        print("6. Exit")

        choice = input("Enter your choice (1 - 6): ")

        if choice == "1":
            name = input("Enter product name: ")
            price = float(input("Enter price: "))
            category = input("Enter category: ")
            stock = int(input("Enter stock quantity: "))
            add_product(name,price,category,stock)

        elif choice == "2":
            view_products()

        elif choice == "3":
            product_id = int(input("Enter product ID to update: "))
            name = input("New name (leave blank to skip): ") or None
            price = input("New price (leave blank to skip): ")
            price = float(price) if price else None
            category = input("New category (leave blank to skip): ") or None
            stock = input("New stock (leave blank to skip): ")
            stock = int(stock) if stock else None
            update_product(product_id,name,price,category,stock)

        elif choice == "4":
            product_id = int(input("Enter product ID to delete: "))
            delete_product(product_id)

        elif choice == "5":
            name = input("Enter product name to search: ")
            search_product(name)

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()