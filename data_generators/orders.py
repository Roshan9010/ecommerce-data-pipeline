import csv
import random
from datetime import datetime, timedelta
from faker import Faker

def generate_orders(num_orders=200, num_users=100):
    fake = Faker()
    
    # Generate orders for the last year
    orders = []
    start_date = datetime.now() - timedelta(days=365)
    
    for i in range(1, num_orders + 1):
        # Random order date within the last year
        order_date = fake.date_between(start_date=start_date, end_date=datetime.now())
        
        order = {
            'order_id': i,
            'user_id': random.randint(1, num_users),
            'order_date': order_date.strftime('%Y-%m-%d'),
            'total_amount': round(random.uniform(10.0, 1000.0), 2)
        }
        orders.append(order)
    
    return orders

def save_orders_to_csv(orders, filename='../data/orders.csv'):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['order_id', 'user_id', 'order_date', 'total_amount']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for order in orders:
            writer.writerow(order)

if __name__ == "__main__":
    orders = generate_orders()
    save_orders_to_csv(orders)
    print(f"Generated {len(orders)} orders in orders.csv")