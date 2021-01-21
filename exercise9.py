
#Question 1: write all names to a file with each name on a new line
#Question 2: extend to use try catch
#Question 3: extend to use finally
#Question 4: extend to use file context manager
people = ["John", 'John', 'John', "Sally", 'Sally', "Mark", "Lisa", 'Lisa', "Joe", 'Joe', 'Joe', 'Joe', 'Joe', "Barry", "Jane", 'Jane']

try:
    with open('people.txt', 'w') as file:
        for name in people:
            file.write(f'{name}\n')
except:
    print('Failed to open')
finally:
    file.close()
    
#Question 5: create a txt file that has the name and a count of the name
people_dictionary = {}

file = open('people.txt', 'r')

for name in file:
    if name.rstrip() not in people_dictionary:
        people_dictionary[name.rstrip()] = 1
    else:
        people_dictionary[name.rstrip()] += 1
file.close()

file = open('people_count.txt','w')

for key, value in people_dictionary.items():
    file.write(f'name:{key}, count:{value}\n')
file.close()


