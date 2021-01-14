
'''loops'''

#Question 1: print 0 to 10 using a for loop
#print message done when complete
# for i in range(0,11):
#     print(i)
# else:
#     print('Done')

#Question 2: print numbers 0 to 10 using a while loop
# counter = 0

# while counter < 10:
#     counter += 1
#     print(counter)

#Question 3: print list of numbers using a for loop
# nums = [0, 2, 8, 20, 43, 82, 195, 204, 367]

# for number in nums:
#     print(number)
    
# #Question 4: Take 2 lists if an element from the first list in second print name of element
# list1 = ["apple", "banana", "cherry", "durian", "elderberry", "fig"]
# list2 = ["avocado", "banana", "coconut", "date", "elderberry", "fig"]

# for fruit1 in list1:
#     for fruit2 in list2:
#         if fruit1 == fruit2:
#             print(fruit1)

#Question 5: every iteration generate random number, if multiple of five break, if multiple 3 continue, else print number
# import random

# def generate_random_number():
#     for num in range(0,10):
#         random_number = random.randint(0,100)
#         print(random_number)
#         if random_number % 5 == 0:
#             break
#         elif random_number % 3 == 0:
#             continue
# generate_random_number()