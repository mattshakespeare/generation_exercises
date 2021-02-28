import pymysql
import os
from dotenv import load_dotenv
import csv
import datetime
# Load environment variables from .env file

load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
warehouse = os.environ.get("mysql_db")
# Establish a database connection
con = pymysql.connect(
    host = host,
    user = user,
    password = password,
    database = warehouse
)

cur = con.cursor(pymysql.cursors.DictCursor)


#create table for raw data
cur.execute('''CREATE TABLE IF NOT EXISTS sales(
                id INT NOT NULL AUTO_INCREMENT,
                customer_id INT NOT NULL,
                purchase_date DATE NOT NULL,
                purchase_amount FLOAT NOT NULL,
                product_id VARCHAR(10) NOT NULL,
                PRIMARY KEY(id));''')

#stores raw data from csv file
csv_list = []

#reading csv file
with open('sales_data.csv','r') as file:
    reader = csv.DictReader(file, delimiter=',')
    
    for row in reader:
        csv_list.append(row)

#convert customer_id into int
for row in csv_list:
    row['customer_id'] = int(row['customer_id'])

#convert purchase_amount into float
for row in csv_list:
    if row['purchase_amount'] != '':
        row['purchase_amount'] = float(row['purchase_amount'])
    else:
        row['purchase_amount'] = 0

#Inserts csv list into DB
for row in csv_list:
    cur.execute('''INSERT INTO sales(customer_id, purchase_date, purchase_amount, product_id)
                    VALUES(%s,DATE(%s),%s,%s)''',(row['customer_id'], row['purchase_date'], row['purchase_amount'], row['product_id']))
    con.commit()

#remove rows with null fields from product amount
cur.execute('''DELETE FROM sales WHERE purchase_amount = 0 ''')
con.commit()

#remove rows with null fields from product id
cur.execute('''DELETE FROM sales WHERE product_id = '' ''')
con.commit()

#create table containing customer total spend and customer average spend
cur.execute('''CREATE TABLE IF NOT EXISTS customer_spend(
                customer_id INT NOT NULL,
                total_spend FLOAT NOT NULL,
                average_spend FLOAT NOT NULL
                );''')


#find sum and average for each customer id and insert into table
cur.execute('''SELECT customer_id, SUM(purchase_amount) as s, AVG(purchase_amount) as a
                FROM warehouse.sales
                GROUP BY customer_id ''') 
total = cur.fetchall() 

#insert values into table
for row in total:
    
    cur.execute('''INSERT INTO customer_spend(customer_id, total_spend, average_spend)
                    VALUES(%s,%s,%s)''', (row['customer_id'], row['s'], row['a']))
    con.commit()

#create table containing count of product id for each customer
cur.execute('''CREATE TABLE IF NOT EXISTS product_count(
                customer_id INT NOT NULL,
                product_id VARCHAR(10) NOT NULL,
                quantity INT NOT NULL);''')

#find count of each product brought by each customer

cur.execute('SELECT customer_id FROM sales GROUP BY customer_id')
customer_id = cur.fetchall()

for i in customer_id:
    
    cur.execute(f'''SELECT customer_id, product_id, COUNT(customer_id) as q
                    FROM warehouse.sales
                    WHERE customer_id = {i['customer_id']}
                    GROUP BY product_id ''')
    
    quantity = cur.fetchall()
    
    
    for item in quantity:
        
        cur.execute('''INSERT INTO product_count(customer_id, product_id, quantity)
                        VALUES(%s,%s,%s)''',(item['customer_id'], item['product_id'], item['q']))
        con.commit()
    
    



con.close()
    


