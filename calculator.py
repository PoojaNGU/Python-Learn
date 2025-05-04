num1=int(input('enter number 1 '))
num2=int(input('enter number 2 '))
perfomance=(input('enter operation from this: \n1. add \n2. sub \n3. mul \n4. div\n' ))

if perfomance=='add':
    num3=num1+num2
    print(num3)
elif perfomance=='sub':
    print(num1-num2)
elif perfomance=='mul':
    print(num1*num2)
elif perfomance=='div':
    if num2!=0 and num1!=0:
        print(num1/num2)
    else:
        print('division by 0 is not allowed')
else:
    print('enter valid operation')
