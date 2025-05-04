import random

# Step 1: Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Step 2: Start guessing loop
while True:
    guess = int(input("Guess a number between 1 and 100: "))
    diff = abs(secret_number - guess)

    if guess == secret_number:
        print("🎉 Congratulations! You guessed it right!")
        break
    elif guess < secret_number:
        if diff <= 5:
            print("Just a bit low! Very close!")
        elif diff <= 15:
            print("Low, but you're getting there.")
        else:
            print("Too low! Try a much higher number.")
    else:
        if diff <= 5:
            print("Just a bit high! Very close!")
        elif diff <= 15:
            print("High, but you're getting there.")
        else:
            print("Too high! Try a much lower number.")
