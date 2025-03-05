phone_book = {
    "Антон1": "123-456-789",
    "Антон2": "987-654-321",
    "Антон3": "555-123-456"
}

print("\nТелефонна книга")
print("1. Додати контакт")
print("2. Пошук контакту")
print("3. Видалити контакт")
print("4. Показати всі контакти")
print("5. Вийти")

choice = input("Оберіть дію (1-5): ")

if choice == '1':
    name = input("Введіть ім'я: ")
    phone = input("Введіть номер телефону: ")
    phone_book[name] = phone
    print(f"Контакт {name} додано/оновлено.")

elif choice == '2':
    name = input("Введіть ім'я для пошуку: ")
    if name in phone_book:
        print(f"{name}: {phone_book[name]}")
    else:
        print("Контакт не знайдено.")

elif choice == '3':
    name = input("Введіть ім'я для видалення: ")
    if name in phone_book:
        phone_book.pop(name)
        print(f"Контакт {name} видалено.")
    else:
        print("Контакт не знайдено.")

elif choice == '4':
    print("\nСписок усіх контактів😊
    for name, phone in phone_book.items():
        print(f"{name}: {phone}")

elif choice == '5':
    print("Вихід з програми. До побачення!")

else:
    print("Невірний вибір. Спробуйте ще раз.")