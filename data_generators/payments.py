import csv
import random

def generate_payments(num_payments=200, num_orders=200):
    # Payment methods
    payment_methods = ['Credit Card', 'Debit Card', 'PayPal', 'Bank Transfer', 'Cash on Delivery']
    
    # Payment statuses
    statuses = ['SUCCESS', 'FAILED', 'PENDING']
    
    payments = []
    
    for i in range(1, num_payments + 1):
        # Higher probability for SUCCESS status (about 80%)
        status_weights = [0.8, 0.15, 0.05]
        status = random.choices(statuses, weights=status_weights, k=1)[0]
        
        payment = {
            'payment_id': i,
            'order_id': random.randint(1, num_orders),
            'payment_method': random.choice(payment_methods),
            'status': status
        }
        payments.append(payment)
    
    return payments

def save_payments_to_csv(payments, filename='../data/payments.csv'):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['payment_id', 'order_id', 'payment_method', 'status']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for payment in payments:
            writer.writerow(payment)

if __name__ == "__main__":
    payments = generate_payments()
    save_payments_to_csv(payments)
    print(f"Generated {len(payments)} payments in payments.csv")