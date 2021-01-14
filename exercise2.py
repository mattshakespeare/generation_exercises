'''control flow'''

score = int(input('Enter your score out of 100: '))

if score < 50:
    print('Your grade is E.')
elif score >= 50 and score < 60:
    print('Your grade is D.')
elif score >= 60 and score < 70:
    print('Your grade is C.')
elif score >= 70 and score < 80:
    print('Your grade is B.')
elif score >= 80 and score < 90:
    print('Your grade is A.')
else:
    print('Your grade is A*.')
    
'''Logical operators'''

user = input('Are you happy with your grade [Y/N]: ').upper()
if user == 'Y' and not score < 50:
    print('Congratulations')
elif user == 'N' and score > 50:
    print('Keep trying! You can achieve the score you want.')
elif user == 'N' and score < 50:
    print('Keep trying.')
else:
    print('Keep trying your doing great.')
