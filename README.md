# E-Commerce Data Pipeline

A complete synthetic e-commerce data pipeline built with Python and SQLite. This project generates realistic e-commerce data, loads it into a database, and runs analytical reports.

## Project Structure

```
├── data/                   # Generated CSV files
│   ├── users.csv
│   ├── products.csv
│   ├── orders.csv
│   ├── order_items.csv
│   └── payments.csv
├── data_generators/        # Scripts to generate synthetic data
│   ├── users.py
│   ├── products.py
│   ├── orders.py
│   ├── order_items.py
│   └── payments.py
├── ecommerce.db            # SQLite database
├── ingest_to_sqlite.py     # Data ingestion script
└── run_report.py           # Reporting script
```

## Components

### 1. Data Generation
Five Python scripts in the `data_generators/` folder generate realistic synthetic e-commerce data:

- **users.py**: Creates 100 users with names, emails, and cities
- **products.py**: Creates 50 products with categories and prices
- **orders.py**: Creates 200 orders with dates and amounts
- **order_items.py**: Creates 400 order items linking orders to products
- **payments.py**: Creates 200 payments with methods and statuses

All data is saved as CSV files in the `data/` folder.

### 2. Data Ingestion
The `ingest_to_sqlite.py` script:
- Creates an SQLite database named `ecommerce.db`
- Defines tables with proper schema and foreign key relationships
- Loads all CSV data into the corresponding database tables

### 3. Reporting
The `run_report.py` script:
- Connects to the SQLite database
- Runs a JOIN query across all tables
- Filters for only successful payments
- Displays a formatted report with user, order, product, and payment information

## Database Schema

```
users (user_id, name, email, city)
products (product_id, product_name, category, price)
orders (order_id, user_id, order_date, total_amount)
order_items (order_item_id, order_id, product_id, quantity)
payments (payment_id, order_id, payment_method, status)
```

## Requirements

- Python 3.x
- faker library (`pip install faker`)
- tabulate library (`pip install tabulate`)

## Usage

1. Generate synthetic data:
   ```
   cd data_generators
   python users.py
   python products.py
   python orders.py
   python order_items.py
   python payments.py
   ```

2. Ingest data into SQLite:
   ```
   python ingest_to_sqlite.py
   ```

3. Run the report:
   ```
   python run_report.py
   ```

## Sample Report Output

The report joins all tables and displays information including:
- User ID and name
- Order ID and date
- Product name
- Quantity and price
- Total order amount
- Payment method and status (filtered to show only successful payments)

![Sample Report](sample_report.png)

## License

This project is open source and available under the MIT License.