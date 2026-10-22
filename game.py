import random
import math
import time

with open ("file.txt", "a") as f:
   
    secret = random.randint(1, 100)
    max_attempts = 10
    attempts = 0

    print(f"Я загадав число від 1 до 100. У тебе {max_attempts} спроб!")

    while attempts < max_attempts:
        guess = int(input("Введи число: "))
        attempts += 1

        if guess < secret:
            print("Число надто мале")
        elif guess > secret:
            print("Число більше за секретне")
        else:
            print(f" Ти вгадав число! Кількість спроб: {attempts}")
            f.write(f'win:{secret}')  
            break
    else:
        print(f" Ти програв. Загадане число було: {secret}")
        f.write(f"lose:{secret}")
  
