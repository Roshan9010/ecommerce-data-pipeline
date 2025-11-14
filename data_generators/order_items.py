import csv
import random

def generate_order_items(num_items=400, num_orders=200, num_products=50):
    order_items = []
    
    for i in range(1, num_items + 1):
        order_item = {
            'order_item_id': i,
            'order_id': random.randint(1, num_orders),
            'product_id': random.randint(1, num_products),
            'quantity': random.randint(1, 10)
        }
        order_items.append(order_item)
    
    return order_items

def save_order_items_to_csv(order_items, filename='../data/order_items.csv'):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['order_item_id', 'order_id', 'product_id', 'quantity']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for item in order_items:
            writer.writerow(item)

if __name__ == "__main__":
    order_items = generate_order_items()
    save_order_items_to_csv(order_items)
    print(f"Generated {len(order_items)} order items in order_items.csv")