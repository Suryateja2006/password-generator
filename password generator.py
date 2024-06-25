import random
length = input("Enter the desired length you want: ")
while not length.isdigit() or int(length) <= 0:
    print("Invalid input. Please enter a positive integer.")
    length = input("Enter the desired length you want: ")
length = int(length)
ll = "abcdefghijklmnopqrstuvwxyz"
ul = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "1234567890"
punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
characters = ll + ul + digits + punctuation
password = ''.join(random.choice(characters) for i in range(length))
print(f"Generated password: {password}")