"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv

conn = psycopg2.connect(
    host='localhost',
    database='north',
    user='postgres',
    password='kloping6'
)

with conn.cursor() as cur:
    with open("north_data/employees_data.csv", "r", encoding='UTF-8') as file:
        file_reader = csv.reader(file, delimiter=",")
        count = 0
        for row in file_reader:
            if count == 0:
                count += 1
                continue
            cur.execute("insert into employees (employee_id, first_name, last_name, title, birth_date, notes) values (%s, %s, %s, %s, %s, %s)", (int(row[0]), row[1], row[2], row[3], row[4], row[5]))
            count += 1
    conn.commit()
    conn.close()

with conn.cursor() as cur:
    with open("north_data/customers_data.csv", "r", encoding='UTF-8') as file:
        file_reader = csv.reader(file, delimiter=",")
        count = 0
        for row in file_reader:
            if count == 0:
                count += 1
                continue
            cur.execute("insert into customers (customer_id, company_name, contact_name) values (%s, %s, %s)", (row[0], row[1], row[2]))
            count += 1
    conn.commit()
    conn.close()


with conn.cursor() as cur:
    with open("north_data/orders_data.csv", "r", encoding='UTF-8') as file:
        file_reader = csv.reader(file, delimiter=",")
        count = 0
        for row in file_reader:
            if count == 0:
                count += 1
                continue
            cur.execute("insert into orders (order_id, customer_id, employee_id, order_date, ship_city) values (%s, %s, %s, %s, %s)", (int(row[0]), row[1], int(row[2]), row[3], row[4]))
            count += 1
    conn.commit()
    conn.close()