'''unit testing'''

def add_two_numbers(a,b):
    if not isinstance(a,int) or not isinstance(b,int):
        return 'arguments are not int'
    try:
        a + b
    except TypeError:
        return 'can\'t add string to number.'
    else:
        return a + b

# def test_add_two_numbers():
#     #test adds two whole numbers
#     a = 1
#     b = 10
#     expected = 11
    
#     result = add_two_numbers(a,b)
    
#     assert result == expected
# test_add_two_numbers()

# def test_add_two_numbers():
#     #test adds a positive whole number and a negative whole number
#     a = -2
#     b = 1
#     expected = -1
    
#     result = add_two_numbers()
    
#     assert result == expected
#test_add_two_numbers()
    
# def test_add_two_numbers():
#     #test adds two floating point numbers
#     a = 1.1
#     b = 1.1
#     expected = 2.2
    
#     result = add_two_numbers()
    
#     assert result == expected
#test_add_two_numbers()

# def test_add_two_numbers():
#     #test adds a string to a whole number
#     a = 'string'
#     b = 20
#     expected = 'can\'t add string to number.'
    
#     result = add_two_numbers(a,b)
#     print(result)

#     assert result == expected
# test_add_two_numbers()



# def test_add_two_numbers():
#     #test adds two strings
#     a = 'Hello'
#     b = ' World!'
#     expected = 'arguments are not int'
    
#     result = add_two_numbers(a,b)
#     print(result)
    
#     assert result == expected  
# test_add_two_numbers()  