username=input('username: ')
email=input('Email: ')
if username=="admin" or email=="xyz@gmail.com":
    print('Successfully logged in')
else:
    print('Enter username or email to log in')

age=int(input('Enter your age: '))
has_id=input('Write True or False')
if age>=18 and has_id=="True":
    print("you are allowed to enter")
if age<18 or not has_id:
    print("You are not allowed to enter")
if not has_id:
    print("Please bring your id next time")

score=float(input('Enter your score and Check your Grade'))
if score>=90 and score<=100:
    print('Grade A')
elif score>=80 and score<90:
    print('Grade B')
elif score>=70 and score <80:
    print('Grade C')
elif score>=60 and score <70:
    print('Grade D')
else:
    print('you have failed')

char='7'
if char.isalpha() or char.isdigit():
    print(f"{char} is an alphabet")
elif char.isdigit():
    print(f"{char} is an digit")   