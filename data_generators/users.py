import csv
import random
from faker import Faker

def generate_users(num_users=100):
    fake = Faker()
    users = []
    
    for i in range(1, num_users + 1):
        user = {
            'user_id': i,
            'name': fake.name(),
            'email': fake.email(),
            'city': fake.city()
        }
        users.append(user)
    
    return users

def save_users_to_csv(users, filename='../data/users.csv'):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['user_id', 'name', 'email', 'city']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for user in users:
            writer.writerow(user)

if __name__ == "__main__":
    users = generate_users()
    save_users_to_csv(users)
    print(f"Generated {len(users)} users in users.csv")