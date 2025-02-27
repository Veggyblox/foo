'''num=int(input('Enter a number: '))
if num>0:
    if num%2==0:
        print('even and positive number')
    else:
        print('odd and positive number')
else:
    if num%2==0:
        print('even and negative number')
    else:
        print('odd and negative number') 

age=int(input('Age: '))
if age>=18:
    if age>60:
        print('your are senior citizen')
    else:
        print('your are an adult')
else:
    if age>=13:
        print('you are teen')
    else:
        print('your are a child')

medical_cause=input('did you have a medical cause Y or N: ')
atten=int(input('enter the attendance of the student: '))

if medical_cause=='Y':
   print('You are allowed')
else:
   if atten>=75:
      print('Allowed')
   else:
      print('Not allowed')

units=int(input('Units: '))
if units<100:
    amount=units*4.50+25
    print(f'your electicity bill is {amount}')
elif units>250 and units<=250:
    amount=units*7.50+50
    print(f"your electicity bill is {amount}")
elif units>250 and units<=250:
    amount=units*7.50+50
    print(f"your electricity bill is {amount}")
else:
    print('Invalid input')'''

print('Select your ride')
print('1.Bike')
print('2.Car')
choice=int(input('Enter your choice: '))
if(choice==1):
   print('1.Scooty\n')
   print('2.Scooter\n')
   choice2=int(input('Enter your Bike choice: '))
   if(choice2==1):
      print('you have selected scooty')
   else:
      print('you have selected scooter')
    
elif (choic==2):
   print('1.Toyota\n')
   print(2.BMW\n)
   choic3=int(input('Enter your car choice: '))
   if (choice3==1):
       print('you have selected Toyota')
   else:
      print('you have selected BMW')
else:
print('Invalid option')
    