'''Data persistence'''

people_list = []

file = open('people.txt','r')

for name in file:
    people_list.append(name.rstrip())
print(people_list)


