'''unit testing'''

#1. Write a unit test for the below function.

def add_two_numbers(a, b):
    return a + b

def test_add_two_numbers():
    #happy path
    
    #arrange
    a = 5
    b = 5
    expected = 10
    #act
    actual = add_two_numbers(a,b)
    #assert
    assert expected == actual
    
    print(f'Test {expected == actual}')
    
    #unhappy path
    
    #arrange
    expected = 12
    #assert
    assert expected != actual
    print(f'Test {expected != actual}')

#test_add_two_numbers()

#2. Write a unit test for the function add_number_with_random_number . You will need to update the code to make use of dependency injection and create a
#mock function.

#import random

def get_random_number():
    return random.randint(1, 10)

def add_number_with_random_number(a, get_random_number):
    return a + get_random_number()

def test_add_number_with_random_number():
    #arrange
    def mock_get_random_number():
        return 10
    a = 10
    expected = 20
    #act
    actual = add_number_with_random_number(a,mock_get_random_number)
    #assert
    assert expected == actual
    print(f'Test {expected == actual}')

#test_add_number_with_random_number()

#3. Write a unit test for the below function add_two_random_numbers . You will need to update the code to make use of dependency injection and create a mock
#function.

from random import randint

def get_random_number(randint):
    return randint(1, 10)

def add_two_random_numbers(get_random_number):
    return get_random_number() + get_random_number()

def test_add_two_random_numbers():
    #arrange
    def mock_get_random_number():
        return 5
    expected = 10
    #act
    actual = add_two_random_numbers(mock_get_random_number)
    #assert
    assert actual == expected
    print(f'Test {actual == expected}')

#test_add_two_random_numbers()

#4. Write a unit test for the get_random_number function seen above. This time it's slightly different as we need to mock a function we haven't written, but the
#same principles apply. Hint: you need to match the number of arguments that the randint function takes for the mock function you will write

def test_get_random_number():
    #arrange
    def mock_randint(a,b):
        return 5
    
    expected = 5
    #act
    actual = 
    #assert
    
    
    