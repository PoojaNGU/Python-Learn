"""a=10
b=20
c=a+b
print(c)

def add(val1,val2):
    a=val1
    b=val2
    print(a+b) 
add(5,4)"""

"""class adding:
    def add(val1,val2):
        a=val1
        b=val2
        print(a+b) 
pooja=adding
pooja.add(10,20)

def star():
    for i in range(4,10):
        print("*")
star()

for i in range(1,5):
    for j in range(1, i+1):
        print(j, end='')
    print()  


for i in range(1,11):
    print(i,"* 2 =",i*2)


while 1<11:
    print(1,"* 2 =",1*2)

a = input('Enter a number: ')
total = 0

for digit in a:
    total += int(digit)

print("Sum of digits:", total)

a=input('enter your name')
if a=='sathish':
    print(a,' babu')
else:
    print('pooja')

user_name=input('enter user name')
password=input('enter password')
if user_name=='sathish' and password=='babu':
    print('login successful')
elif user_name!='sathish':
    print('check username')
elif password!='babu':
    print('check password')
a=[2,1,4,3,7,6]
for i in range(len(a)-1):
    if a[i] > a[i+1]:
        greater_value=a[i]
    else:
        greater_value=a[i+1]
print('greatest number is:', greater_value)"""

n = int(input("How many numbers? "))
arr = []

for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    arr.append(num)

print("Your array:", arr)





   


    

    