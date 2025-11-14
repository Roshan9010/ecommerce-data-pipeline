import sqlite3
from tabulate import tabulate

def run_report(db_name='ecommerce.db'):
    """Run a JOIN query across all tables and generate a report"""
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    # SQL query joining all tables
    query = '''
        SELECT 
            u.user_id,
            u.name,
            o.order_id,
            o.order_date,
            p.product_name,
            oi.quantity,
            p.price,
            o.total_amount,
            pay.payment_method,
            pay.status
        FROM users u
        JOIN orders o ON u.user_id = o.user_id
        JOIN order_items oi ON o.order_id = oi.order_id
        JOIN products p ON oi.product_id = p.product_id
        JOIN payments pay ON o.order_id = pay.order_id
        WHERE pay.status = 'SUCCESS'
        ORDER BY u.user_id, o.order_date
    '''
    
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        
        # Get column names
        column_names = [description[0] for description in cursor.description]
        
        # Display results in a table format
        if results:
            print(tabulate(results, headers=column_names, tablefmt='grid'))
            print(f"\nTotal records found: {len(results)}")
        else:
            print("No records found matching the criteria.")
            
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()

def main():
    print("E-Commerce Report (Successful Payments Only)")
    print("=" * 50)
    run_report()

if __name__ == "__main__":
    main()