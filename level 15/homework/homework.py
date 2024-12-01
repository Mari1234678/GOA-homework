sum_even = 0
count_even = 0
number = 1

while number <= 100:
    if number % 2 == 0:
        sum_even += number
        count_even += 1
    number += 1

average = sum_even / count_even
print("Average of even numbers from 1 to 100 is:", average)

number = int(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
    year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
score = int(input("Enter a score between 1 and 100: "))

if 90 <= score <= 100:
    print("Your grade is A")
elif 80 <= score < 90:
    print("Your grade is B")
elif 70 <= score < 80:
    print("Your grade is C")
else:
    print("Your grade is D")

