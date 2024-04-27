import random
password_chars = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
password_name = int(input("Введите длину пароля:"))
password = ""
for i in range(password_name):
        password += random.choice(password_chars)
print(password)