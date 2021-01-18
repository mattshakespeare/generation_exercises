'''Modules'''
# 1. Create a Python file and import the `math` package. Use the package to print out a value using the factorial method.
# 2. Follow the same as above but this time, only import the factorial method instead of the whole package.
# 3. Follow the same as above but this time, place the factorial call in a function and return the value. Create a second file that will import this function. Call the function from that module and print out the results.from math import factorial as ft
from math import factorial as ft

def generate_factorial():
    number = int(input('Enter a number: '))
    return ft(number)

    