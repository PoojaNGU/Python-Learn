#numbers = [1, 2, 3, 101, 55, 6, 7, 8, 9, 10]
n = int(input("enter your range "))
arr=[]
for i in range(n):
    a=int(input(f'enter number {i+1} '))
    arr.append(a)
print(arr)

even_count = 0
odd_count = 0

for i in arr:
    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even numbers:", even_count)
print("Odd numbers:", odd_count)