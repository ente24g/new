# Створюємо список для зберігання завдань
tasks = []


def add_task(task):
    """Додає нове завдання до списку"""
    tasks.append(task)
    print(f'Завдання "{task}" додано!')


def remove_task(task_number):
    """Видаляє завдання за його номером"""
    if task_number.isdigit():  # Перевіряємо, чи введено число
        task_index = int(task_number) - 1
        if 0 <= task_index < len(tasks):
            removed_task = tasks.pop(task_index)
            print(f'Завдання "{removed_task}" видалено!')
        else:
            print("Неправильний номер завдання!")
    else:
        print("Будь ласка, введіть числове значення!")


def view_tasks():
    """Виводить список завдань"""
    if tasks:
        print("Список завдань:")
        for index, task in enumerate(tasks, start=1):
            print(f'{index}. {task}')
    else:
        print("Список завдань порожній.")


def main():
    """Головна функція для взаємодії з користувачем"""
    while True:
        print("\nМеню:")
        print("1. Додати завдання")
        print("2. Видалити завдання")
        print("3. Переглянути список завдань")
        print("4. Вийти")

        choice = input("Виберіть опцію (1-4): ")

        if choice == "1":
            task = input("Введіть нове завдання: ")
            add_task(task)
        elif choice == "2":
            view_tasks()
            task_number = input("Введіть номер завдання для видалення: ")
            remove_task(task_number)
        elif choice == "3":
            view_tasks()
        elif choice == "4":
            print("Вихід із програми.")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")


# Запускаємо програму
if __name__ == "__main__":
    main()