height=float(input('height: '))
weight=float(input('weight: '))
bmi=weight/(height*height)
if bmi<18.5:.68]
    print(f'your bmi is {bmi}.you are under weight')
elif bmi>=18.5 and bmi<=24.9:
    print(f'your bmi is {bmi}.you are healthy')

elif bmi>=25 and bmi<=29.9:
    print(f'your bmi is {bmi}.you are overweigt')
elif bmi>=30 and bmi<=24.9:
    print(f'your bmi is {bmi}.you are obese')
else:
    print(f'your bmi is {bmi}.you are extremly obese')