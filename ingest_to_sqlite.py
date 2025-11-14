import sqlite3
import csv
import os

def create_database(db_name='ecommerce.db'):
    """Create SQLite database and tables"""
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    # Create users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            city TEXT NOT NULL
        )
    ''')
    
    # Create products table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            product_id INTEGER PRIMARY KEY,
            product_name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    
    # Create orders table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            order_id INTEGER PRIMARY KEY,
            user_id INTEGER NOT NULL,
            order_date DATE NOT NULL,
            total_amount REAL NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(user_id)
        )
    ''')
    
    # Create order_items table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS order_items (
            order_item_id INTEGER PRIMARY KEY,
            order_id INTEGER NOT NULL,
            product_id INTEGER NOT NULL,
            quantity INTEGER NOT NULL,
            FOREIGN KEY (order_id) REFERENCES orders(order_id),
            FOREIGN KEY (product_id) REFERENCES products(product_id)
        )
    ''')
    
    # Create payments table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS payments (
            payment_id INTEGER PRIMARY KEY,
            order_id INTEGER NOT NULL,
            payment_method TEXT NOT NULL,
            status TEXT NOT NULL,
            FOREIGN KEY (order_id) REFERENCES orders(order_id)
        )
    ''')
    
    conn.commit()
    return conn

def insert_data_from_csv(conn, table_name, csv_file_path, columns):
    """Insert data from CSV file into specified table"""
    cursor = conn.cursor()
    
    with open(csv_file_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        placeholders = ','.join(['?' for _ in columns])
        insert_query = f'INSERT INTO {table_name} ({",".join(columns)}) VALUES ({placeholders})'
        
        rows = []
        for row in reader:
            # Extract values in the same order as columns
            values = [row[col] for col in columns]
            rows.append(values)
        
        cursor.executemany(insert_query, rows)
        print(f"Inserted {cursor.rowcount} records into {table_name}")
    
    conn.commit()

def main():
    # Create database and tables
    conn = create_database()
    
    # Define table schemas
    table_configs = [
        {
            'table': 'users',
            'csv_file': 'data/users.csv',
            'columns': ['user_id', 'name', 'email', 'city']
        },
        {
            'table': 'products',
            'csv_file': 'data/products.csv',
            'columns': ['product_id', 'product_name', 'category', 'price']
        },
        {
            'table': 'orders',
            'csv_file': 'data/orders.csv',
            'columns': ['order_id', 'user_id', 'order_date', 'total_amount']
        },
        {
            'table': 'order_items',
            'csv_file': 'data/order_items.csv',
            'columns': ['order_item_id', 'order_id', 'product_id', 'quantity']
        },
        {
            'table': 'payments',
            'csv_file': 'data/payments.csv',
            'columns': ['payment_id', 'order_id', 'payment_method', 'status']
        }
    ]
    
    # Insert data for each table
    for config in table_configs:
        try:
            insert_data_from_csv(
                conn, 
                config['table'], 
                config['csv_file'], 
                config['columns']
            )
        except Exception as e:
            print(f"Error inserting data into {config['table']}: {e}")
    
    # Close connection
    conn.close()
    print("Data ingestion completed successfully!")

if __name__ == "__main__":
    main()