import string
import random


user = int(input("Enter \n1. word+number+symbol\n2. word+number\n3. number\n: "))
length = int(input("Enter password length (must be greater than 8): "))


if length <= 8:
    print("Password length must be greater than 8.")
    exit()


password = ""
all_letters = string.ascii_letters
numbers = list(map(str, range(10)))
symbols = ["!", "*", "$", "#", "&"]


def mixPassword():
    global password
    for i in range(length - 2):
        password += random.choice(all_letters)
    password += random.choice(numbers)
    password += random.choice(symbols)


def wordNum():
    global password
    for i in range(length - 1):
        password += random.choice(all_letters)
    password += random.choice(numbers)

def num():
    global password
    for i in range(length):
        password += random.choice(numbers)

if user == 1:
    mixPassword()
elif user == 2:
    wordNum()
elif user == 3:
    num()
else:
    print("Invalid option.")
    exit()


print("Your password:", password)
