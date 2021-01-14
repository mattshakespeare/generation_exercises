'''Dictionaries'''

car = {  
       'brand': 'Ford',  
       'model': 'Mustang',  
       'year' : 1964,  
       'isNew': False
       }

# #Question 1: Add new key pair to car dict for colour, and print
# car['colour'] = 'Blue'
# print(car['colour'])

# #Question 2: Update the value of the model, print new value
# car['model'] = 'Focus'
# print(car['model'])

# #Question 3: Delete model key pair from Dict
# del car['model']
# print(car)

#Question 4: Use items function to loop through dict print each key-value pair
for key, value in car.items():
    print('key: ' + str(key) + ' value: ' + str(value))
