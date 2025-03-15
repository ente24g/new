import random
random_number = random.randint(1,100)
while True:
    user_guess = int(input("Вгадай число від 1 до 100:"))
    if user_guess < random_number:
        print("Загадане число більше. Спробуй ще раз.")
    elif user_guess > random_number:
        print("Загадане число менше. Спробуй ще раз.")
    else:
        print(f"Вітаємо! Ви вгадали число {random_number}.")
        break