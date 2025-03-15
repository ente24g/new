import random

print("🎲 Вітаємо в грі 'Вгадай число'! 🎲")
print("Комп'ютер загадав число від 1 до 100 000. Спробуй відгадати!")

random_number = random.randint(1, 100_000)
attempts = 0
last_guess = None

while True:
    user_input = input("🔢 Введіть число (або 'вийти' для завершення): ")

    if user_input.lower() == "вийти":#перекладнижній регістр
        print("🚪 Ви вийшли з гри. До зустрічі!")
        break

    if not user_input.isdigit():#не является числом
        print("⚠ Введіть число від 1 до 100 000!")
        continue

    user_guess = int(user_input)
    attempts += 1

    if user_guess < 1 or user_guess > 100_000:
        print("🚫 Число має бути в діапазоні від 1 до 100 000!")
        continue

    if last_guess is not None:
        if abs(random_number - user_guess) < abs(random_number - last_guess):
            print("🔥 Гарячіше!")
        else:
            print("❄ Холодніше!")

    last_guess = user_guess

    if user_guess < random_number:
        print(f"📈 Загадане число більше, ніж {user_guess:,}. Спробуй ще раз.")
    elif user_guess > random_number:
        print(f"📉 Загадане число менше, ніж {user_guess:,}. Спробуй ще раз.")
    else:
        print(f"🎉 Вітаємо! Ви вгадали число {random_number:,} за {attempts} спроб! 🏆")
        break