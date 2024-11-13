# 1)

name = "Mariami"
age = 15
float_num = 2.5
is_adult = False

print(type(name))
print(type(age))
print(type(float_num))
print(type(is_adult))

# 2)

# < > <= >= == !=

print(5 > 10) # False
print(15 < 20) # True
print(5 >= 5) # True
print(10 >= 12) # False
print(10 == 10) # True
print(10 != 10) # Fasle

# 3)

# and, or

print(True and True) # True
print(False and True) # False
print(True and False) # False
print(False and False) # False

print(True or False) # True
print(False or True) # True
print(True or True) # True
print(False or False) # False

# 4)

age = input("Please enter your age: ")
print(type(age))

age = int(age)
print(type(age))

age = float(age)
print(type(age))

# 5)

name = "Mariami"
password = "1234"

user_name = input("Please enter your name: ")
user_pass = input("Please enter a password: ")

print(name == user_name and password == user_pass)