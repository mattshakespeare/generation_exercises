'''functions'''

#Question 1: Take two number print and return sum
#Question 2: Extend Question 1  by passing an arbitary amount of ints.
def sum_numbers(a,b,*numbers):
    sum = a + b
    for number in numbers:
        sum += number
    return sum
sum = sum_numbers(1,1,1,1)
print(sum)

#Question 3 Pass an arbitary amount of named arguments and create a dictionary. 
def create_dictionary(**kwargs):
    dictionary = {}
    for key, value in kwargs.items():
        dictionary[key] = value
    return dictionary

dictionary = create_dictionary(a=1, b=2, c=3, d=4)
print(dictionary)
    