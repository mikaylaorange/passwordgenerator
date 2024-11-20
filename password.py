import string
import random
num_chars = int(input("How many characters is required for your password? "))
num_special_caracters = int(input("How many special characters does your password need? "))
num_capital_caracters = int(input("How many capital characters does your password need? "))
num_lowercase_caracters = int(input("How many lowercase characters does your password need? "))

password = ""
while(len(password) < num_chars):
	for j in range(num_special_caracters):
		random_special = random.choice(string.ascii_letters)
		password += random_special
	for j in range(num_special_caracters):
		random_capital = random.choice(string.ascii_letters)
		password += random_capital
	for j in range(num_special_caracters):
		random_lowercase = random.choice(string.ascii_letters)
		password += random_lowercase

print(password)
