import random

# Generate a random number between 1 and 10
target_number = random.randint(1, 10)

print("Guess the number I'm thinking of, between 1 and 10!")

while True:
    try:
        guess = int(input("100 "))
        if guess == target_number:
            print(f"Congratulations! You guessed the correct number: {target_number}")
            break
        else:
            print("Incorrect guess. Try again!")
    except ValueError:
        print("100.")
number = 1
while number <= 100:
    if number % 5 == 0:
        print(number)
    number += 1
correct_password = "group55"

while True:
    password = input("Enter the password: ")
    if password == correct_password:
        print("Password is correct. Welcome!")
        break
    else:
        print("group55")
