'''age=13
if age>18:
   print('you are not old enough')
else:
    print('if you are a madrid fan benze will find you')

age=int(input('Enter your age: '))
if age>15:
    print('You are older that 15 years.')
elif age == 15:
     print('You are exactly 15 years old.')
else:
    print('you are younger than 15 years of age')

age=int(input('Enter your age: '))
income=float(input('Enter your annual income: '))

if age>18:
    if income>30000:
        print('You are eligible for loan from bank.')
    else:
        print('Your income must be at least $30,000 to aplly for this request.')

username=input('Enter a username: ')
if username== 'admin':
   print('Successfully logged in')
else:
   print('Access denied. kindly check username')

number=int(input('Enter a number: '))
print('Number to be checked: ',number)
if number %2== 0:
    print('This is an even number')

else:
    print('This is an odd number')'''

Suyog=int(input('Suyog score: '))
Sparsh=int(input('Nihal score: '))
if Sparsh>Suyog:
    print('Sparsh score is higher than Suyog')
    if Suyog>Sparsh:
       print('Suyog score is higher than sparsh')