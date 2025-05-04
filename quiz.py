ques1=input('enter the capital of tamil nadu - ')
ques2=input('enter the color of sky - ')
answer=0
if ques1=='chennai':
    print(f"{ques1} is correct")
    answer+=1
else:
    print(f"{ques1} is incorrect")

if ques2=='blue':
    print(f"{ques2} is correct")
    answer+=1
else:
    print(f"{ques2} is incorrect")
print(f"You got {answer} answers correct.")
