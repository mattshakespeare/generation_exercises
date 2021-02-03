import random
def get_random_number():
    return random.randint(1, 10)

def add_number_with_random_number(a, get_random_number):
    return a + get_random_number()

# # 1. Write a unit test for the function add_number_with_random_number . You will need to update the code to make use of dependency injection and create a
# # mock object.
from unittest.mock import Mock

def test_add_number_with_random_number():
    mock_get_random_number = Mock()
    mock_get_random_number.return_value = 5
    
    expected = 10
    actual = add_number_with_random_number(5, mock_get_random_number)
    
    assert expected == actual

test_add_number_with_random_number()

from random import randint

def get_random_number(randint):
    return randint(1, 10)

def test_get_random_number():
    mock_randint = Mock()
    mock_randint.return_value = 5
    
    expected = 5
    actual = get_random_number(mock_randint)
    
    assert expected == actual
    
test_get_random_number()

#3. Write a unit test for the below function. You will need to patch the input and print function. Assert what the print function was called with, and assert
#how many times the input and print function were respectively called.

def get_user_details():
    name = input('Please enter your name: ')
    age = int(input('Please enter your age: '))
    print(f'Thank you, your name is {name} and your age is {age}')

from unittest.mock import patch

@patch('builtins.input', side_effect = ['Matt', 29])
@patch("builtins.print")
def test_get_user_details(mock_print, mock_input):
    get_user_details()
    
    mock_print.assert_called_with('Thank you, your name is Matt and your age is 29')
    assert mock_input.call_count == 2
    assert mock_print.call_count == 1

test_get_user_details()
    
    
