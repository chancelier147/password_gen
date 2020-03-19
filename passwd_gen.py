#!/usr/bin/python

# random module
import random
chars = 'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*'

# the number of passwords
number = input('Number of passwords ? - ')
number = int(number)

# the length of the password
length = input('Password length ? - ')
length = int(length)

# nested for loop to generate random passwords
for p in range(number):
    password = ''
    for c in range(length):
        password += random.choice(chars)
    print(password)