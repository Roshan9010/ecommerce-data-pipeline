import csv
import random
from faker import Faker

def generate_products(num_products=50):
    fake = Faker()
    
    # Define some product categories
    categories = ['Electronics', 'Clothing', 'Books', 'Home & Kitchen', 'Sports', 'Beauty', 'Toys', 'Food']
    
    # Define some product name templates
    product_templates = [
        '{} Pro', '{} Plus', '{} Max', '{} Lite', '{} Deluxe', '{} Basic',
        'Super {}', 'Premium {}', 'Advanced {}', '{} Model X', '{} Edition'
    ]
    
    products = []
    
    for i in range(1, num_products + 1):
        category = random.choice(categories)
        
        # Generate product names based on category
        if category == 'Electronics':
            product_base = fake.word() + ' ' + fake.word()
        elif category == 'Clothing':
            product_base = fake.color_name() + ' ' + fake.word()
        elif category == 'Books':
            product_base = fake.sentence(nb_words=3).rstrip('.')
        elif category == 'Home & Kitchen':
            product_base = fake.word() + ' ' + fake.word()
        elif category == 'Sports':
            product_base = fake.word() + ' ' + fake.word()
        elif category == 'Beauty':
            product_base = fake.word() + ' ' + fake.word()
        elif category == 'Toys':
            product_base = fake.word() + ' ' + fake.word()
        else:  # Food
            product_base = fake.word() + ' ' + fake.word()
            
        product_name_template = random.choice(product_templates)
        product_name = product_name_template.format(product_base.title())
        
        product = {
            'product_id': i,
            'product_name': product_name,
            'category': category,
            'price': round(random.uniform(5.0, 500.0), 2)
        }
        products.append(product)
    
    return products

def save_products_to_csv(products, filename='../data/products.csv'):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['product_id', 'product_name', 'category', 'price']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for product in products:
            writer.writerow(product)

if __name__ == "__main__":
    products = generate_products()
    save_products_to_csv(products)
    print(f"Generated {len(products)} products in products.csv")