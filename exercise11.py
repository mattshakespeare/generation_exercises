# '''csv file'''

import csv

# # 1. Create a CSV file with whatever data you choose. Read the file and print each row. Make sure you use headers!
# with open('csv.csv', 'r') as file:
#     reader = csv.reader(file, delimiter= ',')
#     for row in reader:
#         print(row)
    
# # 2. Extend the above so that the data is read into a dictionary.
# with open('csv.csv', 'r') as file:
#     reader = csv.DictReader(file, delimiter= ',')
#     for row in reader:
#         print(row)

# 3. Write some data to a file. Choose whatever data you wish.
# dictionary = {
#     'first name':'matt',
#     'last name':'shakespeare',
#     'age':29
# }

# fieldnames = dictionary.keys()
# with open('people.csv', 'w, newline=''') as file:
#     writer = csv.DictWriter(file, fieldnames)
    
#     writer.writeheader()
#     writer.writerow(dictionary)

# 4. Write another block of code that will __append__ to the file created in #3.
# name = input('Enter your first name: ').title()
# last_name = input('Enter your last name: ').title()
# age = input('Enter your age: ').title()

# with open('people.csv', 'a', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow([name,last_name,age])

