import random  

# Генеруємо випадкове число від 1 до 20
secret_number = random.randint(1, 20)  #randint – це функція з модуля random, яка генерує випадкове ціле число в заданому діапазоні.

print("Я загадав число від 1 до 20. Спробуй вгадати!")

while True:
    try:
        guess = int(input("Введи своє число: "))

        if guess < 1 or guess > 20:
            print("Будь ласка, введіть число від 1 до 20.")
            continue

        if guess == secret_number:
            print("Вітаю! Ти вгадав число!")
            break
        elif guess < secret_number:
            print("Ні, моє число більше.")
        else:
            print("Ні, моє число менше.")

    except ValueError:
        print("Будь ласка, введіть коректне число.")
